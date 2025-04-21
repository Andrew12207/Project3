#pragma once
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

unordered_map<string, int> loadProducts(const string& csvPath) {
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

int getID(const string& name) {
    string CSV = "unique_products.csv";
    unordered_map<string, int> products;
    products = loadProducts(CSV);

    auto it = products.find(name);
    if (it != products.end()) {
        int id = it->second;
        return id;
    } else {
        return 0;
    }
}