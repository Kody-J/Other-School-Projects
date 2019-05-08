#pragma once
#include <string>
#include <iostream>

using namespace std;


class User
{
public:
	User();
	User(int id, string fn, string ln);
	User(const User& rhs);
	int getIdNumber()const;
	string getFirstName() const;
	string getLastName() const;
	string getFullName() const;
	void setIDNumber(int NewNumber);
	void setFirstName(string fn);
	void setLastName(string ln);
	int checkOutCount() const;
	bool checkOut(const string BookIDCode);
	bool checkIn(const string& BookIDCode);
	bool hasCheckedOut(const string& BookIDCode) const;
	void clear();
	friend istream& operator >> (istream& in, User& item);
	friend ostream& operator<<(ostream& out, const User& item);
	const User operator+(const string item);
	void operator+=(const string BookIDCode);
	bool operator==(const User& U2);
	bool operator!=(const User& U2);
	int searchForBook(string bkID);
	~User();

private:
	bool reSizeArray();
	string *checkedOutArray;
	string firstName, lastName;
	int userIDNumber, booksCheckedOut, arraySize;


};

