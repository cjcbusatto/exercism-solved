#!/bin/bash

if [ "$1" = "total" ]
then
    echo 18446744073709551615
    exit 0
elif [ "$1" -lt "1" ] || [ "$1" -gt "64" ]
then
    echo "Error: invalid input"
    exit 1
elif [ "$1" -eq "1" ]
then
    echo 1
    exit 0
else
    echo $((2**$(($1-1))))
    exit 0
fi

