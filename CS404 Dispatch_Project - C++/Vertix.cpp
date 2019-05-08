#include "Vertix.h"

Vertix::Vertix()
{
	ZipCode = -1;
	num_edges = 0;
	visited = false;
}

void Vertix::set_vehicles(Vehicle others)
{
	vehicles[others.get_type() - 1].push_back(others);
	
}

vector<vector<Vehicle>> Vertix::getVehicles()
{
	return vehicles;
}

void Vertix::remove_vehicle(int idx)
{
	vehicles[idx].pop_back();	
}

void Vertix::set_status(bool v)
{
	visited = v;
}

bool Vertix::get_status()
{
	return visited;
}

int Vertix::get_zipcode()
{
	return ZipCode;
}

void Vertix::set_edge(vector<Edge>& others)
{
	edges = others;
	num_edges++;
}

