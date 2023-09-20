#!/bin/bash

ssh root@$HOST_IP
$HOST_PASSWORD

cd /home/

git pull origin master

systemctl restart farm

exit