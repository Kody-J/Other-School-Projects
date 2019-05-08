#pragma once
#include<string>
#include"Edge.h"
#include<vector>
#include "Vehicle.h"
#include <iostream>

using namespace std;


class Vertix
{
public:
	Vertix();
	Vertix(int zc) : ZipCode(zc), vehicles(3), visited(false) {};

	void set_status(bool v);
	bool get_status();
	int get_zipcode();
	void set_edge(vector<Edge> &others);
	void set_vehicles(Vehicle others);
	vector<vector<Vehicle>> getVehicles();
	void remove_vehicle(int idx);


private:
	int num_edges;
	int ZipCode;
	bool visited;
	vector<Edge> edges;
	vector<vector<Vehicle>> vehicles;


};
