#pragma once
// Your name
// Today's date
// Lab 9

#include <string>
using namespace std;

// Class to store a Word object
class Word
{
private:
	// Word that was found
	string word;
	// Number of times a word has been found
	int count;

public:
	// Default constructor; needed for array creation
	Word();
	// Constructor to store the word with it
	Word(string theWord);

	// Returns the word stored
	string getWord();
	// Returns the count stored
	int getCount();
	// Increments the counter
	void increment();

	// Sets a new word to the object
	void setWord(string theWord);
	// Sets the count to a value
	void setCount(int theCount);
};