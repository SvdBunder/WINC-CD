#!/bin/bash

ssh root@$HOST_IP "cd /home/;git pull origin master;systemctl restart farm;exit"








