#!/bin/bash

python3 ./py/scrap.py --buildurl ${BUILD_URL} > ./py/log.html || echo "Big error"