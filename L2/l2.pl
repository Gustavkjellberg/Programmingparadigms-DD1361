/*Gustav Kjellberg, Isak Hassbring*/

spider(S):-
  person(S),
  checkIfSpider(S).

/*Kattis hittar en icke spider som spider?*/
/*Om ett S skickas in nu som helt saknar en relations till någon så kommer den att returneras som True..*/
/*alla icke-konspiratorer eller icke-spindlar måste ha en relationen bland konspiratörerna, detta kommer att fixa problemet*/

/*Checks  who might be the spider*/
checkIfSpider(S):-
  setof(Y, relation(S,Y), PplWithRel), /*Creates a nonrepeatative list of persons with relation to S*/
  setof(P, person(P), AllPpl), /*Creates a nonreaptative list with all existing persons*/
   /*checks so that all relations that shall exist exists.*/
  possibleCons(AllPpl, PplWithRel,[], Consp),
  subtract(AllPpl, [S|Consp], Tail),
  allRelations(Tail, Consp),!.

isEmpty([]).

/*checks for relation*/
relation(S, Y):- knows(S, Y); knows(Y, S).

allRelations([P|Tail], PplWithRel):-
  knowsInList(P, PplWithRel),
  allRelations(Tail, PplWithRel).
allRelations([],_).


/*If not relation to other possibleCon add to Con list*/
possibleCons(AllPpl, [P|Tail], K, Consp):-
  not(knowsInList(P,K)),
  subtract(AllPpl, [P|Tail], Lst1), subtract(Lst1, K, Lst2),
  testFunk(Lst2, [P|Tail], K),
  possibleCons(AllPpl, Tail, [P|K], Consp).

/*else if relation exists don't add to con list.*/
possibleCons(AllPpl,[P|Tail], K, Consp):-
  subtract(AllPpl, [P|Tail], Lst1), subtract(Lst1, K, Lst2),
  testFunk(Lst2, [P|Tail], K),
  possibleCons(AllPpl, Tail, K, Consp).
/*Basfall*/
possibleCons(_,[], K, K).

testFunk([Head|Tail], Possible, Absolute):-
  knowsInList(Head, Possible); knowsInList(Head, Absolute),
  testFunk(Tail, Possible, Absolute).
testFunk([], _, _).




/*if P has a relation to anyone in the List, return True*/
knowsInList(P, List):- member(R, List), relation(P,R).
/*if there's no relation but the person itself is a member in list, return True*/
knowsInList(P, List):- member(P, List).
knowsInList([],[]).