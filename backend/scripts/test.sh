#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

# Running unittests
coverage run --source='.' manage.py test transactions
# Generating report
coverage html

python manage.py migrate
python manage.py collectstatic --noinput --verbosity 0
python manage.py runserver_plus 0.0.0.0:8000

