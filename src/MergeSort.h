#pragma once
#include <iostream>
#include <string>
#include "LinkedList.h"

struct Node;

class MergeSort {
public:
    static Node* mergeSort(Node* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }
        
        Node* front = nullptr;
        Node* back = nullptr;
        
        splitList(head, &front, &back);
        
        front = mergeSort(front);
        back = mergeSort(back);
        
        return mergeLists(front, back);
    }
    
private:
    static void splitList(Node* head, Node** frontRef, Node** backRef) {
        if (head == nullptr || head->next == nullptr) {
            *frontRef = head;
            *backRef = nullptr;
            return;
        }
        
        Node* slow = head;
        Node* fast = head->next;
        
        while (fast != nullptr) {
            fast = fast->next;
            if (fast != nullptr) {
                slow = slow->next;
                fast = fast->next;
            }
        }
        
        *frontRef = head;
        *backRef = slow->next;
        slow->next = nullptr;
    }
    
    static Node* mergeLists(Node* a, Node* b) {
        if (a == nullptr) return b;
        if (b == nullptr) return a;
        
        Node* result = nullptr;
        
        if (a->id <= b->id) {
            result = a;
            result->next = mergeLists(a->next, b);
        } else {
            result = b;
            result->next = mergeLists(a, b->next);
        }
        
        return result;
    }
};