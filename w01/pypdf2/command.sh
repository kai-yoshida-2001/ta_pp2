#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 basic_operation.py
evince output/division.pdf
