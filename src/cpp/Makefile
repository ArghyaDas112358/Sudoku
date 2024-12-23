CXX = g++
CXXFLAGS = -O3 -Wall -std=c++11 -fPIC `python3 -m pybind11 --includes` -Iinclude

UNAME := $(shell uname)
ifeq ($(UNAME), Darwin)
    LIB_EXT = so  # macOS uses .so for Python modules
else ifeq ($(UNAME), Linux)
    LIB_EXT = so
else ifeq ($(UNAME), Windows)
    LIB_EXT = pyd  # Windows uses .pyd for Python modules
endif

OUTPUT_DIR ?= .   # Default output directory is current directory
TARGET = $(OUTPUT_DIR)/solver_lib.$(LIB_EXT)
SRC = src/wrapper.cpp src/solver.cpp

all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) -shared -o $@ $^ `python3-config --ldflags`

clean:
	rm -f $(OUTPUT_DIR)/solver_lib.$(LIB_EXT)

.PHONY: all clean
