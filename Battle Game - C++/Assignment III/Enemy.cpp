//Kody Johnson
//Program III
//CS 201R - 002

#include "stdafx.h"
#include "Enemy.h"
#include <cstdlib>


Enemy::Enemy()
{
}

void Enemy::selectAction()
{
	int enemyChoice = rand() % 2 + 1;
	if (enemyChoice = '1')  // Settig the _attackType based on valid user input
		_attackType = offensive;
	else
		_attackType = defensive;
}

