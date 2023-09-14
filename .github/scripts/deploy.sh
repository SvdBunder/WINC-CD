#!/bin/bash

SSH root@178.62.217.227

cd /home

git pull origin master

systemctl restart farm

systemctl status farm