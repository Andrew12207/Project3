#include <QApplication>
#include <QMessageBox>
#include "GUIWindow.h"

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    try {
        GUIWindow window;
        window.show();
        return app.exec(); 
    } catch (const std::exception &ex) {
        QMessageBox::critical(nullptr, "Fatal error", ex.what());
        return EXIT_FAILURE;
    }
}
