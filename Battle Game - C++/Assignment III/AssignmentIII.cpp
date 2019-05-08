// AssignmentIII.cpp : Defines the entry point for the console application.
//Kody Johnson
//Program III Battle type game
//CS 201R - 002

#include "stdafx.h"
#include "Utils.h"
#include "Enemy.h"
#include "Player.h"
#include <iostream>
#include <string>
#include <cstdlib>


using namespace std;
void setUpCharacters(Player &a, Enemy &b); //Initilizes the member variables of the user and AI classes

int main()
{
	int round = 1;							 //counter to track the number of rounds
	Player user_player;					     // creating the first player object
	Enemy ai_player;						 // creating the first AI object (enemy)
	setUpCharacters(user_player, ai_player); //Gets the information for both objects
	user_player.displayStats();              // Prints the players choice stats
	ai_player.displayStats();				 // Prints the AI choice stats
	Utils choice;							 //Creating a object to ask for user and enemy output			
	cout << " \nReady? \n1. Ready \n2. Change" << endl; // Asking if the user is okay with the round match up
	int usrChoice = choice.getUserInput(1, 2);			// Gets the user input and checks if valid
	

	//If the user is Not ready and wants to chang things then this loops to allow user to change 
	while(usrChoice != 1)
	{
		setUpCharacters(user_player, ai_player);
		user_player.displayStats();
		ai_player.displayStats();
		cout << " \nReady? \n1. Ready \n2. Change" << endl;
		usrChoice = choice.getUserInput(1,2);
	}
	while (user_player.getHP() > 0 && ai_player.getHP() > 0)
	{
		cout << "-------------------" << endl;
		cout << "ROUND " << round << " \n\n";   // Display the round number
		user_player.displayStats(); // Display the user stats
		ai_player.displayStats();   // Display the ai stats
		user_player.selectAction(); // set the players action type
		ai_player.selectAction();   //  set the AI action type

		int usrAtkDmg = user_player.getAttack(); // Determins the amount of Dmg the player will inflict
		int ai_tempHp = ai_player.getHP(); // Create a temporarry value to display HP loss 
		ai_player.getHit(usrAtkDmg);    // subtract the damage from the user to the AI
		cout << "Enemy is hit for " << ai_tempHp - ai_player.getHP() << endl;

		int aiAtkDmg = ai_player.getAttack(); //Determins the amount of Dmg the AI will inflict
		int usr_tempHp = user_player.getHP();
		user_player.getHit(aiAtkDmg);		  // subtracts the damage from the AI to the user
		cout << user_player.getname() << " is hit for " << usr_tempHp - user_player.getHP() << endl;
		round++; // increment the round counter
		cout << " \n";
	}
	// Determins who wins and prints the results
	if(user_player.getHP() == 0)
	{
		cout << "You Loose!" << endl;
	}
	else
		cout << "You win! " << endl;
	getchar();
}


void setUpCharacters(Player &a, Enemy &b) 
{
	string usrName;
	cout << "PLAYER SETUP \nEnter name: "; //Get any user name
	cin >> usrName;
	cout << "\n\nStats \n1. 5 ATK,  15 DEF \n2. 15 ATK, 5  DEF \n3. 10 ATK, 10 Def" << endl;
	cout << "Choose Stats: >> ";
	Utils choice;
	int usrChoice = choice.getUserInput(1,3);
	switch (usrChoice)
	{
	case 1:
		a.setUp(usrName, 100, 5, 15);
		break;
	case 2:
		a.setUp(usrName, 100, 15, 5);
		break;
	case 3:
		a.setUp(usrName, 100, 10, 10);
		break;
	}
	//The same but random for the enemy character
	Utils tempChoice;
	int enemyChoice = tempChoice.getRandom(1,3); //generates a random number choice from 1 - 3 inclusive
	string tempName = "Enemy";

	switch (enemyChoice)
	{
	case 1:
		b.setUp(tempName, 100, 5, 15);
		break;
	case 2:
		b.setUp(tempName, 100, 15, 5);
		break;
	case 3:
		b.setUp(tempName, 100, 10, 10);
		break;
	}

}
