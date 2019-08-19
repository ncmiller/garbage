module TestGolf where
import Golf

testSkips :: [Bool]
testSkips =
    [ skips "ABCD" == ["ABCD", "BD", "C", "D"],
      skips "hello!" == ["hello!", "el!", "l!", "l", "o", "!"],
      skips [1] == [[1]],
      skips [True, False] == [[True, False], [False]],
      let x = [] :: [Int]
          y = [] :: [[Int]] in
      skips x == y ]

testLocalMaxima :: [Bool]
testLocalMaxima =
    [ localMaxima [2,9,5,6,1] == [9,6],
      localMaxima [2,3,4,1,5] == [4],
      localMaxima [1,2,3,4,5] == [] ]

testAll :: [[Bool]]
testAll = [ testSkips, testLocalMaxima ]
