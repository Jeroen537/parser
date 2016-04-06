'''
Created on 4 dec. 2015

@author: jeroenbruijning
'''
import pyparsing
from pyparsing import *


# lines = OneOrMore(SkipTo(lineEnd, include=True))

# print(lines.parseFile('sparqlgrammar', parseAll=True))

if __name__ == '__main__':
    
    # line starts, anything follows until EOL, fails on blank lines,
    line = lineStart + SkipTo(lineEnd, failOn=lineStart + lineEnd) + lineEnd

    lines = OneOrMore(line)
    
    rule_number = '['+ Word(nums) + ']'
    
    numberedline = Group(FollowedBy(rule_number) + line)
    unnumberedline = Group(NotAny(rule_number) + line)

    rule = Group(numberedline + ZeroOrMore(unnumberedline))
    
    rules = ZeroOrMore(rule)
    
    result = rules.parseFile('../resources/sparqlgrammar')

    print('%d rules:\n' % (len(result)))
    
    for r in reversed(result):
        for t in r:
            print('# ', end='')
            if t[0][0] != '[':
                print('\t\t\t', end='')
            print(' '.join(t))

    