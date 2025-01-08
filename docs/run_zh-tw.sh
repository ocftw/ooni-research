#!/bin/bash
export SITE_URL='https://ooni-research.ocf.tw/docs/zh-tw/'

mkdocs build -v -s -d ./output/zh-tw
