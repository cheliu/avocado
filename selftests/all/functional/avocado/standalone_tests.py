#!/usr/bin/env python

import unittest
import os
import sys

# simple magic for using scripts within a source tree
basedir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
basedir = os.path.abspath(basedir)
if os.path.isdir(os.path.join(basedir, 'avocado')):
    sys.path.append(basedir)

from avocado.utils import process


class StandaloneTests(unittest.TestCase):

    def setUp(self):
        self.original_pypath = os.environ.get('PYTHONPATH')
        if self.original_pypath is not None:
            os.environ['PYTHONPATH'] = '%s:%s' % (basedir, self.original_pypath)
        else:
            os.environ['PYTHONPATH'] = '%s' % basedir

    def run_and_check(self, cmd_line, expected_rc, tstname):
        os.chdir(basedir)
        result = process.run(cmd_line, ignore_status=True)
        self.assertEqual(result.exit_status, expected_rc,
                         "Stand alone %s did not return rc "
                         "%d:\n%s" % (tstname, expected_rc, result))

    def test_passtest(self):
        cmd_line = './examples/tests/passtest.py'
        expected_rc = 0
        self.run_and_check(cmd_line, expected_rc, 'passtest')

    def test_skiptest(self):
        cmd_line = './examples/tests/skiptest.py'
        expected_rc = 0
        self.run_and_check(cmd_line, expected_rc, 'skiptest')

    def test_failtest(self):
        cmd_line = './examples/tests/failtest.py'
        expected_rc = 1
        self.run_and_check(cmd_line, expected_rc, 'failtest')

    def test_errortest(self):
        cmd_line = './examples/tests/errortest.py'
        expected_rc = 1
        self.run_and_check(cmd_line, expected_rc, 'errortest')

    def test_warntest(self):
        cmd_line = './examples/tests/warntest.py'
        expected_rc = 1
        self.run_and_check(cmd_line, expected_rc, 'warntest')

if __name__ == '__main__':
    unittest.main()
