#include "Vehicle.h"

Vehicle::Vehicle()
{
	ID = -1;
	type = -1;
	ZipCode = 99999;
}



Vehicle::Vehicle(int id, int t, int zipcode)
{
	ID = id;
	type = t;
	ZipCode = zipcode;
}

int Vehicle::get_id()
{
	return ID;
}

int Vehicle::get_type()
{
	return type;
}

int Vehicle::get_zipcode()
{
	return ZipCode;
}

void Vehicle::printInfo()
{
	cout << "Vehicle ID: " << ID << " Type: " << type << " Zipcode: " << ZipCode << endl;
}

vector<Vehicle> Vehicle::getVehicle_vec()
{
	return vehicle_vec;
}

void Vehicle::generate_E_vec(int first, int last, int size)
{
	Random_Data_Generator thing; 
	for (int i = 0; i < size; i++) {
		Vehicle vehicle_generator(i + 1, thing.getRan_type(), thing.getRan_zip());
		vehicle_vec.push_back(vehicle_generator);
	}
}

void Vehicle::reset_vehicle()
{
	ID = -1;
	type = -1;
	ZipCode = 99999;
}
