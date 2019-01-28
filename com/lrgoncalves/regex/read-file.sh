#!/bin/bash
filename=$1
#echo $filename
while read -r line; do
    name=$line
    scrapeli --user=$name > $name.json
done < $filename
