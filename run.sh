#!/bin/bash

catimg -w 100 tux.png > tux.txt

echo
python3 rafetch.py
echo
pr -mts tux.txt output.txt
echo
