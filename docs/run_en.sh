#!/bin/bash
export DOCS_DIR='en'
export SITE_NAME='OONI-Research'
export SITE_URL='https://ooni-research.ocf.tw/docs/en/'
export EDIT_URI='https://github.com/ocftw/ooni-research/blob/main/docs/en/'
export SITE_DESC='OONI Probe and ASNs finding in Taiwan.'
export NAV_INTRO='Overview'
export NAV_PP='Projects'
export NAV_PPP='Preparation'
export NAV_POST='News'
export CATE_NAME='Categories'
export LANGUAGE='en'
export FONT_TEXT='Public Sans'
export FONT_CODE='DM Mono'
export OVERRIDES='overrides_en'

mkdocs build -v -d ./output/en
