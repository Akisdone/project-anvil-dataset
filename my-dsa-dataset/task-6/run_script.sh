#!/bin/bash
cd "$(dirname "$0")"
python -m pytest task_tests.py -v