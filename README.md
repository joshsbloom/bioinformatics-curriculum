# Bioinformatics Self-Study Curriculum

A 12-block, sprint-based self-study program covering Unix, Python, R, statistics, and applied genomics (single-cell RNA-seq, GWAS, QTL mapping). Each block is ~2 hours of hands-on work organized as 25-minute sprints with concrete checkpoints. Built for independent learners — no instructor required, all resources freely available.

**[→ Read the compiled curriculum (main.pdf)](main.pdf)**

## Goals

The specific bioinformatics exercises are a vehicle for a broader set of skills. By the end of the curriculum, you should have:

- **General programming competency** in Unix, Python, and R — enough to parse files, write reusable scripts, manipulate tabular and genomic data, and make publication-quality figures.
- **A mental model of the software stack** that most bioinformatics work depends on: the OS and shell; conda environments and containers; language runtimes and their package ecosystems; domain-specific libraries and pipeline engines. Knowing which layer you are operating at is what lets you diagnose problems instead of flailing.
- **Competent use of AI tools** as part of everyday work: prompting with enough context and constraints to get runnable code, spotting hallucinated APIs, verifying against primary documentation, and treating AI output as a draft rather than an oracle.
- **The ability to ask the right question** before an analysis: what is the biological question, what would a positive result look like, what would a null result look like, what could fool you.
- **Project structure instincts**: version-controlled code, reproducible environments, ignore-listed raw data, self-explanatory directory layout, journaled progress. Work that someone else (or future you) can clone and re-run.
- **Layer-by-layer evaluation skills**: at each step of a pipeline, the ability to say what should be true, check that it is, and recognize what has gone wrong when it isn't. This is where verification and real understanding live.

## Build

The pre-built PDF is in the repo; you only need to build it yourself if you edit the sources. See **[BUILD.md](BUILD.md)** for prerequisites, compile commands, cleanup, and the repository layout.

## Curriculum at a glance

| Block | Topic | Focus |
|-------|-------|-------|
| 0     | Setup | Terminal, conda, Git, editor |
| 1–2   | Unix | Pipes, scripting, conda environments, containers |
| 3–4   | Python | Parsing, Pandas, plotting, bio libraries |
| 5–6   | R | Bioconductor, DESeq2, ggplot2 |
| 7–8   | Statistics (R) | Distributions, tests, multiple testing, linear models, power by simulation, PCA, eBayes shrinkage |
| 9–10  | Applications | scRNA-seq pipeline, GWAS pipeline |
| 11–12 | Capstone | AI-assisted analysis, Snakemake, final project |

A running four-part yeast-genetics project (growth curves → heritability → strain ID → QTL mapping) threads through Blocks 5–12; see `sections/08_running_project.tex`.
