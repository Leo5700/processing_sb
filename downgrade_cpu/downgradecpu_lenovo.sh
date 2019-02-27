#!/bin/sh

cpufreq-info
# sudo cpufreq-set -u 800Hz
# sudo cpufreq-set -u 1070MH
# sudo cpufreq-set -u 1330MH
sudo cpufreq-set -u 1600MH
echo ================================================================================
cpufreq-info

read 1 -s -r -p "Press any key to continue"
