# coding: utf-8
########################################################################
# Mall för labb S1, DD1361 Programmeringsparadigm.
# Författare: Per Austrin
########################################################################

########################################################################
# Dessa funktioner är det som ska skrivas för att lösa de olika
# uppgifterna i labblydelsen.
########################################################################
#Gustav Kjellberg 951028-2578
#Isak Hassbring 940204-1496
import re


def dna():          # uppgift 1
    return '^[ACGT]+$'

def sorted():       # uppgift 2
    return '^[9]*[8]*[7]*[6]*[5]*[4]*[3]*[2]*[1]*[0]*$'

def hidden1(x):     # uppgift 3
    # indata x är strängen som vi vill konstruera ett regex för att söka efter
    return x

def hidden2(x):     # uppgift 4
    # indata x är strängen som vi vill konstruera ett regex för att söka efter

    y = ".*"
    for letter in x:
        y = y + letter + ".*"
    return y
#Ja mha {n} ist för *
def equation():     # uppgift 5
    #Vi får ta +/- digit räknesätt/= digit räknesätt/=

    return '^[\+\-]?\d+([\+\-\*\/]\d+)*([\=]([\+\-]?\d+))?([\+\-\*\/]\d+)*$'

def parentheses():  # uppgift 6
#('^\([\([\([\([\(\)]?\)]?\)]?\)]?\)]?$')
    #Vi menar att det går då vi för varje operator kan bestämma hur nästkommande tecken får se ut.
    return '^(\((\((\((\((\(\))*\))*\))*\))*\))*$'

def sorted3():      # uppgift 7
#Då vi inte känner till någon existerande jämförelseparameter i regex vill vi påstå att detta ej går.
    return '^\d*([0]1[2-9]|[0-1]2[3-9]|[0-2]3[4-9]|[0-3]4[5-9]|[0-4]5[6-9]|[0-5]6[7-9]|[0-6]7[8-9]|[0-7]8[9])\d*$'


########################################################################
# Raderna nedan är lite testkod som du kan använda för att provköra
# dina regexar.  Koden definierar en main-metod som läser rader från
# standard input och kollar vilka av de olika regexarna som matchar
# indata-raden.  För de två hidden-uppgifterna används söksträngen
# x="test" (kan lätt ändras nedan).  Du behöver inte sätta dig in i hur
# koden nedan fungerar om du inte känner för det.
#
# För att provköra från terminal, kör:
# $ python s1.py
# Skriv in teststrängar:
# [skriv något roligt]
# ...
########################################################################
from sys import stdin
import re

def main():
    def hidden1_test(): return hidden1('test')
    def hidden2_test(): return hidden2('test')
    tasks = [dna, sorted, hidden1_test, hidden2_test, equation, parentheses, sorted3]
    print('Skriv in teststrängar:')
    while True:
        line = stdin.readline().rstrip('\r\n')
        if line == '': break
        for task in tasks:
            result = '' if re.search(task(), line) else 'INTE '
            print('%s(): "%s" matchar %suttrycket "%s"' % (task.__name__, line, result, task()))


if __name__ == '__main__': main()