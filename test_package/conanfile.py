from conans.model.conan_file import ConanFile
from conans import CMake


class TestConanGTestExample(ConanFile):
    name = "TestConanGTestExample"
    version = "0.1.0"
    author = "lasote"
    url = "https://github.com/lasote/conan-gtest-example"
    license = "MIT"
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    cmake = None

    def build(self):
        self.cmake = CMake(self)
        self.cmake.configure(source_dir=self.conanfile_directory, build_dir="./")
        self.cmake.build()

    def imports(self):
        self.copy("*.so", "bin", "lib")
        self.copy("*.dll", "bin", "bin")
        self.copy("*.dylib", "bin", "bin")

    def test(self):
        target_test = "RUN_TESTS" if self.settings.os == "Windows" else "test"
        self.cmake.build(target=target_test)
