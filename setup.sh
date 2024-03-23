#!/usr/bin/env bash

# exit when command fails
set -o errexit

## install dependencies via pip
pip install -r dependencies.txt

## run migration just in case
python manage.py migrate