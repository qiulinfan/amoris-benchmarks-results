"""Replaces docs/bench/taau.md section 3's tables with the ones in doc_tables.md (quiet runs).

The doc's tables appear in this order: check 1600, check 2560, auto 1600, auto 2560, off 1600,
off 2560, then the fixed/wall tables for check, auto, off. doc_tables.md prints them in the same
order. Each table is a run of lines starting with '|'.
"""
import sys

doc_path, tables_path = sys.argv[1], sys.argv[2]


def tables(lines):
    out, cur = [], []
    for ln in lines:
        if ln.startswith("|"):
            cur.append(ln)
        elif cur:
            out.append(cur)
            cur = []
    if cur:
        out.append(cur)
    return out


new = tables(open(tables_path, encoding="utf-8").read().splitlines())
assert len(new) == 9, len(new)
doc = open(doc_path, encoding="utf-8").read().splitlines()
start = doc.index("## 3. Cost")
end = doc.index("**Chrome** (155, WebGPU through Direct3D 12, the RTX 5060 with `--force_high_performance_gpu`; the")
out, i, k = doc[:start], start, 0
while i < end:
    if doc[i].startswith("|"):
        j = i
        while doc[j].startswith("|"):
            j += 1
        old = doc[i:j]
        assert old[0] == new[k][0], (old[0], new[k][0])
        assert len(old) == len(new[k]), (len(old), len(new[k]))
        for a, b in zip(old, new[k]):
            assert a.split("|")[1] == b.split("|")[1], (a, b)
        out += new[k]
        k += 1
        i = j
    else:
        out.append(doc[i])
        i += 1
assert k == 9, k
out += doc[end:]
open(doc_path, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
print("replaced", k, "tables")
