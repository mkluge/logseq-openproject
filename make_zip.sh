#!/bin/bash

cd `dirname $0`

rm dist/*
yarn
yarn build
zip -r package.zip icon.png LICENSE package.json dist/
