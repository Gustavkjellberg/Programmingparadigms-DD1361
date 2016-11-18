# Labb F2

Detta är en mer omfattande labb i funktionell programmering i
Haskell.  Se labb-peket för uppgifts-instruktioner.

## Inlämning

Lösningen ska läggas i en katalog `F2/` (stort F) i repot och skickas
in som hämtbegäran.  Du kan ge din hämtbegäran vilken titel du vill,
t.ex. "Labb-inlämning".

Beskrivningen av din hämtbegäran ska innehålla följande:

* `Kattis: <id>`

  där `<id>` är Submission-ID på Kattis för din godkända lösning.

* `Students: @<username> @<username>`

  där `<username>` ger ditt och din labbkompis användarnamn
  (KTH-användarnamnet, samma användarnamn som du har på ditt KTH
  Git-konto).  Om du labbat själv anger du bara ditt eget
  användarnamn.

  Observera: för att ditt Git-konto ska kunna matchas mot ditt
  Kattis-konto krävs att antingen:
  - Du har knutit ditt Kattis-konto till ditt kth.se-konto (detta borde
    vara fallet för de allra flesta), eller
  - Du har lagt till (och verifierat) din kth.se-epost-adress till
    ditt Kattis-konto

whatType firstObj == Protein && alpha < 0.94 =


seqDistance :: MolSeq -> MolSeq -> Double
seqDistance firstObj secondObj = if whatType firstObj /= whatType secondObj then error("kaos") else distance where 
  distance
    |whatType firstObj == Protein && alpha > 0.94 = 3.7
    |whatType firstObj == Protein && alpha < 0.94 = -(19/20) * log (1 - ((20*alpha)/19)) 
    |whatType firstObj == DNA && alpha >0.74 = 3.3
    |whatType firstObj == DNA && alpha < 0.74 = -(3/4) * log (1 - ((4*alpha)/3)) 
    where alpha = fromIntegral(trying)/fromIntegral(seqLen firstObj)
  trying = diff (sekv firstObj) (sekv secondObj)





  diff :: [Char] -> [Char] -> Double
i = 0
diff (x:xs) (y:ys) = if x == y then diff xs ys else 1 + diff xs ys


seqDistance :: MolSeq -> MolSeq -> Double
seqDistance firstObj secondObj = if (whatType firstObj) /= (whatType secondObj) then error("kaos") else distance where 
  distance
    |whatType firstObj == Protein && alpha > 0.94 = 3.7
    |whatType firstObj == Protein && alpha < 0.94 = -(19/20) * log (1 - ((20*alpha)/19)) 
    |whatType firstObj == DNA && alpha >0.74 = 3.3
    |whatType firstObj == DNA && alpha < 0.74 = -(3/4) * log (1 - ((4*alpha)/3)) 
    where 
      alpha = fromIntegral difference / fromIntegral dist