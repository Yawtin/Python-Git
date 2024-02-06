#!/bin/bash

echo "Please enter a number"
read num

if [ $(( num % 2 )) -eq 0 ]; then
	echo "\n Your number is even."
else
	echo "\n Your number is odd."
fi
