#pragma once
#include<string>
#include<vector>
#include<map>

#include"Edge.h"
#include "Vehicle.h"
#include "Vertix.h"

using namespace std;


class Graph
{
public:
	Graph();
	~Graph()
	{
		for (unsigned int i = 0; i < G_Vertices.size(); i++)
		{
			G_Vertices[i].set_status(false);
		}
	}

	// add vertix
	void addVertix(Vertix z);
	// add edges
	void addEdge(int from, int to, int dis);
	// print the graph
	void print();
	// print a vertix's edges
	void print_v_edges(int zipcode);
	// print a vertix's neighbours
	void print_v_neighbours(int zipcode);
	// print all edges
	void print_edges();

	int get_v_num();
	int get_e_num();

	void find_edge(int end, int start, Edge & the_one_needed);

	vector<Vertix> get_vertix();
	vector<Edge> get_edges(int zip);

private:
	vector<Vertix> G_Vertices;
	map<int, vector<Edge>> edges;
	int num_ver = 0;
	int num_edg = 0;
};

