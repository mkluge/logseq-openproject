#!/bin/bash

cd `dirname $0`

yarn
npm run build
cp icon.png LICENSE  package.json dist/
