PROJECT(MyTestingExample)
cmake_minimum_required(VERSION 2.8)

include(conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

OPTION(BUILD_TEST "Build the tests" FALSE)

ADD_LIBRARY(encrypter encrypter.cpp)
TARGET_LINK_LIBRARIES(encrypter ${CONAN_LIBS})

IF(BUILD_TEST)
	ADD_EXECUTABLE(encryption_test test/encryption_test.cpp)
	TARGET_LINK_LIBRARIES(encryption_test encrypter ${CONAN_LIBS})
ENDIF()