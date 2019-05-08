//Kody Johnson
//Program III
//CS 201R - 002

#pragma once
#include "Character.h"
using namespace std;

class Player : public Character
{
public:
	Player();
	//Lets the user choose to do Offensive or Defensive
	void selectAction();
	
};

