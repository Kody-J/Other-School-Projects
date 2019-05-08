#include<iostream>
#include "Graph.h"

Graph::Graph()
{
}

void Graph::addVertix(Vertix z)
{
	G_Vertices.push_back(z);
	num_ver++;
}

void Graph::addEdge(int from, int to, int dis)
{
	edges[from].push_back({ from,to,dis });
	num_edg++;
}

void Graph::print()
{
	cout << "This Graph has " << num_ver << " vertices and " << num_edg << " edges.\n\n";
}


void Graph::print_v_edges(int zipcode)
{
	vector<Edge>  temp = edges[zipcode];
	cout << "Edges connected to " << zipcode << " are:" << endl;
	for (int i = 0; i < temp.size(); i++)
	{
		cout << "From zipcode " << zipcode << " to zipcode " << temp[i].get_ends() << " : " << temp[i].get_dest() << endl;
	}
	cout << endl;
}

void Graph::print_v_neighbours(int zipcode)
{
	map<int, vector<Edge>>::iterator it = edges.find(zipcode);
	cout << zipcode << " nieghtbours are: " << endl;
	for (int i = 0; i < it->second.size(); i++)
	{
		cout << it->second[i].get_ends() << "	";
	}
	cout << endl;
}

void Graph::print_edges()
{
	for (map<int, vector<Edge>>::iterator it = edges.begin(); it != edges.end(); it++)
	{
		for (int i = 0; i < it->second.size(); i++)
		{
			cout << it->second[i].get_source() << "	<->	" << it->second[i].get_ends() << "	:	" << it->second[i].get_dest() << endl;
		}
	}
	cout << endl;
}

int Graph::get_v_num()
{
	return num_ver;
}

int Graph::get_e_num()
{
	return num_edg;
}

void Graph::find_edge(int end, int start, Edge & the_one_needed)
{
	
	vector<Edge> spacific_edges = edges[end];

	for (int i = 0; i < spacific_edges.size(); i++) {
		if (spacific_edges[i].get_ends() == start && spacific_edges[i].get_source() == end) {
			the_one_needed = spacific_edges[i];
			break;
		}
	}

}

vector<Vertix> Graph::get_vertix()
{
	return G_Vertices;
}

vector<Edge> Graph::get_edges(int zip)
{
	return edges[zip];
}