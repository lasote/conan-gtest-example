# Conan GTest Example 

[![Build Status](https://travis-ci.org/lasote/conan-gtest-example.svg?branch=master)](https://travis-ci.org/lasote/conan-gtest-example) [![Build status](https://ci.appveyor.com/api/projects/status/kvx4nmlrt98727mo?svg=true)](https://ci.appveyor.com/project/lasote/conan-gtest-example) [![License](http://img.shields.io/:license-mit-blue.svg)](http://doge.mit-license.org)

## Synopsis

[Conan.io](https://conan.io) example for [Google Test](https://github.com/google/googletest/) project.

## Build

Download conan client from [Conan.io](https://conan.io) and run:

    $ conan test_package whatevername/whateverchannel

The above command will export, build and test the project.

Or, build only the example:

    $ conan export lasote/testing
    $ conan install conan-gtest-example/0.1.0@lasote/testing --build conan-gtest-example

### CMake

Use CMake to build the project directly:

    $ mkdir build && cd build
    $ conan install ..
    $ cmake ..
    $ cmake --build .

## Test

To validate the project package:

    $ cd test_package
    $ mkdir build && cd build
    $ conan install ..
    $ cmake ..
    $ cmake --build .  # FIXME
    $ cmake --build . --target test  # FIXME

## License

[LICENSE](LICENSE)
