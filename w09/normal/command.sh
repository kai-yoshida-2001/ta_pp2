#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
#python3 normal.py
python3 answer.py
libreoffice --nologo --writer ./output/normal_example.xlsx
