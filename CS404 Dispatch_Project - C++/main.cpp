/*
This is our solution for the Emergency Vehicle Dispatcher Project

IMPORTANT DETAILS:
1) The relationship between neighboring ZipCodes is provided in the edges.txt file
2) The Emergency Vehicles are created randomly and are placed according to their random ZipCode (The number of vehicles is easily manipulated)
3) The number of Emergency Calls is also a variable which is easily manipulated about the actual Running portion of the program

*/




#include <iostream>
#include<fstream>
#include<string>
#include <map>
#include<queue>
#include<vector>
#include "Dispatcher.h"
#include "Vehicle.h"
#include "Graph.h"
#include"Edge.h"

using namespace std;

int main()
{
	//Initializing all our Class objects and some/most data structures
	Random_Data_Generator helper;
	Graph g;
	Dispatcher tester;
	ifstream fin;
	fin.open("edges.txt");
	Vehicle vehicle_handle;
	vehicle_handle.generate_E_vec(64141, 64161, 45);
	int start = 64141;
	int first_zip = start;
	int end = 64161;
	vector<Vertix> vertices; // Will store all our vertices
	vector<Vehicle> vehicles_vec = vehicle_handle.getVehicle_vec(); // Just the list of random Emergency vehicles

  //creates vertices based on our zip codes (start & finish) more reusable
	for (int i = 0; i < (end - start) + 1; i++) {
		vertices.push_back(first_zip);
		first_zip++;
	}

	//We created random vehicle objects, this places those vehicles into their respective vertix based on ZipCode
	for (unsigned int a = 0; a < vehicles_vec.size(); a++)
		vertices[vehicles_vec[a].get_zipcode() % start].set_vehicles(vehicles_vec[a]);

	//Once our Vertix objects have their vectors of vehicles filled, this uplaods the verticies into our graph
	for (unsigned int b = 0; b < vertices.size(); b++)
		g.addVertix(vertices[b]);

	//Just goes through the headers and discards them
	string header_filter;
	fin >> header_filter;
	fin >> header_filter;
	fin >> header_filter;

	//Reads in the file and builds our graph
	int source, destination, weight;
	while (fin >> source)
	{
		fin >> destination;
		fin >> weight;
		g.addEdge(source,destination, weight);
		g.addEdge(destination, source, weight);

	}

	//Used to generate random emergency calls
	int Emergency_type;
	int Emergency_zip;
	int Emergency_id;
	

	//This is the actual begenning of the program
	int num_of_emergencies = 5;
	for (int i = 0; i < num_of_emergencies; i++)
	{
		//GENERATING RANDOM EMERGENCY
		Edge the_one_needed;
		Emergency_type = helper.getRan_type();
		Emergency_zip = helper.getRan_zip();
		Emergency_id = i + 1;


		Vehicle response_vehicle;
		int distance_tracker = 0;
		vector<int> sorted_paths;


		//Keeps track of the ZipCode with the most recent shortest path
		int first_found = 0;
		distance_tracker = 0;

		//Check the graph at the specific location of the emergency
		if (g.get_vertix()[Emergency_zip % start].getVehicles()[Emergency_type - 1].size() > 0) {
			response_vehicle = g.get_vertix()[Emergency_zip % start].getVehicles()[Emergency_type - 1].back();
			g.get_vertix()[Emergency_zip % start].remove_vehicle(response_vehicle.get_type()-1);
		}

		//Based on the Emergency Zip Code sort the adjacent ZipCodes by shortest distance
		if(response_vehicle.get_id() == -1)
			sorted_paths = tester.shortest_path_vec(Emergency_zip, g);


		while (response_vehicle.get_id() == -1) {
			first_found = 0;
			for (unsigned int j = 0; j < sorted_paths.size(); j++) {
				//If the vector at index j isn't zero then there is a ZipCode to check 
				if (sorted_paths[j] != 0) {

					if (first_found == 0)
						first_found = sorted_paths[j];

					//Used to shorten lengthy command calls
					vector<Vertix>  tempVec = g.get_vertix();
					Vertix specific_vertix = tempVec[sorted_paths[j] % start];
					vector<vector<Vehicle>> vehicle_list_handle = specific_vertix.getVehicles();
					vector<Vehicle> specific_vehicles = vehicle_list_handle[Emergency_type - 1];

					if (specific_vehicles.size() > 0) {
						response_vehicle = g.get_vertix()[sorted_paths[j] % start].getVehicles()[Emergency_type - 1].back();
						g.find_edge(sorted_paths[j], Emergency_zip, the_one_needed);
						if(the_one_needed.get_dest() >= 0)
							distance_tracker += the_one_needed.get_dest();
						g.get_vertix()[sorted_paths[j] % start].remove_vehicle(response_vehicle.get_type() -1);
						break;
					}

				}
			}

			if (response_vehicle.get_type() == -1) {
				g.find_edge(first_found, Emergency_zip, the_one_needed);
				if (the_one_needed.get_dest() >= 0)
					distance_tracker += the_one_needed.get_dest();
				tester.sortest_path_again(first_found, g, sorted_paths, Emergency_zip, the_one_needed.get_dest());
			}
		}


		cout << "The emergency at Zipcode: " << Emergency_zip << " Was responed to by; " <<  endl;
		cout << "Vehicle ID --> " << response_vehicle.get_id() << " Type --> " << response_vehicle.get_type() << " ZipCode --> " << response_vehicle.get_zipcode() << " Distance " << distance_tracker << "\n" << endl;
		response_vehicle.reset_vehicle();

		getchar();
	}
	return 0;
}
