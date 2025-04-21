#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

struct Node {
    // Node defintion
    int id;
    std::string name;
    std::string store;
    float price;
    Node* next;
    
    // Constructor
    Node(int _id, std::string _name, std::string _store, float _price) : 
        id(_id), name(_name), store(_store), price(_price), next(nullptr) {}
};

class LinkedList {
private:
    Node* head;
    
public:
    // Constructor
    LinkedList() : head(nullptr) {}
    
    // Destructor
    ~LinkedList() {
        Node* current = head;
        while (current != nullptr) {
            Node* temp = current;
            current = current->next;
            delete temp;
        }
    }
    
    // Insert a new node at the beginning of the list
    void insert(int id, std::string name, std::string store, float price) {
        Node* newNode = new Node(id, name, store, price);
        newNode->next = head;
        head = newNode;
    }

    void display() {
        Node* current = head;
        while (current != nullptr) {
            std::cout << "ID: " << current->id 
                      << ", Name: " << current->name 
                      << ", Store: " << current->store 
                      << ", Price: $" << current->price << std::endl;
            current = current->next;
        }
    }
    
    // Search for a node by ID
    std::string search(int id) {
        Node* current = head;
        while (current != nullptr) {
            if (current->id == id) {
                std::string foundName = current->name; // Return the name if found
                return foundName; // Return the name if found
            }
            current = current->next;
        }
        return ""; // Changed from nullptr to empty string for string return type
    }
};

// Loading data into linked list from csv
bool loadCSVToLinkedList(const std::string& filename, LinkedList& list) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Error opening file: " << filename << std::endl;
        return false;
    }
    
    std::string line;
    // Skip header
    std::getline(file, line);
    
    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::string idStr, name, store, priceStr;
        
        if (std::getline(ss, idStr, ',') && 
            std::getline(ss, name, ',') && 
            std::getline(ss, store, ',') && 
            std::getline(ss, priceStr)) {
            
            // Convert id string to int
            int id;
            float price;
            try {
                id = std::stoi(idStr);
                price = std::stof(priceStr);
            } catch (const std::exception& e) {
                std::cerr << "Error converting ID to integer: " << idStr << std::endl;
                continue;
            }
            
            // Insert into linked list
            list.insert(id, name, store, price);
        }
    }
    
    file.close();
    return true;
}

int main() {
    LinkedList myList;
    
    // Load data from CSV file
    if (loadCSVToLinkedList("C:/Users/aiden/OneDrive/Documents/GitHub/New folder/product_list.csv", myList)) {
        std::cout << "Data loaded successfully!" << std::endl;
        myList.display();
    }
    
    return 0;
}