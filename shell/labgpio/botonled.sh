#!/bin/bash
gpio -g mode 22 in
gpio -g mode 16 out

while true;

 do
echo -n "Waiting for button ... "
  while [ `gpio -g read 22` = 0 ]; do
    sleep 0.1
  done
if [ `gpio -g read 22` = 1 ];
then
echo  "encendido"
while [ `gpio -g read 22` = 1 ]; do
    sleep 0.1
gpio -g write 16 1
 
  done
fi
gpio -g write 16 0
  echo "apagado"
done
