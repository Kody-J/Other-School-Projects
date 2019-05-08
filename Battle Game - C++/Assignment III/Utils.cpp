//Kody Johnson
//Program III
//CS 201R - 002

#include "stdafx.h"
#include "Utils.h"
#include <iostream>

using namespace std;

Utils::Utils()
{
}

int Utils::getUserInput(int min, int max)
{
	int usrInpt;  // place holder for usr input
	cin >> usrInpt; // get usr input
	while (usrInpt > max || usrInpt < min) // asks for usr input till valid
	{
		cout << "Invalid choice, try again: >> ";
		cin >> usrInpt;
	}
	return usrInpt;
}
 
// Randomly generates a choice for the (AI)
int Utils::getRandom(int min, int max)
{

	int xRan = rand() % max + min;
	return xRan;
}



