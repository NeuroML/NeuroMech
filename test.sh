#!/bin/bash
set -ex

# Format the code
ruff format *.py

python neuromlmech_spec.py