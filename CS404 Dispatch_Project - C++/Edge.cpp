#include "Edge.h"
#include <string>

Edge::Edge()
{
	start_vertix = -1;
	end_vertix = -1;
	distance = -1;
}

Edge::Edge(int from, int to, int dis)
{
	start_vertix = from;
	end_vertix = to;
	distance = dis;
}

int Edge::get_dest()
{
	return distance;
}

int Edge::get_source()
{
	return start_vertix;
}

int Edge::get_ends()
{
	return end_vertix;
}



/*std::string Edge::to_string()
{
//string toSTR = "Started from " + string(start_vertix) + " to " + string(end_vertix) + ": " + string(distance);
return "Started from " + std::to_string(start_vertix) + " to " + std::to_string(end_vertix) + ": " + std::to_string(distance);
}*/