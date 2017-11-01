#!/bin/bash
set -eux -o pipefail

cd extract
wget http://download.cdn.yandex.net/tomita/tomita-linux64.bz2
bunzip2 tomita-linux64.bz2
chmod +x tomita-linux64
