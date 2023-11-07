#!/bin/bash

python3 ./py/scrapy.py || echo "Big error" > ./log.txt
