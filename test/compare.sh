#!/bin/bash

for i in test/data/input/*.txt; do
	extract/extract-normalize $i
done

git diff --no-patch --exit-code test/data/facts || {
	git checkout test/data/facts
	exit 1
}
