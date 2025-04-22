#pragma once
#include <iostream>
#include <string>
#include "LinkedList.h"

class ShellSort {
public:
    static Node* shellSort(Node* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }
        
        int length = getLength(head);
        
        // Convert linked list to array for easier shell sort
        Node** nodeArray = new Node*[length];
        Node* current = head;
        for (int i = 0; i < length; i++) {
            nodeArray[i] = current;
            current = current->next;
        }
        
        // Shell sort using gap sequence
        for (int gap = length/2; gap > 0; gap /= 2) {
            for (int i = gap; i < length; i++) {
                Node* temp = nodeArray[i];
                int j;
                
                for (j = i; j >= gap && nodeArray[j - gap]->id > temp->id; j -= gap) {
                    nodeArray[j] = nodeArray[j - gap];
                }
                
                nodeArray[j] = temp;
            }
        }
        
        // reconstruct the list
        for (int i = 0; i < length - 1; i++) {
            nodeArray[i]->next = nodeArray[i + 1];
        }
        nodeArray[length - 1]->next = nullptr;
        
        head = nodeArray[0];
        
        delete[] nodeArray;
        std::cout << "Shell sort completed" << std::endl;
        
        return head;
    }
    
private:
    static int getLength(Node* head) {
        int length = 0;
        Node* current = head;
        while (current) {
            length++;
            current = current->next;
        }
        return length;
    }
};