#!/bin/bash
prefix=DAIC
for i in  `ls *.txt | sort`;
do
echo "Now working on $i" newName = $prefix-$i
mv" $i"" $newName";
echo "New name is $newName"
done
