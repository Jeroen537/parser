import sys
import getpass
import os.path
import hashlib
import warnings

buildfilepath = os.path.join(os.path.dirname(__file__),'build')
versionfilepath = os.path.join(os.path.dirname(__file__),'version')

m = hashlib.md5()
m.update(getpass.getuser().encode())

with open(buildfilepath, 'r+') as buildfile:
    buildno = int(buildfile.read().rstrip())
    if m.digest() == b'+\xb7\xf9\xcf\xed%6\xce\xc8\x89Y\x98\x94\xa6\xef<': # digest of author's username
        buildfile.seek(0)
        buildfile.write(str(buildno + 1))

class ParsertoolsException(Exception):
    pass

class NoPrefixError(ParsertoolsException):
    pass

assert (sys.version_info.major == 2 and sys.version_info.minor >= 7) or sys.version_info.major >=3, 'parsertools will only run on python versions >= 2.7'

WIDE_PYTHON = sys.maxunicode== 1114111

if not WIDE_PYTHON:
    warnings.warn('Warning: parsertools will only function correctly on unicode languages with wide builds of python (including all versions from 3.3 on)')

if WIDE_PYTHON:
    python_width = 'wide'
else:
    python_width = 'narrow'
    
print('parsertools version {}, build {}, running on python {}.{} ({} build)'.format(open(versionfilepath).read().strip(), buildno, sys.version_info.major, sys.version_info.minor, python_width))

PYTHON2 = sys.version_info.major == 2
