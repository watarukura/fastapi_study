#!/bin/bash

set -euo pipefail

# shopt -s expand_aliases
# alias aws="docker run --rm -it amazon/aws-cli"

function init_ddb() {
    aws dynamodb delete-table \
        --table-name user \
        --no-paginate \
        --endpoint-url http://localhost:18000 || true

    aws dynamodb create-table \
        --table-name user \
        --attribute-definitions AttributeName=id,AttributeType=N \
        --key-schema AttributeName=id,KeyType=HASH \
        --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
        --no-paginate \
        --endpoint-url http://localhost:18000
}

init_ddb
