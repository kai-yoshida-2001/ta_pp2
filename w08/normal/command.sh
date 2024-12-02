#!/bin/bash

./clean.sh
mkdir output
touch output/snapshot_20241015_153010.zip
touch output/snapshot_20241020_203520.zip
touch output/snapshot_20241120_123430.zip
source ~/venv/py3.10.12/bin/activate
#python3 normal.py
python3 answer.py

