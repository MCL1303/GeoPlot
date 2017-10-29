#!/bin/bash
set -eux -o pipefail
pwd
wget http://download.cdn.yandex.net/tomita/tomita-linux64.bz2 -O /tmp/tomita-linux64.bz2
bunzip2 /tmp/tomita-linux64.bz2
mv /tmp/tomita-linux64 extract/tomita-linux64
chmod +x extract/tomita-linux64
