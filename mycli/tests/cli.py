import os
import sys

try:
    from StringIO import StringIO  # python 2
except ImportError:
    from io import StringIO  # python 3
import unittest

from mycli.cli import create_parser
from mycli.prt import prt

class mycliTests(unittest.TestCase):

    def test_prt(self):
        parser = create_parser()
        args = parser.parse_args(['--print'])
        #self.failUnless(args.prt)
        self.assertTrue(args.prt)
        # Read the expected print output from file
        rootdir = os.path.abspath(os.path.dirname(__file__))
        f = open(os.path.join(rootdir, 'prt.txt'))
        expected = f.read()
        f.close()
        # Catch the output of --print
        out = StringIO()
        prt(out=out)
        result = out.getvalue()
        self.assertTrue(expected == result)

    def test_case3(self):  # NotImplementedError --case 3
        parser = create_parser()
        with self.assertRaises(SystemExit):
            parser.parse_args(['--case', '3'])
