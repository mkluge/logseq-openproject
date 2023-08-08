#!/bin/bash

cd `dirname $0`

rm -fr generated_api_client
mkdir generated_api_client

docker run --rm --user $(id -u):$(id -g) -e TS_POST_PROCESS_FILE="/usr/local/bin/prettier --write" -v ${PWD}:/local openapitools/openapi-generator-cli generate -g typescript-axios -i /local/openproject_api_spec.json --additional-properties=modelPropertyNaming=original --additional-properties=supportsES6=true --additional-properties=useSingleRequestParameter=true -o /local/generated_api_client

rm -fr ../openprojevt_api
mv generated_api_client ../openproject_api
