#include "Random_Data_Generator.h"


int Random_Data_Generator::getRan_distance()
{
	random_device rd;
	mt19937 eng(rd());
	uniform_int_distribution<> distr(1, 10);

	return distr(eng);
}

int Random_Data_Generator::getRan_zip()
{
	random_device rd;
	mt19937 eng(rd());
	uniform_int_distribution<> distr(64141, 64161);

	return distr(eng);
}

int Random_Data_Generator::getRan_type()
{
	random_device rd;
	mt19937 eng(rd());
	uniform_int_distribution<> distr(1, 3);

	return distr(eng);
}

int Random_Data_Generator::getZip()
{
	return zip;
}

int Random_Data_Generator::getType()
{
	return type;
}