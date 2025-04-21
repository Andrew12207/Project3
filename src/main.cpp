# include <iostream>
#include <string>
#include <unordered_map>
#include "MergeSort.h"
#include "ItemMap.h"
#include "LinkedList.h"

using namespace std;

int main() {
    unordered_map<string, int> products;
    createMap(products);
    int id = getID(products, "NoodleNook Sugar Granulated 1lb");
    cout << id << endl;


    LinkedList myList;
    
    // Load data from CSV file
    if (loadCSVToLinkedList(myList)) {
        std::cout << "Data loaded successfully!" << std::endl;
    }

    return 0;
}