

/*Gustav Kjellberg, Isak Hassbring*/

spider(S):-
  person(S),
  checkIfSpider(S).


/*Checks  who might be the spider*/
checkIfSpider(S):-
  setof(Y, relation(S,Y), PplWithRel), /*Creates a nonrepeatative list of persons with relation to S*/
  setof(P, person(P), AllPpl), /*Creates a nonreaptative list with all existing persons*/
  subtract(AllPpl, [S|PplWithRel], DoesntKnowSpider),  
  allRelations(DoesntKnowSpider, PplWithRel),!. /*checks so that all relations that shall exist exists.*/

/*checks for relation*/
relation(S, Y):- knows(S, Y); knows(Y, S).

allRelations([],_).
allRelations(_,[]).

/*sorts out all the rules of relationship given in the lab-specification.*/
allRelations([P|Tail], PplWithRel):-
  possibleCons([P|Tail], PplWithRel, [], Consp), /*Calls predicate possibleCons with PplWithRel-list containing everyone that knows the spider and returns a list of conspirators.*/  
  testFunk([P|Tail], PplWithRel, Consp),
  setof(X,knowsInList(X, Consp), ConspFriend), /*Checks that NewTail is a empty list*/
  subtract([P|Tail],ConspFriend, NewTail),
  isListEmpty(NewTail),!.

/*If the list NewTail is anything other than empty, then return false.*/
isListEmpty([]).







/*If P doesn't have a relation to an other possibleCon then add to Con list*/
possibleCons(DoesntKnowSpider,[P|Tail], K, Consp):-
  not(knowsInList(P,K)),
  possibleCons(DoesntKnowSpider, Tail,[P|K], Consp). /*continue for every possible con*/
/*else if relation exists don't add to con list.*/
possibleCons(DoesntKnowSpider,[P|Tail], K, Consp):-
  possibleCons(DoesntKnowSpider, Tail, K, Consp).
/*Basfall*/
possibleCons(_,[], K, K).


testFunk([X|Xs], K, P):-
  knowsInList(X, K); knowsInList(X, P),
  testFunk(Xs, K, P).




  /*testFunk(Xs, K, P).*/

testFunk([],_,_).

knowsInList(P, List):- member(R, List),relation(P,R).
/*if there's no relation but the person itself is a member in list, return List*/
knowsInList(P, List):- member(P, List).
/*if P has a relation to anyone in the List, return True*/