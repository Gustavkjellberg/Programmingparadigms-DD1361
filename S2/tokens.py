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
        self.q = LinkedQ()
        self.q.peek()
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
                            self.q.enqueue(Token(word, word))
                        else:
                            self.q.enqueue(Token('INVALID', word))

            elif number.match(x):
                word += word + str(x)
                if i == len(self.inp)-1:
                    if not word is "":
                        print(word)
                        if word in tokens:
                            self.q.enqueue(Token('NUMBER', int(word)))
                        else:
                            self.q.enqueue(Token('INVALID', word))
                #self.q.enqueue(Token('NUMBER', word))



            else:
                if not word is "":
                    if number.match(word):
                        self.q.enqueue(Token('NUMBER', word))
                    elif word in tokens:
                        self.q.enqueue(Token(word, word))
                    else:
                        self.q.enqueue(Token('INVALID', word))

                word = x
                if word == '.':
                    self.q.enqueue(Token('DOT', word))
                elif word == ' ':
                    self.q.enqueue(Token('SPACE', word))
                elif word == '\n':
                    self.q.enqueue(Token('NEWLINE', word))
                elif word == '"':
                    self.q.enqueue(Token('QUOTE', word))
                elif word == ',':
                    self.q.enqueue(Token('COMMA', word))
                elif word == '#':
                    print("ADSHUUDHALW")
                    iHex = i+1
                    while iHex <= i+6:        #DETTA KAN VARA BRUTALFEL!!!!!
                        word += self.inp[iHex]
                        iHex +=1
                    i += 6
                    self.q.enqueue(Token('HEXA', word))
                else:
                    self.q.enqueue(Token('INVALID', word))
                word =""
            i += 1

        #tree = parser(self.q)
        #test = Parser(self.q)
        #test.read()
        return self.q

        #return kö(object(typ,data)......)






class Parser:

    def __init__(self, q):
        self.q = q
        self.line = 1





    def read(self):
        #forw = re.compile('F''O''R''W')
        #back = re.compile('B''A''C''K')
        #left = re.compile('L''E''F''T')
        #right = re.compile('R''I''G''H''T')
        movement = ['FORW', 'BACK', 'LEFT', 'RIGHT']
        pen = ['UP', 'DOWN']
        #space = re.compile('S''P''A''C''E')
        #newLine = re.compile('N''E''W''L''I''N''E')
        #up = re.compile('U''P')
        #down = re.compile('D''O''W''N')
        #color = re.compile('C''O''L''O''R')
        #hexNumber = re.compile('[#]')

        pt = self.q.peek()
        pt = pt.getType()
        #print(pt)
        if pt in movement:
            mvmnt = self.q.dequeue()
            pt = self.q.peek()
            pt = pt.getType()
            print(pt)
            if pt is 'SPACE':
                self.line = self.ws(self.line)           #skall kolla om space/tab eller \n. returnera kö och ev. ny rad
                number = self.digit(self.line)        #Kolla siffror, returnera tal.
                self.line = self.ws(self.line)
                print("HEJ")
                print(self.q.peek())
                self.dot(self.line)                  # Kollar om det är en punkt äter och returnerar kö
                print("DÅ")
                self.line = self.ws(self.line)
                #self.read(self.q)                                      #rekursivt anrop, här skall nod läggas till
            else:
                raise SyntaxError('Fel på rad ' + str(self.line))#om fel raisea fel

        elif pt in pen:
            print('Pen')
            penState = self.q.dequeue()
            self.line = self.ws(self.line)
            self.dot(self.line)
            self.line = self.ws(self.line)
             # rekursivt antop, här skall nod läggas till

        elif pt == 'COLOR':
            print('Color')
            color = self.q.dequeue()
            self.line = self.ws(self.line)
            hex = self.hexCol(self.line)
            self.line = self.ws(self.line)
            self.dot(self.line)
            self.line = self.ws(self.line)
            #här skall node med 'color' hex skapas

        elif pt == 'REP':
            rep = self.q.dequeue()
            self.line = self.ws(self.line)
            number = self.digit(self.line)
            self.line = self.ws(self.line)
            self.line = self.rep(self.line, number.getData())
            self.line = self.ws(self.line)

        elif pt == 'INVALID':
            self.q.dequeue
            self.line = self.ws(self.line)
            if self.q.peek().getData() is '%':
                self.line = self.cmnt(self.line)   #while not \n, eat.
            else:
                raise SyntaxError('Fel på rad ' + str(self.line))


        elif pt == 'NEWLINE':
            self.line +=1
            self.q.dequeue()

        elif pt == 'SPACE':
            self.line = self.ws(self.line)



        else:
            raise SyntaxError('Fel på rad ' + str(self.line))




    def ws(self, line):
        if self.q.peek():
            pt = self.q.peek().getType()
            while pt is 'SPACE':
                self.q.dequeue()
                pt = self.q.peek().getType()
            if pt is 'NEWLINE':
                self.q.dequeue()
                self.line +=1
                print(self.line)
                self.line = self.ws(self.line)
        return self.line

    def cmnt(self, line):
        pt = self.q.peek().getType()
        if self.q.isEmpty():
            return self.line
        if pt is 'NEWLINE':
            self.line += 1
            return self.line
        while not pt is 'NEWLINE':
            pt = self.q.peek().getType()
            if self.q.isEmpty():
                return self.line
            self.q.dequeue()
        self.line += 1
        return self.line

    def rep(self, line, number):
        number = int(number)
        pt = self.q.peek().getType()
        print(pt)
        tempQ = []
        if pt is '"':
            self.q.dequeue()
            while not pt is '"':
                self.line = ws(self.line)    #FIXA SOM UNDER
                tempQ.append(self.q.dequeue())
        else:
            tempQ.append(self.q.dequeue())
            pt = self.q.dequeue().getType()
            if pt == 'SPACE':
                self.line = self.ws(self.line)
                tempQ.append(Token('SPACE', ' '))
            else:
                return False
            tempQ.append(self.q.dequeue())
            self.line = self.ws(self.line)
            tempQ.append(self.q.dequeue())


        tempQ.reverse()
        while number > 0:
            for elem in tempQ:
                if elem:
                    self.q.addFront(elem)
            number -= 1
        i = 0
        while i < 12:
            print(self.q.dequeue().getType()+ "   jejeje")
            i+=1
        return self.line

    def digit(self, line):
        pt = self.q.peek().getType()
        print (pt)
        if pt is 'NUMBER':
            return self.q.dequeue()
        else:
            raise SyntaxError('Fel på rad ' + str(self.line))

    def hexCol(self, line):
        hexSigns = re.compile('[A-F0-9]')
        pt = self.q.peek()
        hexnr = ""
        print(pt.getType())
        if pt.getType() is 'HEXA':
            iHex = 1
            while iHex <= 6:
                if hexSigns.match(pt.getData()[iHex]):
                    iHex +=1
                    pass
                else:
                    raise SyntaxError('Fel på rad' + str(self.line))
            return self.q.dequeue()
        else:
            raise SyntaxError('Fel på rad ' + str(self.line))


    def dot(self, line):
        pt = self.q.peek().getType()
        if pt is 'DOT':
            self.q.dequeue()
            return
        else:
            raise SyntaxError('Fel på rad ' + str(self.line))



























#_______FUNKTIONER_______#

def initializer(input):
    try:
        x = Lexer(input)
        q = x.checkType()
        y = Parser(q)
        i = 0
        while not q.isEmpty():
            i +=1
            print(i)
            tree = y.read()
    except SyntaxError as inst:
        print(inst)



initializer('REP 3 FORW 1.')
#while not self.q.isEmpty():
 #   y = self.q.dequeue()
  #  print (y.getType())
