#include "stdafx.h"
#include "Appliance.h"


Appliance::Appliance()
{
}

void Appliance::setModelNumber(string mn)
{
	modelNumber = mn;
}

void Appliance::setSerialNumber(string sn)
{
	serialNumber = sn;
}

string Appliance::getModelNumber()
{
	return modelNumber;
}

string Appliance::getSerialNumber()
{
	return serialNumber;
}



void Appliance::WriteData() const
{
	cout << modelNumber << " " << serialNumber;
}

Appliance::~Appliance()
{
}
