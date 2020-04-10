#!/bin/bash
# the size of the body
curl -w "%{size_download}\n" -so /dev/null "$1"
