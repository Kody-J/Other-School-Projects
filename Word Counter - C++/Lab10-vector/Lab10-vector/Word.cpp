#include "stdafx.h"
#include "Word.h"

// Your name
// Today's date
// Lab 9

#include "Word.h"

// Default constructor; needed for array creation
Word::Word()
{
	word = "";
	count = 0;
}

// Constructor to store the word with it
Word::Word(string theWord)
{
	word = theWord;
	count = 0;
}

// Returns the word stored
string Word::getWord()
{
	return word;
}

// Returns the count stored
int Word::getCount()
{
	return count;
}

// Increments the counter
void Word::increment()
{
	count++;
}

// Sets a new word to the object
void Word::setWord(string theWord)
{
	word = theWord;
}

// Sets the count to a value
void Word::setCount(int theCount)
{
	count = theCount;
}