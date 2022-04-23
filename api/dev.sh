#!/bin/sh

# This script is used to load env variables from master env file in a dev scenario

export $(cat ../.env | xargs)
python3 app.py
