# include <iostream>
#include <string>
#include <unordered_map>
// #include "MergeSort.h"
#include "ItemMap.h"
#include "LinkedList.h"
#include "QuickSort.h"

using namespace std;

int main() {
    unordered_map<string, int> products;
    createMap(products);
    int id = getID(products, "NoodleNook Sugar Granulated 1lb");
    cout << id << endl;


    LinkedList unorderedList;
    
    // Load data from CSV file
    if (loadCSVToLinkedList(unorderedList)) {
        std::cout << "Data loaded successfully!" << std::endl;
    }

    Node* unorderedHead = unorderedList.getHead();

    QuickSort sort;
    sort.quickSort(unorderedHead);
    return 0;
}