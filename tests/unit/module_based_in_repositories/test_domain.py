from unittest import mock
from tests.unit.base import TestCase


class TestClassA(TestCase):

    def test_should_assert_something(self):
        self.assertTrue(True)

    def test_should_assert_something_else(self):
        self.assertEqual(1, 1)


class TestClassB(TestCase):

    def test_should_assert_something(self):
        self.assertTrue(True)

    def test_should_assert_something_else(self):
        self.assertEqual(1, 1)
