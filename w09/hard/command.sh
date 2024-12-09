#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
#python3 hard.py
python3 answer.py
libreoffice --nologo --writer ./output/output_example.xlsx
