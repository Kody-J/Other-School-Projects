#include "Dispatcher.h"


vector<int> Dispatcher::shortest_path_vec(int zip, Graph graph)
{

	vector<Edge> vertix_edges = graph.get_edges(zip);

	for (unsigned int i = 0; i < vertix_edges.size(); i++) {
		//used to deconflict indicies
		unsigned int place_marker = vertix_edges[i].get_dest();
		while (ordered_weights[place_marker] != 0) {
			place_marker++;
			//Resize the array if the index is out of range
			if (ordered_weights.size() <= place_marker)
				ordered_weights.resize(place_marker+1);
		}
		ordered_weights[place_marker] = vertix_edges[i].get_ends();
	}

	return ordered_weights;
}

void Dispatcher::sortest_path_again(int zip, Graph _graph, vector<int> & list, int start, int _weight)
{
	vector<Edge> vertix_edges = _graph.get_edges(zip);
	vector<Edge> start_compare = _graph.get_edges(zip);
	int weight = _weight; 

	for (unsigned int i = 0; i < vertix_edges.size(); i++) {
		//used to deconflict indicies
		unsigned int place_marker = vertix_edges[i].get_dest() + weight;
		while (ordered_weights[place_marker] != 0) {
			place_marker++;
			//Resize the array if the index is out of range
			if (ordered_weights.size() <= place_marker)
				ordered_weights.resize(place_marker + 1);
		}
		if(vertix_edges[i].get_source() != start_compare[i].get_ends() && vertix_edges[i].get_ends() != start_compare[i].get_source())
				list[place_marker] = vertix_edges[i].get_ends();

	}
}
