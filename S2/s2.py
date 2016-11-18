#<leona> ::=
#<movement> ::= forw|backw|left|right
#<pen> ::= down|up
#<color> ::= color

#ta bort kommentarer
#gör allt till uppercase
#skapa tokenClass som lagrar alla tokens

#token = [forw]

#forw 1.




import re
text = re.compile('[a-zA-Z]')

y = "DOWN. GUSTAV ."
word = ""
for x in y:
    if text.match(x):
        word = word + x
    else:
        print(word)
        word =""
        print(x)

