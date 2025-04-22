#pragma once
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

// Mapping item name to ID
inline unordered_map<string, int> loadProducts(const string& csvPath) {
    ifstream CSV(csvPath);
    if (!CSV.is_open()) {
        throw runtime_error("Could not open " + csvPath);
    }

    unordered_map<string, int> products;
    products.reserve(25000);
    string line;
    getline(CSV, line);
    while (getline(CSV, line)) {
        size_t commaPos = line.find(',');
        if (commaPos == string::npos) {
            continue;
        }
        
        int id = stoi(line.substr(0, commaPos));
        string name = line.substr(commaPos + 1);

        products.emplace(move(name), id);
    }
    return products;
}

inline void createMap(unordered_map<string, int>& products) {
    string CSV = "unique_products.csv";
    products = loadProducts(CSV);
}
    

inline int getID(unordered_map<string, int>& products, const string& name) {
    cout << "Searching for: " << name << endl;
    auto it = products.find(name);
    if (it != products.end()) {
        int id = it->second;
        cout << "Found product ID: " << id << endl;
        return id;
    } else {
        cout << "Product not found" << endl;
        return 0;
    }
}