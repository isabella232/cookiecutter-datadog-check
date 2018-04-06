# (C) Datadog, Inc. 2010-2017
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)
from datadog_checks.{{cookiecutter.check_name}} import {{cookiecutter.class_name}}


def test_check(aggregator):
    c = {{cookiecutter.class_name}}('{{cookiecutter.check_name}}', {}, {}, None)
    c.check({})
    aggregator.assert_all_metrics_covered()
