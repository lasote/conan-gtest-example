from conans import ConanFile
from conans import CMake


class ConanGTestExample(ConanFile):
    """Build Conan GTest Example"""
    name = "conan-gtest-example"
    version = "0.1.0"
    url = "https://github.com/uilianries/conan-gtest-example"
    author = "lasote"
    license = "MIT"
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake"
    exports = "*"
    description = "Google Test example of use for conan.io"
    requires = "OpenSSL/1.0.2l@conan/stable", "gtest/1.7.0@lasote/stable"
    options = {"shared": [True, False]}
    default_options = "gtest:shared=True", "shared=False"

    def build(self):
        shared = {"BUILD_SHARED_LIBS": self.options.shared}
        cmake = CMake(self)
        cmake.configure(defs=shared)
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*.lib", dst="lib", src="lib", keep_path=False)
        self.copy("*.dll", dst="bin", src="bin", keep_path=False)
        self.copy("*.dylib", dst="bin", src="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["encrypter"]
