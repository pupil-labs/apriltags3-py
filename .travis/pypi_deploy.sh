#!/bin/bash

pip install twine || pip3 install twine
twine upload \
    --username "__token__" \
    --password "$PYPI_APITOKEN" \
    --skip-existing \
    ./dist/*
