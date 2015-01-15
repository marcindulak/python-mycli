import sys

import inspect

def run(out=sys.stdout):
    out.write(inspect.stack()[0][3] + '\n')
