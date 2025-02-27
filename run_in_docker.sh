source ./env_docker.sh
DATE_WITH_TIME= 'date + "+%Y%m%d_%H%M%S"'

set -x
docker run \
 -v $(pwd)/api_udemy_course:/automation/api_udemy_course \
 -e MACHINE=${MACHINE} udemy_api \
 pytest -c /automation/pyproject.toml \
 --color=yes \
 --html /automation/reports/my_results_${DATE_WITH_TIME}.html \
 /automation/api_udemy_course/tests/