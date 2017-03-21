[![Build Status](https://travis-ci.org/lasote/conan-gtest-example.svg?branch=master)](https://travis-ci.org/lasote/conan-gtest-example)  [![Build status](https://ci.appveyor.com/api/projects/status/kvx4nmlrt98727mo?svg=true)](https://ci.appveyor.com/project/lasote/conan-gtest-example)

# Conan GTest Example 

[Conan.io](https://conan.io) example for [gtest](https://github.com/google/googletest/) project

## Build project

Download conan client from [Conan.io](https://conan.io) and run:

    $ conan test_package

This command will export, build and test the project  

Or, if you want build only the example

    $ conan export lasote
    $ conan install conan-gtest-example/0.1.0@lasote/testing --build conan-gtest-example

### CMake

You could use CMake to build the project directly

    $ mkdir build && cd build
    $ conan install ..
    $ cmake ..
    $ cmake --build .

## Test project

To validate the project package:

    $ cd test_package
    $ mkdir build && cd build
    $ conan install ..
    $ cmake ..
    $ cmake --build .
    $ cmake --build . --target test
