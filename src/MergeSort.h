#pragma once
#include <iostream>
#include <string>
#include <chrono>

struct Node {
    int id;
    std::string name;
    std::string store;
    float price;
    Node* next;
    
    // Constructor
    Node(int _id, std::string _name, std::string _store, float _price) : 
        id(_id), name(_name), store(_store), price(_price), next(nullptr) {}
};

class MergeSort {
public:

    static Node* mergeSort(Node* head);
    
private:

    static void splitList(Node* head, Node** frontRef, Node** backRef);
    static Node* mergeLists(Node* a, Node* b);
};