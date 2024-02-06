#!/bin/bash

echo "Please enter a file path"
read file_path

if (-f $file_path);
then
	cat $file_path
else
	touch $file_path
	echo "New File created"
fi
