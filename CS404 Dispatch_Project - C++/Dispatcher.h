#pragma once
#include <vector>
#include "Graph.h"
#include "Edge.h"
#include <iostream>

using namespace std;


class Dispatcher
{
	vector<int> ordered_weights;


public:

	Dispatcher() : ordered_weights(25) {};
	vector<int> shortest_path_vec(int zip, Graph _graph);
	void sortest_path_again(int zip, Graph _graph, vector<int> & list, int start, int weight);


};