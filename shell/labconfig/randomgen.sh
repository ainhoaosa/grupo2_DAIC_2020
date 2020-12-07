#!/bin/bash

#!/bin/bash
#!/bin/bash
 RANDOM=$(date +%s)
for i in `seq 1 20`;
do
	 RANDOM=$(date +%s)
	MyNum=$(( $RANDOM % 10 ))
      	echo  "numero $i $MyNum" >> /home/pi/labconfig/numbers.txt
	echo "$MyNum $i"
	sleep 10
done
