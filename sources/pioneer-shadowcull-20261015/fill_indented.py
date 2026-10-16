"""Fill a paragraph (stdin) with a fixed indent using tools/wrap_docs.py's rules."""
import sys
sys.path.insert(0, sys.argv[1])
import wrap_docs as w
indent = sys.argv[2] if len(sys.argv) > 2 else "  "
sys.stdin.reconfigure(encoding="utf-8"); sys.stdout.reconfigure(encoding="utf-8")
text = sys.stdin.read().strip()
print("\n".join(w.fill(text, indent, indent)))
