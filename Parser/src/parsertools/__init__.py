import sys
import getpass
import os.path
import hashlib

buildfilepath = os.path.join(os.path.dirname(__file__),'build')

m = hashlib.md5()
m.update(getpass.getuser().encode())

with open(buildfilepath, 'r+') as buildfile:
    buildno = int(buildfile.read().rstrip())
    if m.digest() == b'+\xb7\xf9\xcf\xed%6\xce\xc8\x89Y\x98\x94\xa6\xef<':
        buildfile.seek(0)
        buildfile.write(str(buildno + 1))
 
__version__ = '0.2.1'


class ParsertoolsException(Exception):
    pass

class NoPrefixError(ParsertoolsException):
    pass

print('parsertools version {}, build {}'.format(__version__, buildno))


if sys.version_info < (3,3):
    raise ParsertoolsException('This parser only works with Python 3.3 or later (due to unicode handling and other issues)')