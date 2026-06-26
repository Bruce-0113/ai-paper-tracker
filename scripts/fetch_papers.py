import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json
from datetime import datetime, timezone

# ── 設定 ──────────────────────────────────────────────
CATEGORIES = ["cs.AI", "cs.LG", "cs.CV", "cs.CL"]
MAX_RESULTS = 15
DATA_PATH   = "data/papers.json"
README_PATH = "README.md"
# ──────────────────────────────────────────────────────

NS = {"atom": "http://www.w3.org/2005/Atom"}


def fetch_papers() -> list[dict]:
    query = "+OR+".join(f"cat:{c}" for c in CATEGORIES)
    url = (
        "http://export.arxiv.org/api/query?"
        f"search_query={query}"
        "&sortBy=submittedDate&sortOrder=descending"
        f"&max_results={MAX_RESULTS}"
    )
    with urllib.request.urlopen(url, timeout=30) as resp:
        raw = resp.read().decode("utf-8")

    root = ET.fromstring(raw)
    papers = []
    for entry in root.findall("atom:entry", NS):
        cats = [
            t.get("term", "")
            for t in entry.findall("atom:category", NS)
        ]
        papers.append({
            "title": entry.find("atom:title", NS).text.strip().replace("\n", " "),
            "url": entry.find("atom:id", NS).text.strip(),
            "summary": entry.find("atom:summary", NS).text.strip()[:400].replace("\n", " "),
            "authors": [
                a.find("atom:name", NS).text
                for a in entry.findall("atom:author", NS)
            ],
            "published": entry.find("atom:published", NS).text[:10],
            "categories": cats,
        })
    return papers


def category_badge(cats: list[str]) -> str:
    tag_map = {
        "cs.CV": "![CV](https://img.shields.io/badge/cs.CV-blue)",
        "cs.CL": "![CL](https://img.shields.io/badge/cs.CL-green)",
        "cs.AI": "![AI](https://img.shields.io/badge/cs.AI-orange)",
        "cs.LG": "![LG](https://img.shields.io/badge/cs.LG-purple)",
    }
    badges = [tag_map[c] for c in cats if c in tag_map]
    return " ".join(badges[:3]) if badges else ""


def update_readme(papers: list[dict]) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# 🤖 Daily AI Papers\n\n",
        f"> Auto-updated every day at 09:00 Taipei time · Last sync: **{now}**\n\n",
        "Tracking: `cs.AI` · `cs.LG` · `cs.CV` · `cs.CL`\n\n",
        "---\n\n",
    ]

    for i, p in enumerate(papers, 1):
        badges = category_badge(p["categories"])
        authors_str = ", ".join(p["authors"][:3])
        if len(p["authors"]) > 3:
            authors_str += f" +{len(p['authors']) - 3} more"

        lines += [
            f"### {i}. {p['title']}\n\n",
            f"{badges}\n\n" if badges else "",
            f"📅 {p['published']} · ✍️ {authors_str}\n\n",
            f"{p['summary']}...\n\n",
            f"🔗 [Read on arXiv]({p['url']})\n\n",
            "---\n\n",
        ]

    lines.append(
        "_This README is generated automatically by "
        "[GitHub Actions](.github/workflows/fetch_papers.yml)._\n"
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.writelines(lines)


def main():
    print(f"[{datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC}] Fetching papers...")
    papers = fetch_papers()
    print(f"  ✅ Got {len(papers)} papers")

    # 每天存一個獨立檔案，同時更新 latest.json 方便程式讀取
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    payload = {"updated": datetime.now(timezone.utc).isoformat(), "papers": papers}

    daily_path = f"data/{today}.json"
    with open(daily_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    print(f"  ✅ Saved → {daily_path}")

    with open(DATA_PATH, "w", encoding="utf-8") as f:  # DATA_PATH = data/papers.json (latest)
        json.dump(payload, f, indent=2, ensure_ascii=False)
    print(f"  ✅ Updated → {DATA_PATH} (latest)")

    update_readme(papers)
    print(f"  ✅ Updated → {README_PATH}")


if __name__ == "__main__":
    main()
