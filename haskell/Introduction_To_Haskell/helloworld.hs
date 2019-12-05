{-# OPTIONS_GHC -Wall #-}

default Num Integer

f :: Num a => a -> a -> a
f x y = (+) ((*) x x) ((*) y y)

main :: IO ()
main = print $ f 2 4

-- absolute :: (Ord a, Num a) => a -> a
-- absolute x = if x >= 0 then x else -x

-- absolute' x
--     | x >= 0 = x
--     | otherwise = -x

-- main = do
--     print $ absolute 3
--     print $ absolute (-4)
--     print $ absolute' (-5)

-- selectWin1 = snd
-- selectWin2 = fst . fst
-- selectWin3 = fst . snd . snd

-- main = do
--     print $ selectWin1 (1,"win")
--     print $ selectWin2 (("win","no"),"not this one")
--     print $ selectWin3 (1,("no",("win","almost")))

-- f :: a -> a
-- f x = x

-- h :: t -> [Char]
-- h x = "Hello"

-- p :: (Num a) => a -> a -> a -> a
-- p a b c x = a*x*x + b*x + c

-- f :: Num a => a -> a -> a
-- f x y = x*x + y*y
-- x :: Int
-- x = 3
-- y :: Float
-- y = 2.4
-- main = print (f x y)
-- main = print (f 3 2.4)


-- f :: Num a => a -> a -> a
-- g :: Num a => a -> a
-- f x y = x*x + y*y
-- -- g = f 3
-- g = \y -> 3*3+ y*y
-- main = print (g 2)

-- g x y = x*x - y*y + x - y
-- main = do
--     print $ g 3 2
--     print $ g 3 4

-- main = do
--     putStrLn "What is your name?"
--     name <- getLine
--     putStrLn $ "Hello " ++ name ++ "!"

-- main = putStrLn "Hello, World!"
