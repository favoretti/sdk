#!/bin/bash

if [ ! "$1" ]; then
    echo "package name {sdk|f5_converter|netscaler_converter} not provided"
    exit
fi

cp avi/$1/setup.py .
cp avi/$1/MANIFEST.in .
echo "uploading to the pypi "
twine upload dist/*
echo "cleanup"
if [ $1 == "sdk" ]; then
    rm -rf avisdk.egg-info
elif [ $1 == "f5_converter" ]; then
    rm -rf avif5converter.egg-info
else
    rm -rf avinetscalerconverter.egg-info
fi
rm -f setup.py
rm -f MANIFEST.in
