# include <iostream>
#include <string>
#include <unordered_map>
#include "MergeSort.h"
#include "ItemMap.h"

using namespace std;

int main() {
    unordered_map<string, int> products;
    createMap(products);
    int id = getID(products, "NoodleNook Sugar Granulated 1lb");
    cout << id << endl;
    return 0;
}