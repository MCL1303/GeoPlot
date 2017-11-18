#!/bin/bash

for i in test/input/*.txt; do
	extract/extract-normalize $i
done

git diff --no-patch --exit-code data/facts || git checkout data/facts
