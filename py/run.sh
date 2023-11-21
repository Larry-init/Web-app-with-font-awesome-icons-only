#!/bin/bash

python3 ./py/scrap.py ${BUILD_URL} > ./py/log.html || echo "Big error"
