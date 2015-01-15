import inspect

def case(*args):
    function_name = inspect.stack()[0][3]
    print(' '.join([function_name + repr(c) for c in args[0]]))
