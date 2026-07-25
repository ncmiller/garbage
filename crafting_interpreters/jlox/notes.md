# Chapter 5

grammar metasyntax:

```
expr → expr ( "(" ( expr ( "," expr )* )? ")" | "." IDENTIFIER )+
     | IDENTIFIER
     | NUMBER
```

example:
```
asdf(qwer, xcvb)
```

without syntactic sugar:

```
expr -> expr ( "(" ")" )
expr -> expr ( "(" ( expr ) ")" )
expr -> expr ( "(" ( expr (params) ) ")" )
expr -> expr ( "(" ( expr ) "." IDENTIFIER ))
expr -> expr ( "(" ( expr (params) ) "." IDENTIFIER ))
expr -> IDENTIFIER
expr -> NUMBER

params -> "," expr params
params -> ""
```

This encodes a function call, roughly. Though there are some productions
that would be invalid (such as `123()`).
