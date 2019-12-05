-- Exercise 1
toDigitsRev :: Integer -> [Integer]
toDigitsRev x
    | x < 0     = []
    | x < 10    = [x]
    | otherwise = (x `mod` 10) : toDigitsRev(x `div` 10)

toDigits :: Integer -> [Integer]
toDigits = reverse . toDigitsRev

testToDigits :: [Bool]
testToDigits =
    [ toDigits (-17) == [],
      toDigits 0 == [0],
      toDigits 1000 == [1,0,0,0],
      toDigits 01000 == [1,0,0,0],
      toDigits 1234 == [1,2,3,4],
      toDigitsRev 1234 == [4,3,2,1] ]

-- Exercise 2
doubleEveryOther :: [Integer] -> [Integer]
doubleEveryOther = reverse . doubleEveryOtherLeft . reverse

doubleEveryOtherLeft :: [Integer] -> [Integer]
doubleEveryOtherLeft [] = []
doubleEveryOtherLeft [x] = [x]
doubleEveryOtherLeft (x:y:xs) = x : 2 * y : doubleEveryOtherLeft xs

testDoubleEveryOther :: [Bool]
testDoubleEveryOther =
    [ doubleEveryOther [] == [],
      doubleEveryOther [4] == [4],
      doubleEveryOther [1,2] == [2,2],
      doubleEveryOther [1,2,3] == [1,4,3],
      doubleEveryOther [8,7,6,5] == [16,7,12,5] ]

-- Exercise 3
sumDigits :: [Integer] -> Integer
sumDigits xs = sum [sum (toDigits x) | x <- xs]

testSumDigits :: [Bool]
testSumDigits =
    [ sumDigits [] == 0,
      sumDigits [2] == 2,
      sumDigits [42] == 6,
      sumDigits [16,123] == 13,
      sumDigits [16,7,12,5] == 22 ]

-- Exercise 4
validate :: Integer -> Bool
validate x = (checksum x) `mod` 10 == 0

checksum :: Integer -> Integer
checksum = sumDigits . doubleEveryOther . toDigits

testValidate :: [Bool]
testValidate =
    [ validate 4012888888881881 == True,
      validate 4012888888881882 == False ]

-- Exercise 5
type Peg = String
type Move = (Peg, Peg)
hanoi :: Integer -> Peg -> Peg -> Peg -> [Move]
hanoi n _ _ _ | n <= 0 = []
hanoi n a b c = (hanoi (n-1) a c b) ++ [(a,b)] ++ (hanoi (n-1) c b a)

testHanoi :: [Bool]
testHanoi =
    [ hanoi 2 "a" "b" "c" == [("a","c"),("a","b"),("c","b")],
      length (hanoi 15 "a" "b" "c") == 32767 ]

-- Exercise 6
hanoiFour :: Integer -> Peg -> Peg -> Peg -> Peg -> [Move]
hanoiFour n _ _ _ _ | n <= 0 = []
hanoiFour 1 a _ _ d = [(a,d)]
hanoiFour 2 a b _ d = [(a,b),(a,d),(b,d)]
hanoiFour n a b c d =
    (hanoiFour (n-k) a c d b) ++
    (hanoi k a d c) ++
    (hanoiFour (n-k) b c a d)
    where k = floor(sqrt(fromInteger(2*n) :: Double)) :: Integer

testHanoiFour :: [Bool]
testHanoiFour =
    [ length (hanoiFour 2 "a" "b" "c" "d") == 3,
      length (hanoiFour 15 "a" "b" "c" "d") == 129 ]

main :: IO ()
main = do
    print $ testToDigits
    print $ testDoubleEveryOther
    print $ testSumDigits
    print $ testValidate
    print $ testHanoi
    print $ testHanoiFour
