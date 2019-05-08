#pragma once
#include<string>
using namespace std;
class Edge
{
public:
	Edge();
	Edge(int from, int to, int dis);

	int get_dest();
	int get_source();
	int get_ends();
	//string to_string();
	

private:
	int start_vertix;
	int end_vertix;
	int distance;

};
