JAVAC = javac
JAVA = java
SRC_DIR = src
OUT_DIR = out

all: build run clean

build:
	@mkdir -p $(OUT_DIR)
	@find $(SRC_DIR) -name "*.java" -print | xargs $(JAVAC) -d $(OUT_DIR)

run: build
	@echo "Running $(MAIN_CLASS)"
	@$(JAVA) -cp $(OUT_DIR) $(MAIN_CLASS)

clean:
	@rm -rf $(OUT_DIR)
	@echo "Cleaned $(OUT_DIR)"

ifndef MAIN_CLASS
$(error MAIN_CLASS is not set. Usage: make [target] MAIN_CLASS=<ClassName>)
endif