from linkedQ9 import *
import re

EOF, FORW, BACK, LEFT, RIGHT, UP, DOWN, REP, SPACE, QUOTE, COLOR, NUMBER, DOT, COMMA, INVALID = 'EOF', 'FORW', 'BACK', 'LEFT', 'RIGHT', 'UP', 'DOWN', 'REP', 'SPACE', 'QUOTE', 'COLOR', 'NUMBER', 'DOT', 'COMMA', 'INVALID'


#Class to define tokens
class Token:
    def __init__(self, type, data):
        self.type = type
        self.data = data

    def getType(self):
        return self.type

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def setType(self, type):
        self.type = type


    def __str__(self):
        return self.type, self.data
class Lexer:
    def __init__(self, inp):
        self.inp = inp
        self.position = 0
        #Starting with nothing
        self.current_token = None



    def checkType(self):
        tokens = ['FORW', 'BACK', 'LEFT', 'RIGHT', 'UP','HEXA', 'DOWN', 'REP', 'WHITESPACE', 'SPACE' 'QUOTE', 'COLOR', 'NUMBER', 'DOT', 'COMMA', 'INVALID']
        text = re.compile('[a-zA-Z]')
        number = re.compile('[0-9]')
        q = LinkedQ()
        self.inp = self.inp.upper()
        word = ""
        i = 0
        while i <= len(self.inp)-1:
            x = self.inp[i]
            if text.match(x):
                word = word + x
                if i == len(self.inp)-1:
                    if not word is "":
                        if word in tokens:
                            q.enqueue(Token(word, word))
                        else:
                            q.enqueue(Token('INVALID', word))

            else:
                if not word is "":
                    if word in tokens:
                        q.enqueue(Token(word, word))
                    else:
                        q.enqueue(Token('INVALID', word))
                word = x
                if word == '.':
                    q.enqueue(Token('DOT', word))
                elif word == ' ':
                    q.enqueue(Token('SPACE', word))
                elif word == '\n':
                    q.enqueue(Token('WHITESPACE', word))
                elif word == '"':
                    q.enqueue(Token('QUOTE', word))
                elif number.match(word):
                    q.enqueue(Token(NUMBER, word))
                elif word == ',':
                    q.enqueue(Token('COMMA', word))
                elif word == '#':
                    q.enqueue(Token('HEXA', word))
                else:
                    q.enqueue(Token('INVALID', word))
                word =""
            i += 1

        #tree = parser(q)
        #test = Parser(q)
        #test.read()
        return q

        #return kö(object(typ,data)......)






class Parser:
    def __init__(self, q):
        self.q = q

    forw = re.compile('F''O''R''W')
    back = re.compile('B''A''C''K')
    left = re.compile('L''E''F''T')
    right = re.compile('R''I''G''H''T')
    peekToken = q.peek().getType()


    def read(self):
        if forw.match(peekToken):
            print("hej")











x = Lexer('FORW 1. Down 3. Up. Down. Rep 5 " ')
q = x.checkType()
y = Parser(q)
y.read()

while not q.isEmpty():
    y = q.dequeue()
    print (y.getType())
