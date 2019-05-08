//Kody Johnson
//Program III
//CS 201R - 002

#pragma once
#include "stdafx.h"
#include <iostream>

using namespace std;

class Utils
{
public:
	Utils();
	int getUserInput(int min, int max); // Prompts the user for an input and validates weather between min or max
	int getRandom(int min , int max);   // Randomly generates a number between min and max

};

