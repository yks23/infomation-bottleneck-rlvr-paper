# Verifiable Rewards as an Information Bottleneck

This repository contains the writing source for the paper draft
`Verifiable Rewards as an Information Bottleneck`.

## Structure

- `main.tex`: paper entry point.
- `sections/`: section-level LaTeX sources.
- `references.bib`: bibliography.
- `notes/`: reading lists and background notes.
- `data/`: paper metadata used by the reading-list scripts.
- `scripts/`: optional helper scripts for rebuilding reading lists or fetching PDFs.

## Build

The project uses `latexmk` with the repository-local `.latexmkrc`.

```sh
make
```

The generated PDF is written to `build/main.pdf`.

To remove auxiliary files:

```sh
make clean
```

To remove the full build directory:

```sh
make distclean
```
