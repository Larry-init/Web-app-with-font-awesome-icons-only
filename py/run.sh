#!/bin/bash

python3 ./py/scrap.py --buildurl ${BUILD_URL} && > ./py/log.html 2>&1 || echo "Big error"