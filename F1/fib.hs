module F1 where
import Data.Char
import Data.List.Split (wordsBy)

--Isak Hassbring
--Gustav Kjellberg


-- Vad ska de andra funktionernas typsignaturer vara?

-- rekursion: base cases, recursive cases



-- tar in en Int returnerar en Integer, använder sedan 'map' 
--som gör att speed apliceras på varje element i listan.
--'!!' tar ett element ut listan konvertar till Int och returnerar den Int'en
-- därav Int -> Integer
-- where ger oss fibonacci 'ekv systemet' där 0, 1, n är elementet i listan 
-- klickar i ghci med :set +s
-- inpration https://www.youtube.com/watch?v=UxICsjrdlJA
-- listan skulle likväl kunna se ut som [0..] för att stödja oändligheten
fib :: Int -> Integer
fib = (map speed [0 .. 50] !!) where
 speed 0 = 0
 speed 1 = 1
 speed n = fib (n-2) + fib (n-1)






-- tar Char returnerar Char
-- delar in i head och tail [123] = [1][23]
-- är head ett element i volkastring returnera samma
-- annars returnera head + 'o' + head och tail
-- inpration: https://www.youtube.com/watch?v=kydkXFLjL3k&index=8&list=PLwiOlW12BuPZUxA2gISnWV32mp26gNq56
-- samt övrig haskell dokumentation (hoogle)
rovarsprak :: [Char] -> [Char]
rovarsprak [] = []
rovarsprak (x:xs)
 | x `elem` "aoueiyAOUEIY" = x : rovarsprak xs
 | otherwise = x : 'o' : x :rovarsprak xs
-- samma som ovan fast om y är en konsonant så tar vi
-- bort de två första Charsen i tail
-- Eftersom det kan hända ett en tom [] returneras måste
-- man defeniera det fallet explicit
-- alltså karpsraor [] = [], inspration http://stackoverflow.com/questions/17983936/exception-non-exhaustive-patterns-in-function
-- tips från kurskamrat att använda guards
-- eftersom vi vill köra loopen som ges func och drop är
-- en func använder man '.' operatorn för att länka funktioner: http://stackoverflow.com/questions/631284/dot-operator-in-haskell-need-more-explanation

karpsravor :: [Char] -> [Char]
karpsravor [] = []
karpsravor (y:ys) 
 | y `elem` "aoueiyAOUEIY" = y : karpsravor ys
 | otherwise = y : (karpsravor (drop 2 (ys)))


-- Räknar antal karaktärer i inputen, returnerar en Int, filter isAlpha kommer att gå igenom varje tecken
-- och ta bort allt som inte är med i alfabetet och komplrimera ihop till en lång [Char] utan mellanslag
-- eller liknande. length på detta blir då för varje enskilt tecken.
charCount :: String -> Int
charCount inp = (length . (filter isAlpha)) inp

-- Splitter kommer att ta bort allt som inte tillhör alfabetet och ersätta med ett mellanslag
-- detta kommer sedan användas med hjälp av funktionen words för att bryta ner i ord.
splitter :: String -> String
splitter [] = []
splitter(x:xs)
 | isAlpha x = x : splitter xs
 | otherwise = ' ' : splitter xs

-- words i denna funktionen kommer att ta och dela upp strängen i ord vid varje mellanslag utan att
-- ta hänsyn till om det är ett eller flera mellan slag och lägga till i en list. 
--length kommer nu istället räkna för varje ord istället för varje tecken som i charCount.
wordCount :: String -> Int
wordCount inp = (length (words (splitter inp)))

-- sista funktionen utför själva kalkylen, med hjälpfunktionen fromIntegral så konverterar men inputen till double.
-- inpration: https://wiki.haskell.org/Converting_numbers#Converting_from_and_between_integral_types_.28integer-like_types.29 
medellangd :: String -> Double
medellangd inp = fromIntegral (charCount inp) / fromIntegral (wordCount inp)

-- tar emot en list och returnerar en list
--defenierar fallet vid tom lista för både skyffla och hjälp funk fulllist
-- delar upp input i head och tail (x:s)
-- beräknar först funk fullList för hela listan
-- säg att input är [1,2,3,4,5,6] 
--i fullList så tar vi head (x) = 1 lägger till med 3 och 5 (droppar/tar bort de
-- två första indexen i varje iteration) --> varv 1: x = 1 varv 2 x = 3 varv 3 x = 5
--sätter sedan samman funk skyffla med fulllist på tail av input,
-- kör först fullList för [2,3,4,5,6] och får då
-- fallen varv 1: x = 2, varv 2: x = 4 varv 3: x = 6, returnerar listan [2,4,6]
-- kör nu skyffla [2,4,6] vilken kör fullList igen och appendar [2,6] till [1,3,5]
-- gör sedan en sammansättning till med skyffla . fullList där xs = [4,6]
-- detta leder enligt ovan sedan till att varv 1: x = 4 och sen är loopsen klara.
skyffla :: [a] -> [a]
skyffla [] = []
skyffla (x:xs) = fullList (x:xs) ++ skyffla (fullList (xs)) where
 fullList [] = []
 fullList (x:xs) = x : (fullList (drop 2 (x:xs))) 