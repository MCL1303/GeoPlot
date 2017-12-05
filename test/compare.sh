#!/bin/bash
set -euo pipefail

for i in test/data/input/*.txt; do
	extract/extract-normalize $i
done

git diff --exit-code test/data/facts
