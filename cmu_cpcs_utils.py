import inspect
import sys
import random
import types

from io import StringIO

EPSILON = 10**-7


def almostEqual(x, y, epsilon=EPSILON):
    return abs(x - y) <= epsilon


def rounded(d):
    sign = 1 if (d >= 0) else -1
    d = abs(d)
    n = int(d)
    if (d - n >= 0.5):
        n += 1
    return sign * n


def testFunction(fn):
    return fn


# Capturing print output
tempOut = StringIO()


def startOutputCapture():
    global tempOut
    tempOut = StringIO()
    sys.stdout = tempOut


def stopOutputCapture():
    output = tempOut.getvalue()
    sys.stdout = sys.__stdout__
    return output


# Faking input
fakeInputs = []


def fakeInput(prompt=''):
    if fakeInputs == []:
        raise Exception('input() was called, but there are no more inputs left.')
    response = fakeInputs.pop(0)
    print(f'{prompt}{response}')
    return response


def setInputs(*inputs, callerGlobals=None):
    # Set up the caller globals correctly
    if callerGlobals is None:
        callerGlobals = inspect.stack()[1][0].f_globals
    callerGlobals['input'] = fakeInput

    # Fake the inputs
    global fakeInputs
    if (len(inputs) == 1) and (isinstance(inputs[0], list) or isinstance(inputs[0], tuple)):
        fakeInputs = list(inputs[0])
    else:
        fakeInputs = list(inputs)


# An alias for graphics exercises
setTextInputs = setInputs

# Faking randrange
_randrange = random.randrange
fakeRandranges = []


def fakeRandrange(*args):
    if len(fakeRandranges) > 0:
        expected_args_and_val = fakeRandranges.pop(0)
        expected_args = expected_args_and_val[:-1]
        val = expected_args_and_val[-1]
        if args != expected_args:
            expected_arg_str = ', '.join(map(str, expected_args))
            arg_str = ', '.join(map(str, args))

            raise Exception(f'We expected to see a call to randrange({expected_arg_str}), ' +
                            f'but instead we saw a call to randrange({arg_str})')
        return val
    return _randrange(*args)


def setRandranges(randranges, callerGlobals=None):
    # Set up the caller globals correctly
    if callerGlobals is None:
        callerGlobals = inspect.stack()[1][0].f_globals
    if 'random' in callerGlobals:
        if isinstance(callerGlobals['random'], types.ModuleType):
            callerGlobals['random'].randrange = fakeRandrange
    if 'randrange' in callerGlobals:
        callerGlobals['randrange'] = fakeRandrange

    # Fake the randranges
    global fakeRandranges
    if isinstance(randranges[0], int):
        fakeRandranges = [randranges]
    else:
        fakeRandranges = list(randranges)

    for randrange in randranges:
        if not isinstance(randrange, tuple) or not (2 <= len(randrange) <= 4):
            raise Exception('setRandranges must take in a tuple of tuples with 2 to 4 elements.')

    fakeRandranges = list(randranges)


def makeTestbot(fn):
    callerGlobals = inspect.stack()[1][0].f_globals

    def testbotFn(*args, **kwargs):
        # for now, assume args are for fn, kwargs are for testbot fn
        for key in kwargs:
            if key == 'inputs':
                inputs = kwargs[key]
                if isinstance(inputs, str):
                    # if str, assume comma-separated values
                    inputs = inputs.split(',')
                setInputs(inputs, callerGlobals=callerGlobals)
            elif key == 'randranges':
                randranges = kwargs[key]
                if isinstance(randranges[0], int):
                    randranges = (randranges, )
                setRandranges(randranges, callerGlobals=callerGlobals)
            else:
                raise Exception(f'Unknown testbot keyword argument: {key}')
        startOutputCapture()
        fn(*args)
        return stopOutputCapture()

    return testbotFn


def multilineRepr(s):
    if not isinstance(s, str) or '\n' not in s:
        return repr(s)

    quote = "'"
    if "'" in s and '"' not in s:
        quote = '"'

    result = [quote * 3]

    startIdx = 0
    if s[0] == '\n':
        startIdx = 1
        result.append('\n')
    else:
        result.append('\\')
        result.append('\n')

    for i in range(startIdx, len(s)):
        c = s[i]

        if c == quote or c == '\\':
            result.append('\\')
            result.append(c)
        elif c == '\t':
            result.append('\\')
            result.append('t')
        elif c == '\n':
            result.append('\n')
        elif c == '\r':
            result.append('\\')
            result.append('t')
        elif c < ' ' or c >= '\x7f':
            result.append('\\x')
            result.append('%02x' % ord(c))
        else:
            result.append(c)

    result.append(quote * 3)

    return ''.join(result)


def getColWidths(a):
    colWidths = dict()
    for row in range(len(a)):
        if not (isinstance(a[row], list) or isinstance(a[row], tuple)):
            continue
        for col in range(len(a[row])):
            colWidths[col] = max(colWidths.get(col, 0), len(repr(a[row][col])))
    return colWidths


def nestedListReprAddElem(output, a, row, col, colWidths):
    elem = a[row][col]
    if (col > 0):
        output.append(', ')
    justMethod = 'ljust'
    if isinstance(a[row][col], int) or isinstance(a[row][col], float):
        justMethod = 'rjust'
    output.append(getattr(repr(elem), justMethod)(colWidths[col]))


def is2dList(a):
    if not isinstance(a, list):
        return False
    for elem in a:
        if isinstance(elem, list) or isinstance(elem, tuple):
            return True
    return False


def prettyListRepr(a):
    if (a == []):
        return '[]'
    if not is2dList(a):
        return repr(a)
    output = []
    colWidths = getColWidths(a)
    output.append('[\n')
    for row in range(len(a)):
        if isinstance(a[row], list) or isinstance(a[row], tuple):
            lParen, rParen = '[', ']'
            if isinstance(a[row], tuple):
                lParen, rParen = '(', ')'
            output.append(f' {lParen} ')
            for col in range(len(a[row])):
                nestedListReprAddElem(output, a, row, col, colWidths)
            output.append(f' {rParen}')
        else:
            output.append(' ' + repr(a[row]))
        if (row < len(a) - 1):
            output.append(',')
        output.append('\n')
    output.append(']')
    return ''.join(output)


def prettyStr(o):
    if isinstance(o, str) and '\n' in o:
        return multilineRepr(o)

    if isinstance(o, list):
        return prettyListRepr(o)

    return repr(o)


def prettyPrint(o):
    print(prettyStr(o))


__all__ = [
    'almostEqual', 'testFunction', 'setInputs', 'setTextInputs', 'setRandranges',
    'startOutputCapture', 'stopOutputCapture', 'prettyPrint', 'prettyStr',
    'rounded'
]