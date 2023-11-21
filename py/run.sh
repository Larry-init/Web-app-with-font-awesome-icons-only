#!/bin/bash

echo ${BUILD_URL}
echo $BUILD_URL
# python3 py/scrap.py --buildurl $BUILD_URL > py/log.html 2>&1 || echo "Big error"
python3 /var/jenkins_home/workspace/myyg_master/py/scrap.py --buildurl $BUILD_URL > /var/jenkins_home/workspace/myyg_master/py/log.html 2>&1 || echo "Big error"
