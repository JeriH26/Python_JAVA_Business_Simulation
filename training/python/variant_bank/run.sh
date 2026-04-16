#!/usr/bin/env bash
set -euo pipefail

for f in training/python/variant_bank/solutions/v*.py; do
  echo "===== Running ${f} ====="
  python3 "$f"
  echo
done
