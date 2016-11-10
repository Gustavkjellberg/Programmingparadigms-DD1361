/*Fibonacci,   Gustav Kjellberg, Isak Hassbring*/

fib(0,0).
fib(N,F) :- N>0, fib(N, F, _). 

fib(1,1,0).
fib(N, F1, F2):- /*Index, fibValueAt(Index), fibValueAt(Index-1), example, index 7 -> F2=8 and F1 = 13*/ 
    N>1,
    N1 is N-1,
    fib(N1, F2, F3),
    F1 is F2 + F3.    

/*vowel(Char,Index) :- nth0(Index, "aouåeiyäöAOUÅEIYÅÖ", Char). Funkar inte pga ej ascii?*/


vowel(65).
vowel(69).
vowel(73).
vowel(79).
vowel(85).
vowel(89).
vowel(97). 
vowel(101). 
vowel(105). 
vowel(111). 
vowel(117). 
vowel(121). 

/*om vokal fortsätt rekursivt, om inte, forsätt rekursivt med lägg till 111, head*/
rovarsprak([], []).
rovarsprak([Head|Tail], [Head|Result]) :-  
    vowel(Head), rovarsprak(Tail, Result),!.
rovarsprak([Head|Tail], [Head,111, Head|Result]) :-
    rovarsprak(Tail, Result), !.


/*vi skall kolla om tecknet är en bokstav(görs med alpha) vi skall då kolla om nästa tecken är*/
/*en icke-bokstav då är det nytt ord och vi skall lägga till 1 på både word och char*/
/*Behöver fallet då första och andra är chars och då görs endast word +1 */

/*Beöhver basfall då texten är en tom lista och returna nera 0,0*/
/*Behöver basfall där första är något annat än bokstav då fortsätter vi reukrivt med tail*/

/*sedan behöver vi funktion som räknar ut medellängd*/

/*basfall för den tomma listan*/ 

charsAndWords([],0,0).
/*Basfall då vi endast har en bokstav*/
charsAndWords([Fst|[]],1,1) :-
    code_type(Fst, alpha),!.

charsAndWords([_],0,0).




/*funktion för att kolla om flrsta och andra är chars*/ 
charsAndWords([Fst,Scnd|Tail],Char, Word):- 
    not(code_type(Scnd,alpha)),
    code_type(Fst, alpha),
    charsAndWords(Tail, Char1, Word1),
    Char is Char1 + 1, Word is Word1 + 1,!.

/*kollar om första elementet är av char, isf så lägger den till +1 till char*/
charsAndWords([Fst|Tail], Char, Word):-
    code_type(Fst, alpha),
    charsAndWords(Tail, Char1, Word),
    Char is Char1 + 1,!.

/*om första inte är char*/
charsAndWords([_|Tail], Char, Word):-
    charsAndWords(Tail, Char, Word),!.

/*räknar ut medellangd*/
medellangd([],AvgLen):- AvgLen is 0.0.
medellangd(Text, AvgLen):-
    charsAndWords(Text, Char, Word),
    AvgLen is Char/Word.


/*delar upp input i head och tail, lagras i en ny lista*/
/*hjälpfunktion med head och tail, lagrar resultatet i ny lista, resultatet är vart annat element*/
/*hjälpfunktionen med endast tail och lagrar i en annan lista, då får man vart annat element fr.o.m elem 2*/
/*anropar huvudfunk rekursivt med senaste listan för att göra amma sak på den och lagrar detta i en sista lista*/
/*appendar listan från första skyfflingen med listan från andra huvudfunktionsanropen och lägger i listan för huvud funk*/
/*Glöm ej basfall, då inp är tom är resultatet tomt och är det ett element så är det resultatet*/


skyffla([Head|Tail], Skyfflad):-
    everyOtherElem([Head|Tail], FirstList),
    everyOtherElem(Tail, ListForIteration),!,
    skyffla(ListForIteration, Skyfflad1),
    append(FirstList, Skyfflad1, Skyfflad).
skyffla([],[]).

everyOtherElem([First,_|Tail1], [First|Result]):-
    everyOtherElem(Tail1,Result),!.


everyOtherElem([],[]).
everyOtherElem([A|[]],[A]).





