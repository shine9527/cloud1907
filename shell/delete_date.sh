#!/usr/bin/env bash
#
# ...
# ...


for i in $(seq 5); do
  sed -i "/.*2019-0${i}-.*/d" $1
done
