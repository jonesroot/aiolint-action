#!/bin/bash

echo "Running AIOLint..."
python /app/scripts/lint_checker.py

if [ "$1" == "true" ]; then
  echo "Running auto-fix..."
  python /app/scripts/fix_code.py
fi
