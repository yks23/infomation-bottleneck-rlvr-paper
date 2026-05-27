#!/usr/bin/env python3
"""Download selected PDFs from papers.jsonl."""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path

import openreview


HERE = Path(__file__).resolve().parent


def sanitize_title(title: str) -> str:
    cleaned = "".join(c for c in title if c.isalnum() or c in " _-")
    cleaned = "_".join(cleaned.split())
    return cleaned[:120] or "paper"


def load_records() -> list[dict]:
    records = []
    with (HERE / "papers.jsonl").open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return records


def build_client() -> openreview.api.OpenReviewClient:
    return openreview.api.OpenReviewClient(
        baseurl="https://api2.openreview.net",
        username=os.environ.get("OPENREVIEW_USERNAME"),
        password=os.environ.get("OPENREVIEW_PASSWORD"),
    )


def selected_records(records: list[dict], ranks: list[int], all_records: bool) -> list[dict]:
    if all_records:
        return records
    wanted = set(ranks)
    return [record for record in records if int(record["rank"]) in wanted]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rank", type=int, action="append", default=[])
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--out-dir", type=Path, default=HERE / "pdfs")
    args = parser.parse_args()

    if not args.all and not args.rank:
        parser.error("Use --rank N one or more times, or use --all.")

    records = selected_records(load_records(), args.rank, args.all)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    client = build_client()

    for record in records:
        rank = int(record["rank"])
        note_id = record.get("note_id") or record.get("forum")
        title = record.get("title", "paper")
        venue = re.sub(r"[^a-zA-Z0-9_-]+", "_", record.get("venue_key", "venue"))
        path = args.out_dir / f"{rank:03d}_{venue}_{sanitize_title(title)}.pdf"
        if path.exists():
            print(f"skip existing: {path}")
            continue
        print(f"downloading #{rank}: {title}")
        pdf_bytes = client.get_attachment(field_name="pdf", id=note_id)
        tmp_path = path.with_suffix(".pdf.part")
        tmp_path.write_bytes(pdf_bytes)
        tmp_path.replace(path)
        print(f"saved: {path}")


if __name__ == "__main__":
    main()
