//Kody Johnson
//Program III
//CS 201R - 002

#include "stdafx.h"
#include "Player.h"
#include <iostream>
#include "Character.h"
#include "Utils.h"

using namespace std;

Player::Player()
{
}

//Prompt the to enter an option (1. for attack and 2. for defensive)
void Player::selectAction()
{
	char usrInpt;
	cout << "1. Offensive Attack \n2. Defensive Attack" << endl;
	cin >> usrInpt;
	while (usrInpt != '1' && usrInpt != '2') // Keeps asking user to make a valid input till recieved
	{
		cout << "Entry invalid, please choose again: " << endl;
		cin >> usrInpt;
	}
	if (usrInpt == '1')  // Settig the _attackType based on valid user input
		_attackType = offensive;
	else
		_attackType = defensive;
	
}

