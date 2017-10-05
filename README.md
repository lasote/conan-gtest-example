# Conan GTest Example 

[![Build Status](https://travis-ci.org/lasote/conan-gtest-example.svg?branch=master)](https://travis-ci.org/lasote/conan-gtest-example) [![Build status](https://ci.appveyor.com/api/projects/status/kvx4nmlrt98727mo?svg=true)](https://ci.appveyor.com/project/lasote/conan-gtest-example) [![License](http://img.shields.io/:license-mit-blue.svg)](http://doge.mit-license.org)

## Synopsis

[Conan.io](https://conan.io) example for [gtest](https://github.com/google/googletest/) project.

The project is using OpenSSL to build an encryption library, and using Google test to ensure that the library is built correctly.
The Google test library is required as a **require** in the **test_package/conanfile.py**.

## Build

Download conan client from [Conan.io](https://conan.io) and run:

    $ conan create user/channel

The above command will export, build and test a conan package for a custom encryption library.


## License
[LICENSE](LICENSE)
