#!/usr/bin/env python3
"""Validate facts.json schema, uniqueness, and Wikipedia source URLs."""
import json
import sys

VALID_CATEGORIES = {
    "space", "biology", "science", "history",
    "culture", "tech", "food", "geography"
}

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "facts.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert isinstance(data, list) and len(data) > 0, "facts.json must be a non-empty JSON array"
    seen_ids = set()
    for i, item in enumerate(data):
        for key in ("id", "category", "title", "body", "highlights", "sourceTitle", "sourceUrl"):
            assert key in item and item[key], f"Item #{i} missing required field: {key}"
        assert item["id"] not in seen_ids, f"Duplicate fact id: {item['id']}"
        seen_ids.add(item["id"])
        assert item["category"] in VALID_CATEGORIES, f"Invalid category in {item['id']}: {item['category']}"
        assert item["sourceUrl"].startswith("https://"), f"Non-HTTPS sourceUrl in {item['id']}"
        assert isinstance(item["highlights"], list) and len(item["highlights"]) >= 1, f"Empty highlights in {item['id']}"
    print(f"OK: {len(data)} facts validated cleanly.")

if __name__ == "__main__":
    main()
