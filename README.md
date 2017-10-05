# Conan GTest Example 

[![Build Status](https://travis-ci.org/lasote/conan-gtest-example.svg?branch=master)](https://travis-ci.org/lasote/conan-gtest-example) [![Build status](https://ci.appveyor.com/api/projects/status/kvx4nmlrt98727mo?svg=true)](https://ci.appveyor.com/project/lasote/conan-gtest-example) [![License](http://img.shields.io/:license-mit-blue.svg)](http://doge.mit-license.org)

## Synopsis

[Conan.io](https://conan.io) example for [gtest](https://github.com/google/googletest/) project.

The project is using OpenSSL to build an encryption library, and using Google test to ensure that the library is built correctly.
The Google test library is required in the **test_package/conanfile.py**.

A different approach would be running the test at the end of the **build()** method in the root conanfile.py and require gtest library as a **build_require**,
so it would be only downloaded when the encryption library has to be built from sources.

With that approach, the **test_package** project could just run an example using/linking with the encryption library.

## Build

Download conan client from [Conan.io](https://conan.io) and run:

    $ conan create user/channel

The above command will export, build and test a conan package for a custom encryption library.


## License
[LICENSE](LICENSE)
