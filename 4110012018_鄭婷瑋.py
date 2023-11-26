# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 13:13:02 2023

@author: ASUS
"""

import re

class SimpleLexer(object):
    def __init__(self):
        self.token_rules = [
            ('NUMBER', r'\d+'),
            ('PLUS', r'\+'),
            ('MINUS', r'-'),
            ('MUTIPLY', r'\*'),
            ('DIVIDE', r'/'),
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('WS', r'\s+'),
        ]
        self.token_regex = '|'.join('(?P<%s>%s)' % pair for pair in self.token_rules)
        self.re_token_regex = re.compile(self.token_regex)
        
    def tokenize(self, code):
        for mo in self.re_token_regex.finditer(code):
            kind = mo.lastgroup
            value = mo. group()
            if kind == 'NUMBER':
                value = int(value)
            elif kind == 'WS':
                continue
            yield kind, value
            
code = '27+(43/36-48)*51'
lexer = SimpleLexer()
tokens = list(lexer.tokenize(code))
    
print(tokens)