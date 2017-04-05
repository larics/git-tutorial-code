cmake_minimum_required(VERSION 3.3)
project(lust)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(lust_SOURCES lust.cpp)
add_executable(lust ${lust_SOURCES})
