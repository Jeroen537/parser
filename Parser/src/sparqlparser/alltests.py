'''
Created on 11 mrt. 2016

@author: jeroenbruijning
'''

from subprocess import *
import os

os.chdir('../reftest/fed')
print('Running fed test/n')
print(check_output(['/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4', 'testCases.py']).decode('utf-8'))
os.chdir('../query')
print('\nRunning query test\n')
print(check_output(['/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4', 'testCases.py']).decode('utf-8'))
os.chdir('../update1')
print('\nRunning update1 test\n')
print(check_output(['/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4', 'testCases.py']).decode('utf-8'))
os.chdir('../query')
print('\nRunning update2 test\n')
print(check_output(['/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4', 'testCases.py']).decode('utf-8'))
os.chdir('../../sparqlparser')
print('\nRunning grammar test\n')
print(check_output(['/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4', 'grammar.py']).decode('utf-8'))
print('\nRunning func_test test\n')
print(check_output(['/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4', 'func_test.py']).decode('utf-8'))
print('\nRunning grammar_functest test\n')
print(check_output(['/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4', 'grammar_functest.py']).decode('utf-8'))
print('\nRunning grammar_unittest test\n')
print(check_output(['/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4', 'grammar_unittest.py']).decode('utf-8'))
