from conans import ConanFile
from conans import CMake


class ConanGTestExample(ConanFile):
    """Build Conan GTest Example

    """
    name = "conan-gtest-example"
    version = "0.1.0"
    url = "https://github.com/uilianries/conan-gtest-example"
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake"
    exports = "*"
    description = "Google Test example of use for conan.io"
    requires = "OpenSSL/1.0.2i@lasote/stable", "gtest/1.7.0@lasote/stable"
    options = {"shared": [True, False]}
    default_options = "gtest:shared=True", "shared=False"

    def build(self):
        cmake = CMake(self.settings)
        shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else "-DBUILD_SHARED_LIBS=OFF"
        self.run('cmake %s %s %s' % (self.conanfile_directory, cmake.command_line, shared))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*.lib", dst="lib", src="lib", keep_path=False)
        self.copy("*.dll", dst="bin", src="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["encrypter"]

