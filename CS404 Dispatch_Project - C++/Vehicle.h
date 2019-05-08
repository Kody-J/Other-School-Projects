#pragma once
#include <vector>
#include "Random_Data_Generator.h"
#include <cstdlib>
#include <iostream>

using namespace std;


class Vehicle
{
public:
	Vehicle();
	Vehicle(int id, int t, int zipcode);
	int get_id();
	int get_type();
	int get_zipcode();
	void printInfo();
	vector<Vehicle> getVehicle_vec();
	void generate_E_vec(int first, int last, int size);
	void reset_vehicle();

private:

	int ID;
	int type;
	int ZipCode;
	vector<Vehicle> vehicle_vec;

};

