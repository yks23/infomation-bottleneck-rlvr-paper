#!/usr/bin/env python3
"""Build a focused RLVR information-bottleneck reading list from OpenReview metadata."""

from __future__ import annotations

import csv
import json
import math
import re
from collections import Counter
from pathlib import Path
from textwrap import shorten


ROOT = Path(__file__).resolve().parents[2]
METADATA_DIR = ROOT / "dev" / "metadata"
OUT_DIR = Path(__file__).resolve().parent
QUERY_FILE = ROOT / "dev" / "query_rlvr_information_bottleneck.txt"

TOKEN_RE = re.compile(r"[a-zA-Z][a-zA-Z0-9_+-]{2,}")
STOPWORDS = {
    "the", "and", "for", "with", "from", "that", "this", "are", "can", "into",
    "has", "have", "not", "but", "our", "their", "its", "using", "use", "used",
    "such", "may", "all", "both", "than", "then", "where", "while", "which",
    "between", "through", "toward", "towards", "paper", "study", "propose",
    "large", "language", "models", "model", "llms", "llm",
}

THEMES = {
    "core_rlvr_feedback_bottleneck": [
        "verifiable reward", "rlvr", "binary feedback", "sparse verifier",
        "zero-variance", "advantage collapse", "identical rewards", "all responses",
        "reward sparsity", "sparse feedback",
    ],
    "information_entropy_theory": [
        "information theory", "information gain", "information bottleneck",
        "entropy", "mutual information", "feedback entropy", "token entropy",
        "policy entropy", "outcome entropy",
    ],
    "reward_granularity_dense_feedback": [
        "dense reward", "hybrid reward", "reward model", "process reward",
        "partial credit", "step-level", "fine-grained", "rubric", "verifier",
        "reward shaping",
    ],
    "exploration_rollout_diversity": [
        "exploration", "rollout", "trajectory diversity", "diverse trajectories",
        "sampling efficiency", "adaptive sampling", "rollout allocation",
        "curriculum", "temperature", "policy optimization",
    ],
}

PRIORITY_IDS = {
    "0CajQNVKyB",
    "kiXFIESZKv",
    "Z5sWYACAop",
    "qkWP6phrvZ",
    "4nLvUk8edu",
    "sE8DCSJTzd",
    "ObF4WIMkY6",
    "LZZENDlZt9",
    "Uro84w2xz5",
    "pRSRiXdpkm",
}


def normalize(text: str) -> str:
    return " ".join(str(text or "").split())


def tokenize(text: str) -> list[str]:
    return [
        token.lower()
        for token in TOKEN_RE.findall(text)
        if token.lower() not in STOPWORDS
    ]


def load_records() -> list[dict]:
    records = []
    for path in sorted(METADATA_DIR.glob("*_metadata.jsonl")):
        with path.open(encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    record = json.loads(line)
                    record["title"] = normalize(record.get("title"))
                    record["abstract"] = normalize(record.get("abstract"))
                    record["keywords"] = normalize(record.get("keywords"))
                    records.append(record)
    return records


def tf(tokens: list[str]) -> Counter:
    counts = Counter(tokens)
    total = sum(counts.values()) or 1
    return Counter({key: value / total for key, value in counts.items()})


def tfidf_scores(query: str, records: list[dict]) -> dict[str, float]:
    docs = [
        tokenize(" ".join([r.get("title", ""), r.get("abstract", ""), r.get("keywords", "")]))
        for r in records
    ]
    doc_freq = Counter()
    for doc in docs:
        doc_freq.update(set(doc))

    n_docs = len(records) or 1
    query_tf = tf(tokenize(query))
    query_weights = {
        token: weight * math.log((n_docs + 1) / (doc_freq.get(token, 0) + 1)) + 1.0
        for token, weight in query_tf.items()
    }
    query_norm = math.sqrt(sum(weight * weight for weight in query_weights.values())) or 1.0

    scores = {}
    for record, doc in zip(records, docs):
        doc_tf = tf(doc)
        dot = 0.0
        doc_norm_sq = 0.0
        for token, weight in doc_tf.items():
            token_weight = weight * math.log((n_docs + 1) / (doc_freq.get(token, 0) + 1)) + 1.0
            doc_norm_sq += token_weight * token_weight
            dot += query_weights.get(token, 0.0) * token_weight
        doc_norm = math.sqrt(doc_norm_sq) or 1.0
        scores[record_key(record)] = dot / (query_norm * doc_norm)
    return scores


def record_key(record: dict) -> str:
    return record.get("forum") or record.get("note_id") or record.get("url")


def theme_hits(record: dict) -> dict[str, list[str]]:
    text = " ".join([
        record.get("title", ""),
        record.get("abstract", ""),
        record.get("keywords", ""),
    ]).lower()
    hits = {}
    for theme, keywords in THEMES.items():
        matched = [kw for kw in keywords if kw in text]
        if matched:
            hits[theme] = matched
    return hits


def select_records(records: list[dict], scores: dict[str, float]) -> list[dict]:
    selected = []
    for record in records:
        hits = theme_hits(record)
        score = scores.get(record_key(record), 0.0)
        forum = record.get("forum") or record.get("note_id")
        text = " ".join([record.get("title", ""), record.get("abstract", "")]).lower()
        has_required_context = "rlvr" in text or "verifiable reward" in text or "reinforcement learning" in text
        if forum in PRIORITY_IDS or (has_required_context and hits and score >= 0.075):
            keyword_score = sum(len(v) for v in hits.values())
            record = dict(record)
            record["similarity_score"] = round(score, 6)
            record["keyword_score"] = keyword_score
            record["themes"] = ";".join(hits)
            record["matched_keywords"] = "; ".join(
                f"{theme}: {', '.join(words)}" for theme, words in hits.items()
            )
            selected.append(record)
    selected.sort(
        key=lambda r: (
            record_key(r) in PRIORITY_IDS,
            r["similarity_score"],
            r["keyword_score"],
        ),
        reverse=True,
    )
    return selected[:80]


def write_csv(records: list[dict]) -> None:
    fields = [
        "rank",
        "similarity_score",
        "keyword_score",
        "venue_key",
        "venue",
        "title",
        "authors",
        "url",
        "themes",
        "matched_keywords",
        "abstract",
        "note_id",
        "forum",
    ]
    with (OUT_DIR / "papers.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for idx, record in enumerate(records, start=1):
            row = {field: record.get(field, "") for field in fields}
            row["rank"] = idx
            writer.writerow(row)


def write_jsonl(records: list[dict]) -> None:
    with (OUT_DIR / "papers.jsonl").open("w", encoding="utf-8") as f:
        for idx, record in enumerate(records, start=1):
            record = dict(record)
            record["rank"] = idx
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


def paper_line(idx: int, record: dict) -> str:
    abstract = shorten(record.get("abstract", ""), width=650, placeholder="...")
    return (
        f"### {idx}. [{record.get('title')}]({record.get('url')})\n"
        f"- Venue: {record.get('venue_key')} / {record.get('venue')}\n"
        f"- Score: {record.get('similarity_score')} | Themes: `{record.get('themes')}`\n"
        f"- Keywords: {record.get('matched_keywords')}\n"
        f"- Abstract: {abstract}\n"
    )


def write_markdown(records: list[dict]) -> None:
    top = records[:25]
    lines = [
        "# Information Bottleneck x RLVR Reading List",
        "",
        "This folder collects OpenReview papers related to information theory, information bottlenecks, entropy, feedback granularity, and RLVR.",
        "",
        "Sources: NeurIPS 2025 and ICLR 2026 OpenReview accepted-paper metadata. ICML 2026 currently has no accepted records in OpenReview metadata.",
        "",
        "## Start Here",
        "",
    ]
    lines.extend(paper_line(idx, record) for idx, record in enumerate(top[:12], start=1))
    lines.extend([
        "## Theme Views",
        "",
    ])
    for theme in THEMES:
        themed = [record for record in records if theme in record.get("themes", "")]
        if not themed:
            continue
        lines.append(f"### {theme}\n")
        for record in themed[:12]:
            lines.append(f"- [{record.get('title')}]({record.get('url')}) ({record.get('venue_key')}, score={record.get('similarity_score')})")
        lines.append("")

    lines.extend([
        "## Files",
        "",
        "- `papers.csv`: sortable spreadsheet-style index.",
        "- `papers.jsonl`: machine-readable records.",
        "- `download_pdfs.py`: downloads selected PDFs by rank or all records.",
        "- `pdfs/`: default output folder for downloaded PDFs.",
        "",
        "## Download Examples",
        "",
        "```sh",
        "python3 download_pdfs.py --rank 1 --rank 2 --rank 3",
        "python3 download_pdfs.py --all",
        "```",
        "",
    ])
    (OUT_DIR / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    records = load_records()
    query = QUERY_FILE.read_text(encoding="utf-8")
    scores = tfidf_scores(query, records)
    selected = select_records(records, scores)
    write_csv(selected)
    write_jsonl(selected)
    write_markdown(selected)
    print(f"Wrote {len(selected)} selected papers to {OUT_DIR}")


if __name__ == "__main__":
    main()
