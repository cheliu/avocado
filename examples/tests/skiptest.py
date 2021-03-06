#!/usr/bin/python

from avocado import test
from avocado import job
from avocado.core import exceptions


class skiptest(test.Test):

    """
    Functional test for avocado. Throw a TestNAError (skips the test).
    """

    def action(self):
        """
        This should throw a TestNAError (skips the test).
        """
        raise exceptions.TestNAError('This test should be skipped')

if __name__ == "__main__":
    job.main()
