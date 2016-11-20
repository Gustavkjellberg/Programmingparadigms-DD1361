#_______imports_______#
from linkedQ9 import *
import re


#_______DEFINITIONER_______#
#EOF, FORW, BACK, LEFT, RIGHT, UP, DOWN, REP, SPACE, QUOTE, COLOR, NUMBER, DOT, COMMA, INVALID = 'EOF', 'FORW', 'BACK', 'LEFT', 'RIGHT', 'UP', 'DOWN', 'REP', 'SPACE', 'QUOTE', 'COLOR', 'NUMBER', 'DOT', 'COMMA', 'INVALID'


#_______CLASSER_______#
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

            elif number.match(x):
                word += word + str(x)
                if i == len(self.inp)-1:
                    if not word is "":
                        if word in tokens:
                            q.enqueue(Token('NUMBER', int(word)))
                        else:
                            q.enqueue(Token('INVALID', word))
                #q.enqueue(Token('NUMBER', word))



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
                    q.enqueue(Token('NEWLINE', word))
                elif word == '"':
                    q.enqueue(Token('QUOTE', word))
                elif word == ',':
                    q.enqueue(Token('COMMA', word))
                elif word == '#':
                    iHex = 1
                    while iHex <= 7:        #DETTA KAN VARA BRUTALFEL!!!!!
                        word += self.inp[iHex]
                    i += 6
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





    def read(self):
        line = 0
        #forw = re.compile('F''O''R''W')
        #back = re.compile('B''A''C''K')
        #left = re.compile('L''E''F''T')
        #right = re.compile('R''I''G''H''T')
        movement = ['FORW', 'BACKW', 'LEFT', 'RIGHT']
        pen = ['UP', 'DOWN']
        #space = re.compile('S''P''A''C''E')
        #newLine = re.compile('N''E''W''L''I''N''E')
        #up = re.compile('U''P')
        #down = re.compile('D''O''W''N')
        #color = re.compile('C''O''L''O''R')
        #hexNumber = re.compile('[#]')


        pt = self.q.peek()
        pt = pt.getType()
        if pt in movement:
            print("rörelse")
            mvmnt = self.q.dequeue()
            pt = self.q.peek()
            pt = pt.getType()
            print(pt)
            if pt is 'SPACE':
                line = ws(line)             #skall kolla om space/tab eller \n. returnera kö och ev. ny rad
                number = digit(line)        #Kolla siffror, returnera tal.
                line = ws(line)
                dot(line)                  # Kollar om det är en punkt äter och returnerar kö
                line = ws(line)
                read()                                      #rekursivt anrop, här skall nod läggas till
            else:
                raise SyntaxError('Fel på rad ' + str(line))#om fel raisea fel

        elif pt in pen:
            print('Pen')
            penState = self.q.dequeue()
            line = ws(line)
            dot(line)
            line = ws(line)
            read() # rekursivt antop, här skall nod läggas till

        elif pt is 'COLOR':
            print('Color')
            color = self.q.dequeue()
            line = ws(line)
            hex = hexCol(line)
            line = ws(line)
            dot(line)
            line = ws(line)
            #här skall node med 'color' hex skapas
            read()

        elif pt is 'REP':
            rep = q.dequeue()
            line = ws(line)
            number = digit(line)
            line = ws(line)
            line = rep(line, number.getData())
            line = ws(line)
            read()

        elif pt == 'INVALID':
            q.dequeue
            line = ws(line)
            if self.q.peek() is '%':
                line = cmnt(line)   #while not \n, eat.
                read()
            else:
                raise SyntaxError('Fel på rad' + str(line))


        elif pt is 'NEWLINE':
            line +=1
            self.q.dequeue()
            read()

        elif pt is 'SPACE':
            line = ws(line)
            read()



        else:
            raise SyntaxError('Du gjorde något sjukt fel')




    def ws(self, line):
        pt = self.q.peek().getToken
        if pt is 'SPACE':
            q.dequeue
        if pt is 'NEWLINE':
            line +=1
            line = ws(line)
        return line

    def cmnt(self, line):
        pt = self.q.peek().getToken
        if self.q.isEmpty()
            return line
        if pt is 'NEWLINE':
            return line += 1

        while not pt is 'NEWLINE':
            self.q.dequeue()
        return cmnt(line)

    def rep(self, line, number):

        pt = self.q.peek().getToken

        if pt is '"':
            q.dequeue()
            dq = []
            while not pt is '"':
                line = ws(line)
                dq.append(q.dequeue())
        else:
            dq.append(q.dequeue())
            line = ws(line)
            dq.append(q.dequeue())
            line = ws(line)
            dq.append(q.dequeue())
        dq.reverse()

        while number > 0:
            for elem in dq:
                q.addFront(elem)
            number -= 1
        return line

    def digit(self, line):
        pt = self.q.peek().getToken
        if pt is 'NUMBER':
            return q.dequeue()
        else:
            raise SyntaxError('Fel på rad' + str(line))

    def hexCol(self, line):
        hexSigns = re.compile('[A-F0-9]')
        pt = self.q.peek()

        hexnr = ""
        if pt.getType() is 'HEXA':
            iHex = 1
            while iHex <= 7:
                if hexSigns.match(pt.getData()[iHex]):
                    pass
                else:
                    raise SyntaxError('Fel på rad' + str(line))
            return q.dequeue()
        else:
            raise SyntaxError('Fel på rad' + str(line))



























#_______FUNKTIONER_______#

def initializer(input):
    try:
        x = Lexer(input)
        q = x.checkType()
        y = Parser(q)
        tree = y.read()
    except SyntaxError as inst:
        print(inst)



initializer('FORW 1. Down 3. Up. Down. Rep 5 " ')
#while not q.isEmpty():
 #   y = q.dequeue()
  #  print (y.getType())
