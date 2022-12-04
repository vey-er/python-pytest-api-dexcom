#!/bin/bash
set -eo pipefail
set -x
echo "Test started"
locust --config=Tests/api_performance/config/config.yml
