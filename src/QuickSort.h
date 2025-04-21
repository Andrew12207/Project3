#pragma once
#include "LinkedList.h"

// Node already defined in LinkedList.h
struct Node;

struct QuickSort {
public:
    void quickSort(Node*& head) {
        head = quickSortRecur(head, getTail(head));
    }

private:
    // Return the last node of a sub-list
    static Node* getTail(Node* cur) {
        while (cur && cur->next) {
            cur = cur->next;
        }
        return cur;
    }

    // Partitions the list with a pivot point at the end node
    static Node* partition(Node* head, Node* end, Node*& newHead, Node*& newEnd) {
        Node* pivot = end;
        Node* prev = nullptr;
        Node* cur = head;
        Node* tail = pivot;

        while (cur != pivot) {
            if (cur->id < pivot->id) {
                if (!newHead) newHead = cur;
                prev = cur;
                cur = cur->next;
            } else {
                if (prev) {
                    prev->next = cur->next;
                    Node* temp = cur->next;
                    cur->next = nullptr;
                    tail->next = cur;
                    tail = cur;
                    cur = temp;
                }
            }
        }

        if (!newHead) {
            newHead = cur;
        }
        newEnd = tail;
        return pivot;
    }

    static Node* quickSortRecur(Node* head, Node* end) {
        if (!head || head == end) {
            return head;
        }

        Node* newHead = nullptr;
        Node* newEnd = nullptr;
        Node* pivot = partition(head, end, newHead, newEnd);

        // Sort left Half
        if (newHead != pivot) {
            Node* temp = newHead;
            while (temp->next != pivot) {
                temp = temp->next;
            }

            // detatch this sub-list
            temp->next = nullptr;

            newHead = quickSortRecur(newHead, temp);

            temp = getTail(newHead);

            // re-attach pivot
            temp->next = pivot;
        }

        // Sort right half
        pivot->next = quickSortRecur(pivot->next, newEnd);

        return newHead;
    }
};