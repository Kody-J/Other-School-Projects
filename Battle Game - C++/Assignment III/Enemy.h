//Kody Johnson
//Program III
//CS 201R - 002


#pragma once
#include "Character.h"
#include <iostream>

using namespace std;

class Enemy : public Character
{
public:
	Enemy();
	void selectAction(); // randomly generates a choice for the enemy (AI) attack type
};

