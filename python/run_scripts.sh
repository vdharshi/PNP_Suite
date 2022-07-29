#!/bin/bash

echo enter the path
read p
cd $p

ls $p > /home/run.txt

while read line
do

python3 $line


done < /home/run.txt
