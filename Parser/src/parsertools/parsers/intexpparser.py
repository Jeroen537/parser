'''
Created on 11 aug. 2016

@author: jeroenbruijning
'''
'''
Created on 28 mrt. 2016

@author: jeroenbruijning
'''
from pyparsing import *
from parsertools.base import ParseStruct, parseStructFunc, separatedList
from parsertools import ParsertoolsException

# Custom exception. This is optional. When present, it can be used in methods of the Parser class as defined below.

class IntExpException(ParsertoolsException):
    '''Custom exception. This is optional. When present, it can be used in methods of a ParseStruct subclass if
    defined below.'''
    
    pass

#
# Define the IntExp class
#

class IntExp(ParseStruct):
    '''Optional subclass of ParseStruct for the language. Typically, this class contains attributes and methods for the language that
    go beyond context free parsing, such as pre- and post processing, checking for conditions not covered by the grammar, etc.'''
    
    pass
#
# The following is boilerplate code, to be included in every Parsertools parser definition module
#

class Parser:
    '''Class to be instantiated to contain a parser for the language being implemented.
    This code must be present in the parser definition file for the language.
    Optionally, it takes a class argument if the language demands functionality in its
    ParseStruct elements that goes beyond what is provided in base.py. The argument must be
    a subclass of ParseStruct. The default is to instantiate the parser as a ParseStruct 
    parser.'''
    
    def __init__(self, class_=ParseStruct):
        self.class_ = class_

    def addElement(self, pattern, newclass=None):
        if newclass:
            assert issubclass(newclass, self.class_)
        else:
            newclass = self.class_ 
        setattr(self, pattern.name, type(pattern.name, (newclass,), {'_pattern': pattern}))
        pattern.setParseAction(parseStructFunc(getattr(self, pattern.name)))
#
# Create the custom Parser object, optionally with a custom ParseStruct subclass
#

IntExpParser = Parser(IntExp)

# Brackets and interpuction

LPAR = Literal('(').setName('LPAR')
IntExpParser.addElement(LPAR)
 
RPAR = Literal(')').setName('RPAR')
IntExpParser.addElement(RPAR)

# Operators

PLUS = Literal('+').setName('PLUS')
IntExpParser.addElement(PLUS)

# Terminals

INTEGER_e = r'[0-9]+'
INTEGER = Group(Regex(INTEGER_e)).setName('INTEGER')
IntExpParser.addElement(INTEGER)
IntExpParser.INTEGER.compute = lambda x: int(str(x))

# Non-terminals

BaseExpression = Group(INTEGER).setName('BaseExpression')
IntExpParser.addElement(BaseExpression)
IntExpParser.BaseExpression.compute = lambda x: x.getItems()[0].compute()

Expression = Forward().setName('Expression')
IntExpParser.addElement(Expression)

AdditiveExpression = Group(separatedList(Expression, sep=IntExpParser.PLUS)).setName('AdditiveExpression')
IntExpParser.addElement(AdditiveExpression)
IntExpParser.AdditiveExpression.compute = lambda x: sum([item.compute() for item in x.getItems() if isinstance(item, IntExpParser.BaseExpression)])

BracketedExpression = Group(LPAR + Expression + RPAR).setName('BracketedExpression')
IntExpParser.addElement(BracketedExpression)
IntExpParser.BracketedExpression.compute = lambda x: x.getItems()[1].compute()

Expression << Group(BaseExpression| AdditiveExpression | BracketedExpression)
IntExpParser.Expression.compute = lambda x: x.getItems()[0].compute()

if __name__ == '__main__':
#     s = '123 + 456 + 789'
#     r = IntExpParser.Expression(s)
#     
#     s = '1234'
#     r = IntExpParser.INTEGER(s)
#     print(r.compute())
#     
#     s = '12345'
#     r = IntExpParser.BaseExpression(s)
#     print(r.compute())

    s = '123 + 456'
    r = IntExpParser.AdditiveExpression(s)
#     print(r.dump())
    print(r.compute())

    s = '123 + 456 + 789'
    r = IntExpParser.AdditiveExpression(s)
#     print(r.dump())
    print(r.compute())
    
    s = '(123 + 456)'
    r = IntExpParser.BracketedExpression(s)
    print(r.dump())
    print(r.compute())
    
#     s = '123 + 456 + 789'
#     r = IntExpParser.Expression(s)
#     print(r.dump())
#     print(r.compute())

