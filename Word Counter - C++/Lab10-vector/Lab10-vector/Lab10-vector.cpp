// Lab10-vector.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
// Your name
// Today's date
// Lab 9

#include "Word.h"
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Starting point
int main()
{
	// File I/O
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	// vector for Words
	vector <Word> vec;

	// Read in file
	string wordIn;
	// While there are more words
	while (fin >> wordIn)
	{
		// It's not found by default
		bool found = false;

		// For each element in the array, if it exists, increment its count, and mark it as found
		for (vector<Word>::iterator iter = vec.begin(); iter != vec.end(); iter++)
		{
			if (iter->getWord() == wordIn)
			{
				iter->increment();
				found = true;
				// Quit for loop early
				break;
			}
		}

		// If not found, add it. If array is full, resize it first.
		if (!found)
		{
			vec.push_back(wordIn);
			vec[vec.size() - 1].increment();
		}
	}

	// Print list of words and counts

	fout << "Words found: " << vec.size() << endl;

	// For each word, print it's word/count pair.
	for (int i = 0; i < vec.size(); i++)
	{
		fout << vec[i].getWord() << " - " << vec[i].getCount() << endl;
	}
}
