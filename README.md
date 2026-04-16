# Bioinformatics Self-Study Curriculum

A 12-block, sprint-based self-study program covering Unix, Python, R, statistics, and applied genomics (single-cell RNA-seq, GWAS, QTL mapping). Each block is ~2 hours of hands-on work organized as 25-minute sprints with concrete checkpoints. Built for independent learners — no instructor required, all resources freely available.

The compiled curriculum is `main.pdf`.

## Build

### Prerequisites

Install a LaTeX distribution that includes `pdflatex`:

- **Linux (Debian/Ubuntu):** `sudo apt install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended`
- **macOS:** install [MacTeX](https://www.tug.org/mactex/) (or the smaller BasicTeX and then `tlmgr install` the packages below)
- **Windows:** install [MiKTeX](https://miktex.org/) or [TeX Live](https://tug.org/texlive/)

The document uses these LaTeX packages (all standard in a full TeX Live / MacTeX / MiKTeX install): `amsmath`, `amssymb`, `tcolorbox`, `tabularx`, `longtable`, `enumitem`, `booktabs`, `fancyhdr`, `titlesec`, `parskip`, `listings`, `microtype`, `seqsplit`, `hyperref`, `xcolor`, `geometry`, `lmodern`.

### Compile

Run both commands from the repository root (where `main.tex` lives):

```bash
pdflatex main.tex
pdflatex main.tex   # second pass resolves the table of contents
```

`pdflatex` writes `main.pdf` to the current directory, alongside auxiliary files (`main.aux`, `main.log`, `main.out`, `main.toc`). The first pass builds the `.aux`/`.toc` files but page numbers in the table of contents will be wrong; the second pass reads those files and produces the final 35-page PDF.

If you have `latexmk` installed, a single command handles the passes automatically:

```bash
latexmk -pdf main.tex
```

### Clean

To remove build artifacts (keeping `main.pdf`):

```bash
rm -f main.aux main.log main.out main.toc
```

Or with `latexmk`: `latexmk -c` (keeps `main.pdf`) or `latexmk -C` (also removes `main.pdf`).

## Repository layout

```
main.tex              top-level document (preamble + \input order)
main.pdf              compiled output
sections/             chapter sources (one .tex per chapter / appendix)
  00_titlepage.tex
  01_how_to_use.tex
  02_blocks_1_2_unix.tex
  03_blocks_3_4_python.tex
  04_blocks_5_6_r.tex
  05_blocks_7_8_statistics.tex
  06_blocks_9_10_applications.tex
  07_blocks_11_12_capstone.tex
  08_running_project.tex
  09_appendix_a_tools.tex
  10_appendix_b_concepts.tex
  11_appendix_c_reading.tex
```

## Curriculum at a glance

| Block | Topic | Focus |
|-------|-------|-------|
| 0     | Setup | Terminal, conda, Git, editor |
| 1–2   | Unix | Pipes, scripting, conda environments |
| 3–4   | Python | Parsing, Pandas, plotting, bio libraries |
| 5–6   | R | Bioconductor, DESeq2, ggplot2 |
| 7–8   | Statistics | Distributions, multiple testing, PCA, Bayesian ideas |
| 9–10  | Applications | scRNA-seq pipeline, GWAS pipeline |
| 11–12 | Capstone | AI-assisted analysis, Snakemake, final project |

A running four-part yeast-genetics project (growth curves → heritability → strain ID → QTL mapping) threads through blocks 5–12; see `sections/08_running_project.tex`.

## Editing

- Content edits go in the relevant file under `sections/`.
- Shared preamble (packages, colors, callout boxes, the `\sprint` macro) lives in `main.tex`.
- Use the existing callout boxes (`brainbox`, `dobox`, `tipbox`, `warnbox`, `winbox`, `restbox`) rather than inventing new ones — they carry the document's visual vocabulary.
