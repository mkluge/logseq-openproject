#!/bin/bash

cd `dirname $0`

rm dist/*
yarn
yarn build
cp icon.png LICENSE package.json dist/
