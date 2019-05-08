#include "stdafx.h"
#include "User.h"
#include <string>

using namespace std;

//Initilizes IDnumber, First and Last Name 
User::User()
{
	userIDNumber = 0;
	firstName = "";
	lastName = "";

}

//Overloads for user ID, firs and last name
User::User(int id, string fn, string ln)
{
	userIDNumber = id;
	firstName = fn;
	lastName = ln;
}

//Copies a existing object to a new object
User::User(const User& rhs)
{
	userIDNumber = rhs.userIDNumber;
	lastName = rhs.lastName;
	firstName = rhs.firstName;
	arraySize = rhs.arraySize;
	booksCheckedOut = rhs.booksCheckedOut;
	checkedOutArray = new string[arraySize];
	for (int i = 0; i < booksCheckedOut; i++)//Itterates thrugh array contents and transfers thmem to the LHS
		checkedOutArray[i] = rhs.checkedOutArray[i];

}

int User::getIdNumber() const
{
	return userIDNumber;
}

string User::getFirstName() const
{
	return firstName;
}

string User::getLastName() const
{
	return lastName;
}
//Returns LastName, Firstnanme
string User::getFullName() const
{
	string fullName = lastName + ", " + firstName;
	return fullName;
}

void User::setIDNumber(int newNumber)
{
	if (100 <= newNumber && newNumber < 1000000)
		userIDNumber = newNumber;

}

void User::setFirstName(string fn)
{
	firstName = fn;
}

void User::setLastName(string ln)
{
	lastName = ln;
}

int User::checkOutCount() const
{
	return booksCheckedOut;
}
//Takes in a BookID string and checks to see if its in the checkout array alrady, if it isnt, adds it to the checkedOutArray
//Also calls resize() if the array is full, and will create an array of [5] if the user has no books checked out
bool User::checkOut(const string BookIDCode)
{
	if (hasCheckedOut(BookIDCode) == true)
		return false;
	else if (arraySize == booksCheckedOut && arraySize > 0)// resizes if the array is full, onlyif the array is alrady > 0
	{
		reSizeArray();
		checkedOutArray[booksCheckedOut] = BookIDCode;
		booksCheckedOut += 1;
		return true;
	}
	else if (arraySize == 0) //If the array is empty then crates a small araay for 5 books to begin with
	{
		arraySize = 5;
		checkedOutArray = new string[arraySize];
		checkedOutArray[booksCheckedOut] = BookIDCode;
		booksCheckedOut += 1;
		return true;
	}
	else//adds the new book to the checked out array
	{
		checkedOutArray[booksCheckedOut] = BookIDCode;
		booksCheckedOut += 1;
		return true;
	
	}
}
//Searches for the given book in the checked out array, if the book is found then the book is removed from the array
//if the array becomes epty then it is deleted
bool User::checkIn(const string & BookIDCode)
{
	if (hasCheckedOut(BookIDCode) == false)//returns false if book is not found
		return false;
	else if (booksCheckedOut == 0)//delets array if it becomes empty after checking out
	{
		delete [] checkedOutArray;
		checkedOutArray = nullptr;
		return true;
	}
	else
	{
		string *tempArray = new string [arraySize];//coppies the array of checked out books minus the one being checked in and updates the # of books checked out
		int objectCounter = 0;
		for (int i = 0; i < arraySize; i++)
		{
			if (checkedOutArray[i] != BookIDCode)
			{
				tempArray[objectCounter] = checkedOutArray[i];
				objectCounter += 1;
			}
		}
		booksCheckedOut -= 1;
		delete [] checkedOutArray;
		checkedOutArray = tempArray;
		return true;
	}
}
//Itterates through the checkedOutArray to find if a book is checked out
bool User::hasCheckedOut(const string & BookIDCode) const
{
	if(booksCheckedOut > 0)
		for (int i = 0; i < booksCheckedOut; i++)
			if (checkedOutArray[i] == BookIDCode)
			return true;
	return false;
}
//Clears the conents of a user object
void User::clear()
{
	userIDNumber = 0;
	firstName = "";
	lastName = "";
	booksCheckedOut = 0;
	arraySize = 0;

}
//adds the contents of the RHS to the LHS (returnung a different object)
const User User::operator+(const string item)
{
	User tempUser;
	tempUser.firstName = firstName;
	tempUser.lastName = lastName;
	tempUser.userIDNumber = userIDNumber;
	tempUser.booksCheckedOut = booksCheckedOut;
	tempUser.arraySize = arraySize;
	tempUser.checkedOutArray = new string[arraySize + 1];
	if (tempUser.booksCheckedOut > 0)
	{
		for (int i = 0; i < booksCheckedOut; i++)
			tempUser.checkedOutArray[i] = checkedOutArray[i];
	}
	delete[] checkedOutArray;
	tempUser.checkOut(item);
	return tempUser;
}

void User::operator+=(const string BookIDCode)
{
	checkOut(BookIDCode);
}

bool User::operator==(const User & U2)
{
	if (userIDNumber == U2.userIDNumber)
		return true;
	return false;
}

bool User::operator!=(const User & U2)
{
	if(userIDNumber != U2.userIDNumber)
		return true;
	return false;
}

int User::searchForBook(string bkID)
{
	if (booksCheckedOut == 0)
		return -1;
	else
		for (int i = 0; i < booksCheckedOut; i++)
		{
			if (checkedOutArray[i] == bkID)
				return i;
		}
	return -1;
}
//resizes array when needed by doubling it (copies into a temp array first then sets LHS array = tho the temp array)
bool User::reSizeArray()
{
	string *resized = new string[arraySize * 2];
	for (int i = 0; i < arraySize; i++)
		resized[i] = checkedOutArray[i];

	arraySize *= 2;
	delete[] checkedOutArray;
	checkedOutArray = resized;
	return true;
}


istream & operator>>(istream & in, User & item)
{

	item.clear();
	in >> item.userIDNumber >> item.firstName >> item.lastName >> item.arraySize;
	if (item.arraySize > 0)
	{
		item.checkedOutArray = new string[item.arraySize];
		for (int i = 0; i < item.arraySize; i++)
		{
			string tempBook;
			in >> tempBook;
			item.checkOut(tempBook);
		}
	}

	return in;
}

ostream & operator<<(ostream & out, const User & item)
{
	out << item.userIDNumber << " " << item.firstName << " " << item.lastName << endl;
	out << item.booksCheckedOut << endl;
	if (item.booksCheckedOut > 0)
	{
		for (int i = 0; i < item.booksCheckedOut; i++)
			out << item.checkedOutArray[i] << endl;
	}
	return out;
}


User::~User()
{
}
