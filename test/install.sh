#!/bin/bash
set -eux -o pipefail
pwd
wget http://download.cdn.yandex.net/tomita/tomita-linux64.bz2 -O tomita-linux64.bz2
bunzip2 tomita-linux64.bz2
chmod +x tomita-linux64
PATH=$PATH;`pwd`
