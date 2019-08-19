{-# OPTIONS_GHC -Wall #-}
module Golf where

---------------------------------
-- Exercise 1
---------------------------------
everyNthHelper :: [a] -> Int -> Int -> [a]
everyNthHelper [] _ _ = []
everyNthHelper (x:xs) counter n
    | counter == 0 = x : (everyNthHelper xs n n)
    | otherwise  = everyNthHelper xs (counter - 1) n

everyNth :: [a] -> Int -> [a]
everyNth xs n = everyNthHelper xs n n

skips :: [a] -> [[a]]
skips xs = [everyNth xs n | n <- [0..(length xs)-1]]

---------------------------------
-- Exercise 2
---------------------------------
localMaxima :: [Integer] -> [Integer]
localMaxima [] = []
localMaxima (x:y:z:xs)
    | y > x && y > z = y : localMaxima (y:z:xs)
localMaxima (_:xs) = localMaxima xs

---------------------------------
-- Exercise 3
---------------------------------
valToChar :: Integer -> Char
valToChar 0 = ' '
valToChar _ = '*'

decrCap :: Integer -> Integer
decrCap 0 = 0
decrCap x = x - 1

histLines :: [Integer] -> String
histLines xs
    | all (== 0) xs = []
    | otherwise     = histLines (map decrCap xs) ++ "\n" ++ (map valToChar xs)

count :: Integer -> [Integer] -> Integer
count x = toInteger . length . filter (== x)

counts :: [Integer] -> [Integer]
counts xs = [count x xs | x <- [0..9]]

histogram :: [Integer] -> String
histogram xs = histLines (counts xs) ++ "\n==========\n0123456789\n"
