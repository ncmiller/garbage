{-# OPTIONS_GHC -Wall #-}
module LogAnalysis where

import Log

---------------------------------
-- Exercise 1
---------------------------------
parseMessageWords :: [String] -> LogMessage
parseMessageWords ("E":word1:word2:msgWords) = LogMessage (Error level) tstamp msg
    where level = read word1 :: Int
          tstamp = read word2 :: Int
          msg = unwords msgWords :: String
parseMessageWords (msgType:word1:msgWords)
    | msgType == "W" = LogMessage Warning tstamp $ msg
    | msgType == "I" = LogMessage Info tstamp $ msg
    where tstamp = read word1 :: Int
          msg = unwords msgWords :: String
parseMessageWords msgWords = Unknown $ unwords msgWords

parseMessage :: String -> LogMessage
parseMessage = parseMessageWords . words

parse :: String -> [LogMessage]
parse = map parseMessage . lines

---------------------------------
-- Exercise 2
---------------------------------
insert :: LogMessage -> MessageTree -> MessageTree
insert (Unknown _) tree = tree
insert newLog (Node left (Unknown _) _) = insert newLog left -- malformed tree...
insert newLog Leaf = Node Leaf newLog Leaf
insert newLog@(LogMessage _ logStamp _) (Node left node@(LogMessage _ nodeStamp _) right)
    | logStamp < nodeStamp = Node (insert newLog left) node right
    | otherwise            = Node left node (insert newLog right)

---------------------------------
-- Exercise 3
---------------------------------
build :: [LogMessage] -> MessageTree
build [] = Leaf
build (x:xs) = insert x (build xs)

---------------------------------
-- Exercise 4
---------------------------------
inOrder :: MessageTree -> [LogMessage]
inOrder Leaf = []
inOrder (Node left node right) = (inOrder left) ++ [node] ++ (inOrder right)

---------------------------------
-- Exercise 5
---------------------------------
whatWentWrongSorted :: [LogMessage] -> [String]
whatWentWrongSorted [] = []
whatWentWrongSorted ((LogMessage (Error level) _ msg):logs)
    | level < 50 = whatWentWrongSorted logs
    | otherwise = (msg:(whatWentWrongSorted logs))
whatWentWrongSorted (_:xs) = whatWentWrongSorted xs

whatWentWrong :: [LogMessage] -> [String]
whatWentWrong = whatWentWrongSorted . inOrder . build
