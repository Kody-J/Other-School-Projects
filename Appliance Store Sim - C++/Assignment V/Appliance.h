/*
Kody Johnson
CS 201 - 002
Assignment v
*/
#pragma once
#include <string>
#include <iostream>

using namespace std;

class Appliance
{
public:
	Appliance();
	//Sets the model number
	void setModelNumber(string mn);
	//Sets the serial number
	void setSerialNumber(string sn);
	//returns the model number
	string getModelNumber();
	//returns the serial number
	string getSerialNumber();
	//Used in child classes to return as string of the appliance type
	virtual string reportType() const = 0;
	//Used by child classes to read in the data from the file and sets their objects data accordingly 
	virtual void readData(istream& a) = 0;
	//Used by child classes to print out the Serial and Model numbers
	virtual void WriteData() const;

	~Appliance();

private:
	string modelNumber, serialNumber;
	
};

