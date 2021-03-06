// Lab 7.cpp : Defines the entry point for the console application.
//Kody Johnson 
//CS 201 L - 002
/* Read in a .txt file and count the instances of each unique word and print out the results */

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include "Word.h"

using namespace std;

void resizeArray(Word *&w, int &s);

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int size = 10;
	Word *words;
	string thing;
	words = new Word [size];
	int numOfElements = 0;
	bool wordInArray = false; //bool statement for me to keep track if the array already conatains an element

	//Checks if the input file is valid
	if (!fin)
	{
		cout << "Error opening input file" << endl;
		return 1;
	}

	//Main loop through the input file 
	while(fin >> thing)
	{
		Word checkWord; //creates a word object to start the checking process
		checkWord.setWord(thing);

		//Checks to see if the word is in the array, if it is, then the word (objects) count is incremented()
		for (int i = 0; i < numOfElements; i++)
		{
			if(words[i].getWord() == thing) //checkWord.getWord())
			{
				words[i].increment();
				wordInArray = true;
				break;
			}
		}
		//Places the new element into the words[] if it does not already exist
		if (wordInArray == false)
		{
			words[numOfElements] = checkWord;
			words[numOfElements].increment();
			numOfElements += 1;
		}
		wordInArray = false;
		
		if (numOfElements == size)
			resizeArray(words, size);
	}


	//Beginning to output
	fout << "Words found: " << numOfElements << endl;
	fout << "Array’s max size:  " << size << endl;
	for (int i = 0; i < numOfElements; i++)
	{
		fout << words[i].getWord() << " - " << words[i].getCount() << endl;
	}

    return 0;

}

// Takes *words[], passes it by refrence, doubles the size and copies the contents of the old array into the resized one
//then delets the old contents;
void resizeArray(Word *&w, int &s)
{		
	
	Word *resized = new Word [s * 2];
	for (int i = 0; i < s; i++)
		resized[i] = w[i];

	s = s * 2;
	delete [] w;
	w = resized;
}