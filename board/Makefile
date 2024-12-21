CXX = g++
CXXFLAGS = -O3 -Wall -std=c++11 -fPIC `python3 -m pybind11 --includes`

UNAME := $(shell uname)
ifeq ($(UNAME), Darwin)
    LIB_EXT = so  # macOS uses .so for Python modules
else ifeq ($(UNAME), Linux)
    LIB_EXT = so
else ifeq ($(UNAME), Windows)
    LIB_EXT = pyd  # Windows uses .pyd for Python modules
endif

TARGET = solver_lib.$(LIB_EXT)  # Updated to solver_lib
SRC = wrapper.cpp solver.cpp

all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) -shared -o $@ $^ `python3-config --ldflags`

clean:
	rm -f $(TARGET)

.PHONY: all clean
