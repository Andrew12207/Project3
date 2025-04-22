#include "GUIWindow.h"
#include <sstream>
#include <iomanip>

GUIWindow::GUIWindow(QWidget *parent)
    : QMainWindow(parent)
{
    setWindowTitle("Product Price Lookup");
    resize(800, 500);
    
    setupUI();
    loadData();
}

GUIWindow::~GUIWindow() {}

void GUIWindow::setupUI() {
    // Setting up window
    QWidget* centralWidget = new QWidget(this);
    QHBoxLayout* mainLayout = new QHBoxLayout(centralWidget);
    QGroupBox* pricesGroup = new QGroupBox("Prices", centralWidget);
    QVBoxLayout* pricesLayout = new QVBoxLayout(pricesGroup);
    pricesDisplay = new QTextEdit(pricesGroup);
    pricesDisplay->setReadOnly(true);
    pricesLayout->addWidget(pricesDisplay);
    // setting up searching buttons
    QGroupBox* controlsGroup = new QGroupBox("Search", centralWidget);
    QVBoxLayout* controlsLayout = new QVBoxLayout(controlsGroup);
    QHBoxLayout* searchLayout = new QHBoxLayout();
    productInput = new QLineEdit(controlsGroup);
    productInput->setPlaceholderText("Enter product");
    searchButton = new QPushButton("→", controlsGroup);
    searchLayout->addWidget(productInput);
    searchLayout->addWidget(searchButton);
    
    // Sort method dropdown/combobox
    sortMethodDropdown = new QComboBox(controlsGroup);
    sortMethodDropdown->addItem("Merge Sort");
    sortMethodDropdown->addItem("Shell Sort");
    timeTakenLabel = new QLabel("Time taken to sort: ---μs", controlsGroup);
    
    controlsLayout->addLayout(searchLayout);
    controlsLayout->addWidget(sortMethodDropdown);
    controlsLayout->addWidget(timeTakenLabel);
    controlsLayout->addStretch();
    
    // setting price box to take up the left 2/3 of window, search controls will take up right 1/3
    mainLayout->addWidget(pricesGroup, 2);  
    mainLayout->addWidget(controlsGroup, 1);
    
    setCentralWidget(centralWidget);
    connect(searchButton, &QPushButton::clicked, this, &GUIWindow::onSearchClicked);
    connect(productInput, &QLineEdit::returnPressed, this, &GUIWindow::onSearchClicked);
}

void GUIWindow::loadData() {
    // Load name/id map + linked list
    createMap(products);
}

void GUIWindow::onSearchClicked() {
    std::string productName = productInput->text().toStdString();
    int productId = getID(products, productName);
    
    if (productId == 0) {
        QMessageBox::warning(this, "Product Not Found", 
                           "The product name you entered does not match any existing product names");
        return;
    }
    loadCSVToLinkedList(productList);
    
    auto start = std::chrono::high_resolution_clock::now();
    
    Node* head = productList.getHead();
    
    if (sortMethodDropdown->currentText() == "Merge Sort") {
        std::cout << "Using Merge Sort" << std::endl;
        head = MergeSort::mergeSort(head);
    } else {
        std::cout << "Using Shell Sort" << std::endl;
        head = ShellSort::shellSort(head);
    }
    
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    timeTakenLabel->setText(QString("Time taken to sort: %1μs").arg(duration.count()));
    

    displayResults(productId, head);
}

void GUIWindow::displayResults(int productId, Node* head) {
    // Clear previous results if necessary
    pricesDisplay->clear();

    std::cout << "Displaying results for product ID: " << productId << std::endl;
    // Linear search through the sorted linked list
    //Node* current = productList.getHead();
    std::stringstream results;

    Node* current = head;
    while (current != nullptr) {
        if (current->id == productId) {
            std::cout << "Found matching product: " << current->name << std::endl;
            results << formatNode(current) << "\n\n";
        }
        current = current->next;
    }
    std::cout << "Results found:\n" << results.str() << std::endl;
    // Display results
    pricesDisplay->setText(QString::fromStdString(results.str()));
}

std::string GUIWindow::formatNode(Node* node) {
    std::stringstream ss;
    ss << "Product: " << node->name << "\n"
       << "Store: " << node->store << "\n"
       << "Price: $" << std::fixed << std::setprecision(2) << node->price;
    return ss.str();
}