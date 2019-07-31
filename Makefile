
robot-four: robot-four.cpp
	g++ -std=c++17 robot-four.cpp `pkg-config opencv --cflags --libs`

clean:
	rm a.out
