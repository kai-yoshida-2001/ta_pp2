#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 basic_operation.py
libreoffice --nologo --writer output/new.docx
