package com.craftinginterpreters.lox;

import java.util.HashMap;
import java.util.Map;

class Environment {
    final Environment enclosing;
    private final Map<String, Object> values = new HashMap<>();

    Environment() {
        enclosing = null;
    }

    Environment(Environment enclosing) {
        this.enclosing = enclosing;
    }

    Object get(Token name) {
        // System.out.println("get " + name.lexeme);
        if (values.containsKey(name.lexeme)) {
            Object value = values.get(name.lexeme);
            if (value != null) {
                return value;
            }

            throw new RuntimeError(name,
                "Variable not initialized: '" + name.lexeme + "'.");
        }

        if (enclosing != null) return enclosing.get(name);

        throw new RuntimeError(name,
                "Undefined variable '" + name.lexeme + "'.");
    }

    void assign(Token name, Object value) {
        // System.out.println("assign " + name.lexeme + " = " + value);
        if (values.containsKey(name.lexeme)) {
            values.put(name.lexeme, value);
            return;
        }

        if (enclosing != null) {
            enclosing.assign(name, value);
            return;
        }

        throw new RuntimeError(name,
                "Undefined variable '" + name.lexeme + "'.");
    }

    void define(String name, Object value) {
        // System.out.println("define " + name + " = " + value);
        values.put(name, value);
    }
}
