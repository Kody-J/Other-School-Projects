#include "stdafx.h"
#include "Refrigerator.h"


Refrigerator::Refrigerator()
{
	capicity = 0;
	frostFree = false;
}

string Refrigerator::reportType() const
{
	string type = "'Refrigerator'";
	return type;
}
void Refrigerator::readData(istream &fn)
{
	//Creates temporary variables to then set the varius data 
	string tempSN, tempMN;
	char tempFrost;
	fn >> tempMN >> tempSN >> capicity >> tempFrost;
	setModelNumber(tempMN);
	setSerialNumber(tempSN);
	if (tempFrost == 'T' || tempFrost == 't')
		frostFree = true;
}

void Refrigerator::WriteData() const
{
	Appliance::WriteData();
	cout << " " << capicity << " ";
	if (frostFree == true)
		cout << "T";
	else
		cout << "F";
}

Refrigerator::~Refrigerator()
{
}
