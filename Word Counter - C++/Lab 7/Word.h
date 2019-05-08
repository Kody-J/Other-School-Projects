//Kody Johnson
//CS 201l - 002
//Lab7

#pragma once
#include <string>
using namespace std;


class Word
{
public:
	Word();
	void increment();
	int getCount();
	string getWord();
	void setWord(string w);
	void setCount(int c);

private:
	string word;
	int count;

};

