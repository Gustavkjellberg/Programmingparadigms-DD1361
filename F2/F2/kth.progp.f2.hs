module F2 where
--{-# LANGUAGE OverloadedStrings #-}
import Data.List
--Gustav Kjellberg, 951028-2578
--Isak HassBring, 940204-1496

--2
-- skapar två datatyper, MolSeq och Type
data MolSeq = MolSeq {namn :: String, sekv :: String, whatType :: Type } 
data Type = DNA | Protein deriving (Eq, Enum)

--Konverterar två string till en MolSeq
string2seq :: String -> String -> MolSeq
string2seq namn sekv = MolSeq namn sekv (checkType (sekv))
--Kollar vilten Type MolSeq är
checkType :: String -> Type
checkType sekv = if length (filter (`notElem` "ACGT") sekv) /= 0 then Protein else DNA
--Plockar ut namnet från MolSeq
seqName :: MolSeq -> String
seqName obj = (namn obj)
--Räknar ut längden på MolSeq
seqLength :: MolSeq -> Int
seqLength obj = length(sekv obj)
--Plockar ut sekvensen ut MolSeq
seqSequence :: MolSeq -> String
seqSequence obj = (sekv obj)

-- 3
--Räknar ut hur många tecken som skiljer sig i sekvenserna.
diff :: [Char] -> [Char] -> Integer
diff [] [] = 0
diff (x:xs) (y:ys) = if x == y then diff xs ys else 1 + diff xs ys

--Räknar ut evolutionära avståndet mellan två MolSeqs utav samma typ.
seqDistance :: MolSeq -> MolSeq -> Double
seqDistance firstObj secondObj = if (whatType firstObj) /= (whatType secondObj) then error("Kan inte jämföra två olika strängar") else distance where 
 distance 
  |whatType firstObj == Protein && alpha > 0.94 = 3.7
  |whatType firstObj == Protein && alpha <= 0.94 = -(19/20) * log (1 - ((20*alpha)/19)) 
  |whatType firstObj == DNA && alpha >0.74 = 3.3
  |whatType firstObj == DNA && alpha <= 0.74 = -(3/4) * log (1 - ((4*alpha)/3)) 
  where 
    alpha = fromIntegral(diff (sekv firstObj) (sekv secondObj))/fromIntegral(seqLength firstObj)

--Skaoar en typ Profile
data Profile = Profile {profName :: String, quantity :: Int, matrix :: [[(Char, Int)]], profileType :: Type}

nucleotides = "ACGT"
aminoacids = sort "ARNDCEQGHILKMFPSTWYVX"
makeProfileMatrix :: [MolSeq] -> [[(Char, Int)]]  --Tar en MolSeq och returnerar en lista av listor beståenda av tupler
makeProfileMatrix [] = error "Empty sequence list"
makeProfileMatrix sl = res where 
 t = whatType (head sl) --Kollar typen på MolSeqen
 defaults =        
  if (t == DNA)
  then 
   zip nucleotides (replicate (length nucleotides) 0) -- Rad (i) --Om DNA så zippa varje objekt i nukleoidsträng med 0, detta bildar en lista med tupler. replicate återskapar 0 lika många gånger som det finns tecken.
  else 
   zip aminoacids (replicate (length aminoacids) 0) -- Rad (ii) --Om Protein så zippa varje objekt i amonisträng med 0, detta bildar en lista med tupler. 
 strs = map seqSequence sl -- Rad (iii) -- tar ut varje sekvens ur respektive MolSeq och lagrar i en lista.
 tmp1 = map (map (\x -> ((head x), (length x))) . group . sort) --grupperar och sorterar de tecken som förekommer, räknar sedan hur många det är av varje enskilt tecken och skapar en lista av tupler inhållandes "nyckeln" som är tecknet och antalet förekomster.
  (transpose strs) -- Rad (iv)
 equalFst a b = (fst a) == (fst b) 
 res = map sort (map (\l -> unionBy equalFst l defaults) tmp1) --Tar de skapade listorna och sammansätter dem, tar bort dubletter och sorterar på bokstavsordning.

--Skapar en Profile utav en MolSeq. 
molseqs2profile :: String -> [MolSeq] -> Profile
molseqs2profile pName molseq = Profile pName quantity matrix molType where  
 matrix = makeProfileMatrix molseq 
 quantity = length molseq 
 molType = whatType (head molseq) 
-- Tar ut namnet från Profile
profileName :: Profile -> String
profileName pName = (profName pName)
--rälnar ut antalet förekomster av ett tecken delat på antal tecken per sekvens.
profileFrequency :: Profile -> Int -> Char -> Double
profileFrequency profile i c = freq / fromIntegral (quantity profile) where
 freq = checkChar (matrix profile !! i) c


-- kollar om Tecknet är det man angett.
checkChar :: [(Char, Int)] -> Char -> Double
checkChar (x:xs) c
 |fst x == c = fromIntegral (snd x)
 |otherwise = checkChar xs c 
--Räknar ut evolutionära avståndet av två Profile.
profileDistance :: Profile -> Profile -> Double
profileDistance fstProfile sndProfile = sum dist where
 dist = [abs((profileFrequency fstProfile i c) - (profileFrequency sndProfile i c)) | i <- [0..end] ,c <- chars]
 chars = if profileType (fstProfile) == DNA then nucleotides else aminoacids
 end = length (matrix fstProfile) -1



--4

--Skapar en klass med tre funktioner
class Evol a where
 name :: a -> String
 name a = ""
 distance :: a -> a -> Double
 distance a b = 0.0
 distanceMatrix :: [a] -> [(String, String, Double)]
 distanceMatrix [] = []
 distanceMatrix serie = compare(head serie) serie ++ distanceMatrix (tail serie) where
  compare a [] = []
  compare first serie = diffList first (head serie) : compare first (tail serie)
  diffList a b = (name a, name b, distance a b)
--Skapar en MolSeq-instans av evol
instance Evol MolSeq where
 name a = seqName a
 distance a b = seqDistance a b
--Skapar en Profileinstans av evol.
instance Evol Profile where
 name a = profileName a
 distance a b = profileDistance a b





{-testing.hs:97:2: error:
    Pattern bindings (except simple variables) not allowed in class declaration:
      distanceMatrix :: [a]
                        -> [(String String Double)] distanceMatrix (x : xs)
        = nextElem (x : xs) 0 ++ distanceMatrix (xs)
        where
            nextElem (x : xs) i
              | i < length (x : xs)
              = (name x, name ((x : xs) !! i), distance x ((x : xs) !! i))
                : nextElem (x : xs) (i += 1)
              | otherwise = []
Failed, modules loaded: none.       VARFÖR??-}





