#pragma once

#include <QMainWindow>
#include <QLineEdit>
#include <QPushButton>
#include <QComboBox>
#include <QLabel>
#include <QTextEdit>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QGroupBox>
#include <QMessageBox>
#include <chrono>
#include "ItemMap.h"
#include "LinkedList.h"
#include "MergeSort.h"
#include "ShellSort.h"

class GUIWindow : public QMainWindow {
    Q_OBJECT

public:
    GUIWindow(QWidget *parent = nullptr);
    ~GUIWindow();

private slots:
    void onSearchClicked();

private:
    QLineEdit* productInput;
    QPushButton* searchButton;
    QComboBox* sortMethodDropdown;
    QLabel* timeTakenLabel;
    QTextEdit* pricesDisplay;
    
    unordered_map<string, int> products;
    LinkedList productList;
    
    void setupUI();
    void loadData();
    void displayResults(int productId, Node* head);
    std::string formatNode(Node* node);
};