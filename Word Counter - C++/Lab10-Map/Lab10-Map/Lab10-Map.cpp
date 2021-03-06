// Lab10-Map.cpp : Defines the entry point for the console application.
/*
  Kody Johnson
  11/09/2017
  Lab 10: Reads in a .txt file and counts all instances of a unique word or character and displays the infomation

*/

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <map>

using namespace std;

// Starting point
int main()
{
	// File I/O
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	if (!fin.good())
	{
		cout << "Could not open this file!" << endl;
		system("pause");
		return -1;
	}

	// Read in file
	string wordIn;

	map<string, int> words;
	// While there are more words
	while (fin >> wordIn)
	{
		// If not found, add it. If array is full, resize it first.
		words[wordIn] += 1;
	}


	// Print list of words and counts

	fout << "Words found: " << words.size() << endl;

	// For each word, print it's word/count pair.
 	for (map<string, int>::iterator itr = words.begin(); itr != words.end(); itr ++)
	{
		fout << itr->first << " - " << itr->second << endl;
	}
}
