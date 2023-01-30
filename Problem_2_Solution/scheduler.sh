#!/bin/bash

# Add the cron jobs for the main script to the crontab file
(crontab -l 2>/dev/null; echo "0 1 * * * /usr/bin/python /AutoChek-DE-Technical-Assessment/Problem_2_Solution/main.py") | crontab -
(crontab -l 2>/dev/null; echo "0 23 * * * /usr/bin/python /AutoChek-DE-Technical-Assessment/Problem_2_Solution/main.py") | crontab -
