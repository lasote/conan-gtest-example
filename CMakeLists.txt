PROJECT(MyTestingExample)
cmake_minimum_required(VERSION 3.0)

include(conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

ADD_LIBRARY(encrypter encrypter.cpp)
TARGET_LINK_LIBRARIES(encrypter ${CONAN_LIBS})
