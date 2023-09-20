#!/bin/bash

ssh root@$HOST_IP "$HOST_PASS;cd /home/;git pull origin master;systemctl restart farm;exit"








