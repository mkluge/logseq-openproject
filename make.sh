#!/bin/bash

cd `dirname $0`

rm dist/*
yarn
npm run build
cp icon.png LICENSE package.json dist/
