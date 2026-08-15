SRC_DIR := src
OUT_DIR := out
LOX_SRC_DIR := $(SRC_DIR)/com/craftinginterpreters/lox
LOX_TEST_DIR := $(SRC_DIR)/com/craftinginterpreters/test
SRCS := $(shell find $(SRC_DIR) -name "*.java")
CLS := $(SRCS:$(SRC_DIR)/%.java=$(OUT_DIR)/%.class)
JC := javac
JCFLAGS := -d $(OUT_DIR)/ -cp $(SRC_DIR)/
MAIN_CLASS := com.craftinginterpreters.lox.Lox
GENERATE_AST_CLASS := com.craftinginterpreters.tool.GenerateAst

.SUFFIXES: .java

.PHONY: all clean run test generate_ast

all: $(CLS)

$(CLS): $(OUT_DIR)/%.class: $(SRC_DIR)/%.java
	$(JC) $(JCFLAGS) $<

clean:
	rm -rf $(OUT_DIR)

run: $(CLS)
	@java -classpath $(OUT_DIR) $(MAIN_CLASS)

test: $(CLS)
	@java -classpath $(OUT_DIR) $(MAIN_CLASS) $(LOX_TEST_DIR)/test.lox

generate_ast: $(OUT_DIR)/com/craftinginterpreters/tool/GenerateAst.class
	@java -classpath $(OUT_DIR) $(GENERATE_AST_CLASS) $(LOX_SRC_DIR)
