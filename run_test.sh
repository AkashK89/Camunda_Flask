#!/bin/bash
#pip install -r requirements.txt
python -m coverage run .\tests\test_script.py
echo "Unittest execution done............."
python -m coverage report
python -m coverage json
echo "JSON report generated"