#pragma once

#include "Appliance.h"
#include <string>

using namespace std;

class Refrigerator : public Appliance
{
public:
	//Sets capacity to '0' and frostfree to 'false'
	Refrigerator();
	//Returns a string of the objects data type "Refrigerator"
	string reportType() const;
	//Used to read in the data from the file and sets objects data accordingly
	void readData(istream&);
	//Used to print out the objects data values 
	void WriteData() const;
	~Refrigerator();

private:
	float capicity;
	bool frostFree;
};

