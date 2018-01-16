#!/bin/bash
jupyter nbconvert --to script toblocks-v2.ipynb
grep -v '^$' toblocks-v2.py > toblocks.py
