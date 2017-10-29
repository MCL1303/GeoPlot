#!/bin/bash
set -eux -o pipefail

wget http://download.cdn.yandex.net/tomita/tomita-linux64.bz2 -O /usr/bin/tomita-linux64.bz2
bunzip2 /usr/bin/tomita-linux64.bz2
chmod +x /usr/bin/tomita-linux64
