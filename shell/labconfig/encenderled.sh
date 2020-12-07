#!/bin/bash
cpu=$(</sys/class/thermal/thermal_zone0/temp)
cpuuse=$(cat /proc/stat | awk '{print $1}')
echo "$(date) @ $(hostname)"
echo "-------------------------------------------"
while true;
do
grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage "%"}'
echo "GPU => $(/opt/vc/bin/vcgencmd measure_temp)"
echo "CPU $((`cat /sys/class/thermal/thermal_zone0/temp`/1000))"
grep 'cpu ' /proc/meminfo | awk '{usage=($4)*100/($1+$2)} END {print usage "%"}'

sleep 0.2
done
