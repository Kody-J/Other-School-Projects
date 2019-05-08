#pragma once
#include "Appliance.h"
#include <string>

using namespace std;


class Oven : public Appliance
{
public:
	Oven();
	//Returns a string of the objects data type "Oven"
	string reportType() const;
	//Used to read in the data from the file and sets objects data accordingly
	void readData(istream&fn);
	//Used to print out the objects data values 
	void WriteData() const;
	~Oven();
private:
	float capacity;
	bool selfCleaning, convection;

};

