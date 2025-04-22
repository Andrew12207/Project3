cmake_minimum_required(VERSION 3.16.3)
project(Project3)

set(CMAKE_PREFIX_PATH
    "C:/Qt/6.9.0/mingw_64/lib/cmake"
    CACHE PATH "Where to find Qt5Config.cmake"
)

set(CMAKE_CXX_STANDARD 14)

#compile flags to match Gradescope test environment
set(GCC_COVERAGE_COMPILE_FLAGS "-Wall -Werror") # remove -Wall if you don't want as many warnings treated as errors
# gradescope does use -Werror, so if you remove it here you may run into issues when trying to submit
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${GCC_COVERAGE_COMPILE_FLAGS}" )

find_package(Qt6 REQUIRED COMPONENTS Widgets)

include_directories(src)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

add_executable(Main
        src/main.cpp src/GUIWindow.cpp # your main file
        # add your own header files below - should be automatically added in CLion
        # example (can also separate with newlines):
        # src/AVL.h src/AVL.cpp
        )
        
target_link_libraries(Main PRIVATE Qt6::Widgets)