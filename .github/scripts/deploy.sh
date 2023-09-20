#!/bin/bash

echo SSH root@$HOST_IP
echo $HOST_PASSWORD

cd /home

git pull origin master

systemctl restart farm

exit