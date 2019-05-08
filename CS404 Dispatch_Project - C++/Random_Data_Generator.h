#pragma once

/*
This class serves to generate the random data necessary to create :
1 ---> A random list of emergency calls for the dispatcher to recieve
2 ---> A random Emergency Vehicle
*/

#include <random>
#include <string>
#include <vector>
using namespace std;

class Random_Data_Generator
{
private:

	int call_count;
	int zip;
	int type;

	int distance;


public:

	Random_Data_Generator() : call_count(0), zip(getRan_zip()), type(getRan_type()) {};

	int getRan_distance();
	int getRan_zip();
	int getRan_type();
	int getZip();
	int getType();


};

