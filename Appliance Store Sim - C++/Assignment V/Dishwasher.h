/*
Kody Johnson
CS 201 - 002
Assignment v
*/
#pragma once
#include "Appliance.h"
#include <string>

using namespace std;

class Dishwasher : public Appliance
{
public:
	Dishwasher();
	//Returns a string of objects type "Dishwasher"
	string reportType() const;
	//Used to read in the data from the file and sets objects data accordingly   
	void readData(istream&);
	//Used to print out the objects data values
	void WriteData() const;
	~Dishwasher();

private:
	int cycleTime;
	bool waterSaver, highTemp;
};

