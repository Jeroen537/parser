
'''
Created on 11 mrt. 2016

@author: jeroenbruijning
'''

from subprocess import *
import parsertools
import os
from parsertools import buildfilepath, versionfilepath, PYTHON_VERSION

python = '/Users/jeroenbruijning/anaconda/bin/python3.5'
python = '/opt/local/bin/python2'

print('Running SPARQLParser tests')
os.chdir('sparqlparser/reftest/fed')
print('Running fed test/n')
print(check_output([python, 'testCases.py']).decode('utf-8'))
os.chdir('../query')
print('\nRunning query test\n')
print(check_output([python, 'testCases.py']).decode('utf-8'))
os.chdir('../update1')
print('\nRunning update1 test\n')
print(check_output([python, 'testCases.py']).decode('utf-8'))
os.chdir('../update2')
print('\nRunning update2 test\n')
print(check_output([python, 'testCases.py']).decode('utf-8'))
os.chdir('../..')
print('\nRunning grammar_functest test\n')
print(check_output([python, 'grammar_functest.py']).decode('utf-8'))
print('\nRunning func_unittest test\n')
print(check_output([python, 'func_unittest.py']).decode('utf-8'))
print('\nRunning grammar_unittest test\n')
print(check_output([python, 'grammar_unittest.py']).decode('utf-8'))
# print('Running N3Parser tests')
# os.chdir('../n3parser')
# print('\nRunning grammar_unittest test\n')
# print(check_output([python, 'grammar_unittest.py']).decode('utf-8'))
print('\nAll tests finished (Version {}, Build {})'.format(open(versionfilepath).read().strip(), open(buildfilepath).read().strip()))
