#!/bin/bash
gpio -g mode 22 in
gpio -g mode 16 out
led="0"
encen="1"
apag="0"
ejec="0"
while true;

 do
ejec="0"
echo -n "Waiting for button ... "
  while [ `gpio -g read 22` = 0 ]; do
    sleep 0.1
  done
if [ `gpio -g read 22` = 1 ];
then
echo "pulsado"

while [ `gpio -g read 22` = 1 ]; do
    sleep 0.1
done

if [ $led -eq $encen ];

then
if [ $ejec -eq "0" ];
then
led="0"
ejec="1"
gpio -g write 16 0
echo "apagado"
fi
fi

if [ $led -eq $apag ];
then
if [ $ejec -eq "0" ];
then
led="1"
ejec="1"
gpio -g write 16 1
  echo "encencdido"
fi
fi
fi
done



