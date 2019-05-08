//Kody Johnson
//Program III
//CS 201R - 002

#pragma once
#include <string>

using namespace std;


class Character
{
public:
	Character();
	void setUp(string &_name, int _hp, int _atk, int _def); // Initilizes the member variables name, hp, atk, and def 
	void displayStats();                                    // Prints the characters name, hp, atk , and def
	void selectAction(); // used in player and enemy classes
	int getAttack();     //calculates how much damage is done
	void getHit(int _atk); // determins how much heatl (hp) is lost
	int getHP(); // prints the amount of hp the character has
	string getname(); // returns the charaters name



protected:
	enum attackType { offensive, defensive }; // creates an attack type
	attackType _attackType;
	string name;

private:
	static int counter;
	int hp, atk, def;
	
	


};

