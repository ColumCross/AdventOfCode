#!/bin/bash

input="/home/colum/Documents/AdventOfCode/input.txt"

increases=0
decreases=0
args=()

while IFS= read -r line
do
	args+=("$input")
done < "$input"

previousLine=$args[0]

for ((i=1; i<args.length(); i++)); do
	if($args[$1] > $previousLine); then
		$increases++
	else
		$decreases++
	fi
done

echo $increases
