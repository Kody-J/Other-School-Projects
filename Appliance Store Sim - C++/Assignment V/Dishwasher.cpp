#include "stdafx.h"
#include "Dishwasher.h"


Dishwasher::Dishwasher()
{
}

string Dishwasher::reportType() const
{
	string type = "'Dishwasher'";
	return type;
}

void Dishwasher::readData(istream &fn)
{
	string tempMN, tempSN;
	char tempWS, tempHT;
	fn >> tempMN >> tempSN >> cycleTime >> tempWS >> tempHT;
	setModelNumber(tempMN);
	setSerialNumber(tempSN);
	if (tempWS == 'T' || tempWS == 't')
		waterSaver = true;
	else
		waterSaver = false;
	if (tempHT == 'T' || tempHT == 't')
		highTemp = true;
	else
		highTemp = false;

}

void Dishwasher::WriteData() const
{
	Appliance::WriteData();
	cout << " " << cycleTime << " ";
	if (waterSaver == true)
		cout << "T ";
	else
		cout << "F ";
	if (highTemp == true)
		cout << "T";
	else
		cout << "F";

}


Dishwasher::~Dishwasher()
{
}
