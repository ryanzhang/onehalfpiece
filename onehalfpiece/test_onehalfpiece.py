#!/usr/bin/env python

from unittest import TestCase

from onehalfpiece.main import hello_world


class HelloWordTestCase(TestCase):

    def test_hello_world(self):
        self.assertEqual('Hello World!', hello_world())
