,
  allRelations(Tail, [S|PplWithRel], Consp)

  knowsInList(P, [S|PplWithRel]),!

  allRelations(NonConsp, [S|AllConsp], []),

  subtract(AllPpl, [S|AllConsp], NonConsp),




  friendsOf([Head|Tail],Lst, ConspFriend):-
  knowsInList(X, Head),
  subtract(),
  friendsOf(Tail, [Head|Lst], ConspFriend).

friendsOf([],Lst, Lst).



/*If P doesn't have a relation to an other possibleCon then add to Con list*/
possibleCons(DoesntKnowSpider, [P|Tail], K, Consp):-
  not(knowsInList(P,K)),
  testFunk(DoesntKnowSpider, K, [P|Tail]),
  possibleCons(DoesntKnowSpider, Tail,[P|K], Consp). /*continue for every possible con*/
/*else if relation exists don't add to con list.*/
possibleCons(DoesntKnowSpider, [P|Tail], K, Consp):-
  testFunk(DoesntKnowSpider, K, [P|Tail]),
  possibleCons(Tail, K, Consp).
/*Basfall*/
possibleCons(_,[], K, K).


allRelations(DoesntKnowSpider, PplWithRel):-  
  possibleCons(DoesntKnowSpider, PplWithRel, [], Consp), /*Calls predicate possibleCons with PplWithRel-list containing everyone that knows the spider and returns a list of conspirators.*/  
  testFunk(DoesntKnowSpider, Consp, PplWithRel),
  setof(X,knowsInList(X, Consp), ConspFriend), /*Creates a nonrepetative list of persons that has a relation to any of the conspirators*/
  subtract(DoesntKnowSpider,ConspFriend, NoRelationPpl), /*Removes all the persons who knows a conspirator, and the rules from the lab-specification says that this list should be empty.*/
  isListEmpty(NoRelationPpl),!. /*Checks that NewTail is a empty list*/






  /*Gustav Kjellberg, Isak Hassbring*/

spider(S):-
  person(S),
  checkIfSpider(S).


/*Checks  who might be the spider*/
checkIfSpider(S):-
  setof(Y, relation(S,Y), PplWithRel), /*Creates a nonrepeatative list of persons with relation to S*/
  setof(P, person(P), AllPpl), /*Creates a nonreaptative list with all existing persons*/
  subtract(AllPpl, PplWithRel, DoesntKnowSpider),  
  allRelations(DoesntKnowSpider, PplWithRel),!. /*checks so that all relations that shall exist exists.*/
                       /*felet från kattis sa att en spider returnerades som ej var det*/
 /*dessa två rader tar bort eventuella spiders som inte har någon relation alls.*/

/*checks for relation*/
relation(S, Y):- knows(S, Y); knows(Y, S).

allRelations([],_,_).
allRelations(_,[],_).

/*sorts out all the rules of relationship given in the lab-specification.*/
allRelations(DoesntKnowSpider, PplWithRel):-  
  possibleCons(DoesntKnowSpider, PplWithRel, [], Consp), /*Calls predicate possibleCons with PplWithRel-list containing everyone that knows the spider and returns a list of conspirators.*/  
  setof(X,knowsInList(X, Consp), ConspFriend), /*Creates a nonrepetative list of persons that has a relation to any of the conspirators*/
  subtract(DoesntKnowSpider,ConspFriend, NoRelationPpl), /*Removes all the persons who knows a conspirator, and the rules from the lab-specification says that this list should be empty.*/
  isListEmpty(NoRelationPpl),!. /*Checks that NewTail is a empty list*/


/*If the list NewTail is anything other than empty, then return false.*/
isListEmpty([]).







/*If P doesn't have a relation to an other possibleCon then add to Con list*/
possibleCons(DoesntKnowSpider, [P|Tail], K, Consp):-
  not(knowsInList(P,K)),
  testFunk(DoesntKnowSpider, K, [P|Tail]),
  possibleCons(DoesntKnowSpider, Tail,[P|K], Consp). /*continue for every possible con*/
/*else if relation exists don't add to con list.*/
possibleCons(DoesntKnowSpider, [P|Tail], K, Consp):-
  testFunk(DoesntKnowSpider, K, [P|Tail]),
  possibleCons(DoesntKnowSpider, Tail, K, Consp).
/*Basfall*/
possibleCons(_,[], K, K).


testFunk([X|Xs], K, P):-
  knowsInList(X, P); knowsInList(X, K),
  testFunk(Xs, K, P).

testFunk([],_,_).

knowsInList(P, List):- member(R, List),relation(P,R).
/*if there's no relation but the person itself is a member in list, return List*/
knowsInList(P, List):- member(P, List).
/*if P has a relation to anyone in the List, return True*/





/*sorts out all the rules of relationship given in the lab-specification.*/
allRelations(DoesntKnowSpider, PplWithRel):-  
  possibleCons(PplWithRel, [], Consp), /*Calls predicate possibleCons with PplWithRel-list containing everyone that knows the spider and returns a list of conspirators.*/  
  testFunk(DoesntKnowSpider, Consp, PplWithRel),
  setof(X,knowsInList(X, Consp), ConspFriend), /*Creates a nonrepetative list of persons that has a relation to any of the conspirators*/
  subtract(DoesntKnowSpider,ConspFriend, NoRelationPpl), /*Removes all the persons who knows a conspirator, and the rules from the lab-specification says that this list should be empty.*/
  isListEmpty(NoRelationPpl),!. /*Checks that NewTail is a empty list*/