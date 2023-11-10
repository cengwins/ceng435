#!/bin/bash
x=0
while [ $x -le 9 ]
do
        echo "Generating $x times"
        truncate -s 10K "small-$x.obj"
        truncate -s 10M "large-$x.obj"
        x=$(( $x + 1 ))
done