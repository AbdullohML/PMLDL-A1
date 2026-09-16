#!/bin/bash

cd /home/abdullloh/PMLDL-A1
source .venv/bin/activate

dvc repro >> pipeline.log 2>&1
