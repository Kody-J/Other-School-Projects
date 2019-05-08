#include "stdafx.h"
#include "Oven.h"


Oven::Oven()
{
}

string Oven::reportType() const
{
	string type = "Oven";
	return type;
}

void Oven::readData(istream &fn)
{
	string tempMN, tempSN;
	char tempSC, tempCV;
	fn >> tempMN >> tempSN >> capacity >> tempSC >> tempCV;
	setModelNumber(tempMN);
	setSerialNumber(tempSN);
	if (tempSC == 'S' || tempSC == 's')
		selfCleaning = true;
	else
		selfCleaning = false;

	if (tempCV == 'C' || tempCV == 'c')
		convection = true;
	else
		convection = false;

}

void Oven::WriteData() const
{
	
	Appliance :: WriteData();
	cout << " " << capacity << " ";
	if (selfCleaning == true)
		cout << "S ";
	else
		cout << "R ";

	if (convection == true)
		cout << "C";
	else
		cout << "R";

}

Oven::~Oven()
{
}
