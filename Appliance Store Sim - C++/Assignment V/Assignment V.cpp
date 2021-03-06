// Assignment V.cpp : Defines the entry point for the console application.
// Appliance Store Simulator
/*
Kody Johnson
CS 201R-002
Assignment V

Recieves a list of appliances from a new shipment and updates inventory

*/

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include "Appliance.h"
#include "Dishwasher.h"
#include "Oven.h"
#include "Refrigerator.h"
#include "Assignment V.h"

using namespace std;

void writeStuff(Appliance *items[], int count, const string& targetType);

int main()
{

	ifstream fin("appliances.txt");
	Appliance **InStock = new Appliance*[100];
	char typeOfAppliance;

	//Checks if the file is valid sends error msg and returns -1 if not
	if (!fin.good())
	{
		cout << "Could not open this file " << endl;
		system("pause");
		return -1;
	}
	// main loop which itterates through the file and creates objects of the corresponding data types untill file is empty
	int idxCnt = 0;
	while (fin >> typeOfAppliance)
	{
		if (typeOfAppliance == 'R')
		{
			Refrigerator *tempFridge = new Refrigerator;//temporary object to be stored in InStock array
			tempFridge->readData(fin); //sets the objects data 
			InStock[idxCnt] = tempFridge; //places the object int the Instock array
			idxCnt += 1;
		}
		else if (typeOfAppliance == 'D') //Repeats for this object the same as the last type
		{
			Dishwasher *tempDishWash = new Dishwasher;
			tempDishWash->readData(fin);
			InStock[idxCnt] = tempDishWash;
			idxCnt += 1;
		}
		else //Repeats for this object the same as the last type
		{
			Oven *tempOven = new Oven;
			tempOven->readData(fin);
			InStock[idxCnt] = tempOven;
			idxCnt += 1;
		}
	}
	//Printing the data based on data type
	cout << "Recived the following appliances (total: " << idxCnt << ") \n" << endl;
	int typeCnt = 0;
	while (typeCnt < 3)
	{
		if (typeCnt == 0)
		{
			cout << "Ovens: " << endl;
			writeStuff(InStock, idxCnt, "Oven");
			cout << endl;
			typeCnt += 1;
		}
		else if (typeCnt == 1)
		{
			cout << "Dishwasher: " << endl;
			writeStuff(InStock, idxCnt, "'Dishwasher'");
			cout << endl;
			typeCnt += 1;
		}
		else
		{
			cout << "Refrigerators: " << endl;
			writeStuff(InStock, idxCnt, "'Refrigerator'");
			cout << endl;
			typeCnt += 1;
		}
	}
	cout << "\n\n" << "cleaning the freestore ....Done!" << endl;
	//Deletes each dynamically created pointer within the array
	for (int i = 0; i < idxCnt; i++)
		delete InStock[i];

	//Deletes the dynamic array
	delete[] InStock;
	InStock = nullptr;
	system("pause");
    return 0;
}

//Used to itterate throught the InStock array and find spicific types of objects to print out
void writeStuff(Appliance *items[], int count, const string& targetType)
{
	for (int i = 0; i < count; i++)
	{
		if (items[i]->reportType() == targetType)
		{
			items[i]->WriteData();
			cout << endl;
		}

	}

}
