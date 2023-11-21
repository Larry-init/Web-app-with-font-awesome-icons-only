#!/bin/bash

${BUILD_URL}
echo 'new line'
echo ${BUILD_URL}
python3 ./py/scrap.py --buildurl ${BUILD_URL} > ./py/log.html || echo "Big error"
