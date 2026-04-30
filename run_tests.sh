#!/bin/bash
source venv/Scripts/activate
pytest test_app.py -v
if [ $? -eq 0 ]; then
    echo "All tests passed."
    exit 0
else
    echo "Some tests failed."
    exit 1
fi