//Kody Johnson 
//CS 201 L - 002
//Lab 7

#include "stdafx.h"
#include "Word.h"

//Defaults the word var to empty string and count to 0
Word::Word()
{
	word = "";
	count = 0;
}

//increments the count by one
void Word::increment()
{
	count += 1;
}


//returns the value of count
int Word::getCount()
{
	return count;
}

//returns the value of word
string Word::getWord()
{
	return word;
}

// sets the var word to whatever is passed
void Word::setWord(string w)
{
	word = w;
}

//sets the var count to whatever int is passed to it
void Word::setCount(int c)
{
	count = c;
}


