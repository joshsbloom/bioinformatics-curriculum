"""Generate small, realistic-looking data files for the curriculum.

Outputs (written to ../data/ relative to this script's runtime cwd):
  counts.tsv       gene_id, chromosome, sample1..sample4 (raw counts)
  sample_info.tsv  sample, condition, replicate
  de_results.csv   gene, chromosome, sample, log2FC, p.value, pAdj
  peaks.bed        chrom, start, end, name, score (BED5)

Reproducible via fixed seed. Tiny by design (~50 genes, 30 peaks).
"""
import os
import random
import math

random.seed(42)

OUT = "/home/jbloom/Dropbox/Tutorials/AI_Comp_Curriculum/data"

# ---- 50 yeast-flavored gene IDs across chrI..chrV (rough plausibility) -----
chroms = ["chrI", "chrII", "chrIII", "chrIV", "chrV"]
genes = []
for i in range(50):
    chrom = chroms[i % 5]
    name = f"YGENE{i+1:03d}"
    genes.append((name, chrom))

# ---- counts.tsv: 4 samples, 2 control + 2 treated, with realistic-ish DE ----
samples = ["sample1", "sample2", "sample3", "sample4"]
conditions = {"sample1": "control", "sample2": "control",
              "sample3": "treated", "sample4": "treated"}

# Pre-decide per-gene baseline + DE effect, so de_results.csv lines up with counts
gene_truth = {}
for gname, chrom in genes:
    baseline = random.choice([10, 30, 80, 200, 500, 1500])
    effect_dir = random.choice([-1, 1])
    effect_mag = random.choice([0.0, 0.0, 0.0, 0.5, 1.2, 2.5])  # most are null
    log2fc_true = effect_dir * effect_mag
    gene_truth[gname] = (baseline, log2fc_true)

with open(os.path.join(OUT, "counts.tsv"), "w") as f:
    f.write("gene_id\tchromosome\tsample1\tsample2\tsample3\tsample4\n")
    for gname, chrom in genes:
        baseline, log2fc = gene_truth[gname]
        row = [gname, chrom]
        for s in samples:
            mean = baseline
            if conditions[s] == "treated":
                mean = baseline * (2 ** log2fc)
            # Add Poisson-ish noise via gauss on log scale, clamp to >=0 int
            noisy = max(0, int(round(random.gauss(mean, max(2, mean ** 0.5)))))
            row.append(str(noisy))
        f.write("\t".join(row) + "\n")

# ---- sample_info.tsv ----
with open(os.path.join(OUT, "sample_info.tsv"), "w") as f:
    f.write("sample\tcondition\treplicate\n")
    for s in samples:
        rep = "1" if s.endswith(("1", "3")) else "2"
        f.write(f"{s}\t{conditions[s]}\t{rep}\n")

# ---- de_results.csv: matches counts.tsv genes, plus a per-gene 'sample' label
# (the column a reviewer might use to track which sample first detected the
# transcript; user requested it). p.value scales with effect mag.
with open(os.path.join(OUT, "de_results.csv"), "w") as f:
    f.write("gene,chromosome,sample,log2FC,p.value,pAdj\n")
    pvals = []
    rows = []
    for gname, chrom in genes:
        _, log2fc_true = gene_truth[gname]
        # observed log2FC = truth + small noise
        log2fc = log2fc_true + random.gauss(0, 0.2)
        # p-value: large effects -> small p; null effects -> ~uniform
        if abs(log2fc_true) < 0.1:
            p = random.random()
        else:
            p = max(1e-12, math.exp(-abs(log2fc_true) * 4) * random.random())
        first_sample = random.choice(samples)
        rows.append([gname, chrom, first_sample, log2fc, p])
        pvals.append(p)
    # BH adjustment
    n = len(pvals)
    order = sorted(range(n), key=lambda i: pvals[i])
    padj = [0.0] * n
    prev = 1.0
    for rank, i in enumerate(reversed(order), start=1):
        k = n - rank + 1  # original BH rank
        v = pvals[i] * n / k
        prev = min(prev, v)
        padj[i] = min(1.0, prev)
    for r, pa in zip(rows, padj):
        gname, chrom, s, log2fc, p = r
        f.write(f"{gname},{chrom},{s},{log2fc:.3f},{p:.4g},{pa:.4g}\n")

# ---- peaks.bed: 30 peaks scattered across same yeast chroms ----
chrom_lengths = {"chrI": 230218, "chrII": 813184, "chrIII": 316620,
                 "chrIV": 1531933, "chrV": 576874}
with open(os.path.join(OUT, "peaks.bed"), "w") as f:
    for i in range(30):
        chrom = random.choice(chroms)
        L = chrom_lengths[chrom]
        start = random.randint(1000, L - 5000)
        end = start + random.randint(200, 1500)
        score = random.randint(50, 1000)
        f.write(f"{chrom}\t{start}\t{end}\tpeak{i+1:03d}\t{score}\n")

print("wrote files to", OUT)
for fn in ("counts.tsv", "sample_info.tsv", "de_results.csv", "peaks.bed"):
    p = os.path.join(OUT, fn)
    n = sum(1 for _ in open(p))
    print(f"  {fn}: {n} lines")
