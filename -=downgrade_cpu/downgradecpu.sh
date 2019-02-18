#!/bin/sh

cpufreq-info
sudo cpufreq-set -u 950MHz
sudo cpufreq-set -c 1 -u 950MHz
echo ================================================================================
cpufreq-info

read -n 1 -s -r -p "Press any key to continue"