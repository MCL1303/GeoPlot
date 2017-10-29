#!/usr/bin/env sh

wget http://download.cdn.yandex.net/tomita/tomita-linux64.bz2 -O /tmp/tomita.bz2
tar -xj /tmp/tomita.bz2 /usr/bin/
chmod +x /usr/bin/tomita-linux64
