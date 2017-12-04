#!/bin/bash
set -euo pipefail

find test/data/facts/ -type f -name "*.xml" -print0 | xargs -n1 -0 model/build

git diff --exit-code model/models
