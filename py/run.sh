#!/bin/bash

echo ${BUILD_URL}
echo $BUILD_URL
python3 ./py/scrap.py --buildurl $BUILD_URL > ./py/log.txt 2>&1 || echo "Big error"
