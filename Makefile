CXX = g++
CXXFLAGS = -Wall -O2

TARGET = health_agent
SRC = src/main.cpp

all:
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET)

clean:
	rm -f $(TARGET)
