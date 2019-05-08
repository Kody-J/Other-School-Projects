//Kody Johnson
//Program III
//CS 201R - 002

#include "stdafx.h"
#include "Character.h"
#include <iostream>
#include <string>
#include "Utils.h"

using namespace std;

Character::Character()
{
}

// Initilizes the Name, Health Points(hp), Attack point (atk), and Defense (def) based on user inputs
void Character::setUp(string &_name, int _hp, int _atk, int _def)
{
	name = _name;
	hp = _hp;
	atk = _atk;
	def = _def;

}

// Prints the stats of the object (hp, atk, and def)
void Character::displayStats()
{
	cout << name;
	cout.width(6);
	cout << internal << "HP: " << hp << ", ATK: " << atk << ", Def: " << def << endl;
}

//Void in character, to be used in Player aand Enemy class
void Character::selectAction()
{
}

// Determins the amount of attack damage to pass into gitHIt() to subtrack from HP
int Character::getAttack()
{
	// If attack Type is offensive att a random number from 1-3 to the atk value and return it
	if (_attackType == offensive)
	{
		Utils temp;
		int tempAtkDmg = temp.getRandom(1, 3); // Randomly detemins the amount of damage to be inflicted (high, the amount of attack points(atk) - low, 5)
		tempAtkDmg += atk;
		cout << name << " does an Offensive attack! " << tempAtkDmg << " points of damage!" << endl;
		return tempAtkDmg;
	}
	cout << name << " does a Defensive attack! " << atk << " points of damage!" << endl;
	return atk;
}

// Determins what amount of dmg to reduce from HP based on _attackType
void Character::getHit(int _atk)
{
	//Cheks if _attackType is Offensive and reduces hp (atk - def)
	if (_attackType == offensive)
	{
		int dmgDelt = _atk - def;
		if (dmgDelt < 0) // catches if the dmg delt is less than zero
			dmgDelt = 5;
		if (hp - dmgDelt >= 0)// catches if hp would be less than 0
			hp -= dmgDelt;
		else
			hp = 0;
	}

	else
	{
		int dmgDelt = _atk - def - rand() % 3 + 1;
		if (hp - dmgDelt >= 0)
		{
			hp -= dmgDelt;
		}
		else
			hp = 0;
	}
}

int Character::getHP()
{
	return hp;
}

string Character::getname()
{
	return name;
}


