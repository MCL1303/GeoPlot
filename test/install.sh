#!/bin/bash
set -eux -o pipefail

wget http://download.cdn.yandex.net/tomita/tomita-linux64.bz2 -O /tmp/tomita-linux64.bz2
bunzip2 /tmp/tomita-linux64.bz2
sudo mv /tmp/tomita-linux64 /usr/bin/tomita-linux64
sudo chmod +x /usr/bin/tomita-linux64
