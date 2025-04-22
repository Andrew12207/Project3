#pragma once
#include <iostream>
#include <string>
#include "LinkedList.h"

class MergeSort {
public:
    static Node* mergeSort(Node* head) {
        // check if list is empty or has only one element
        if (head == nullptr || head->next == nullptr) {
            return head;
        }
        
        int size = 1;
        Node* current = head;
        int totalLength = getLength(head);  // Get total length of the list
        
        Node dummy(0, "", "", 0.0);
        dummy.next = head;
        
        // start merge sort from bottom up
        while (size < totalLength) {
            Node* tail = &dummy; 
            current = dummy.next; 
            
            // Merge subarrays of current size
            while (current) {
                Node* left = current;
                Node* right = split(left, size);
                current = split(right, size);
                tail = merge(left, right, tail);
            }
            
            size *= 2;
        }
        std::cout << "Merge sort completed" << std::endl;
        
        return dummy.next;
    }
    
private:
    // Calculate the length of the linked list
    static int getLength(Node* head) {
        int length = 0;
        Node* current = head;
        while (current) {
            length++;
            current = current->next;
        }
        return length;
    }
    
    // Split the list into two parts after n nodes
    static Node* split(Node* head, int n) {
        if (!head) return nullptr;
        
        for (int i = 1; head && i < n; i++) {
            head = head->next;
        }
        
        if (!head) return nullptr;
        
        // break the list and return the second part
        Node* second = head->next;
        head->next = nullptr;
        return second;
    }
    
    // attach two merged sorted lists to tail
    static Node* merge(Node* left, Node* right, Node* tail) {
        while (left && right) {
            if (left->id <= right->id) {
                tail->next = left;
                left = left->next;
            } else {
                tail->next = right;
                right = right->next;
            }
            tail = tail->next;
        }
        
        tail->next = (left) ? left : right;
        
        // Move tail to the end of the merged list
        while (tail->next) {
            tail = tail->next;
        }
        
        return tail;
    }
};