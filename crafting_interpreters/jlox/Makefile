SRC_DIR := src
OUT_DIR := out
SRCS := $(shell find $(SRC_DIR) -name "*.java")
CLS := $(SRCS:$(SRC_DIR)/%.java=$(OUT_DIR)/%.class)
JC := javac
JCFLAGS := -d $(OUT_DIR)/ -cp $(SRC_DIR)/
MAIN_CLASS := com.craftinginterpreters.lox.Lox

.SUFFIXES: .java

.PHONY: all clean run

all: $(CLS)

$(CLS): $(OUT_DIR)/%.class: $(SRC_DIR)/%.java
	$(JC) $(JCFLAGS) $<

clean:
	rm -rf $(OUT_DIR)

run: $(CLS)
	@java -classpath $(OUT_DIR) $(MAIN_CLASS)
