#!/bin/bash

make && \
java \
    -classpath out \
    com.craftinginterpreters.tool.GenerateAst \
    src/com/craftinginterpreters/lox
