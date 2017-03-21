import os
from conans.model.conan_file import ConanFile
from conans import CMake


USERNAME = os.getenv("CONAN_USERNAME", "lasote")
CHANNEL = os.getenv("CONAN_CHANNEL", "testing")


class TestConanGTestExample(ConanFile):
    name = "TestConanGTestExample"
    version = "0.1.0"
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    requires = "conan-gtest-example/0.1.0@%s/%s" % (USERNAME, CHANNEL)

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake %s %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def imports(self):
        self.copy("*.so", "bin", "lib")
        self.copy("*.dll", "bin", "bin")
        self.copy("*.dylib", "bin", "bin")

    def test(self):
        target = "RUN_TESTS" if self.settings.os == "Windows" else "test"
        self.run("cmake --build . --target %s" % target)

