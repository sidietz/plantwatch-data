#!/bin/bash

for f in *.csv; do
    psql -d plantwatch -c "\copy power FROM $f delimiter ',' csv header"
done
