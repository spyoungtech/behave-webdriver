import pytest
import sys
import os
present_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(present_dir, '..', '..'))
sys.path.insert(0, root_dir)
from behave_webdriver import NoTransformation, FormatTransformation, transform_parameter


class TestContext(object):
    pass


def test_no_transformation_evaluation_returns_unmodified_value():
    in_value = 'initial parameter value'
    out_value = NoTransformation().eval(in_value)
    assert out_value == in_value


def test_format_transformation_replaces_placeholders():
    in_value = '{schema}://{host}:{port}/{path}'
    out_value = FormatTransformation(schema='https', host='example.com', port=8443, path='hello').eval(in_value)
    assert out_value == 'https://example.com:8443/hello'


def test_transformation_is_retrieved_from_context():
    c = TestContext()
    setattr(c, 'parameter_transformation', FormatTransformation(TEST_SLUG='testxyz'))
    v = transform_parameter(c, '!{TEST_SLUG}?')
    assert v == '!testxyz?'