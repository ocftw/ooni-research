#!/bin/bash
export DOCS_DIR='en'
export SITE_NAME='OONI-Research'
export SITE_URL='https://ooni-research.ocf.tw/docs/en/'
export EDIT_URI='https://github.com/ocftw/ooni-research/blob/main/docs/en/'
export SITE_DESC='OONI Probe and ASNs finding in Taiwan.'
export ENV_PP='Projects'
export LANGUAGE='en'
export FONT_TEXT='Public Sans'
export FONT_CODE='DM Mono'

mkdocs build -v -d ./output/en