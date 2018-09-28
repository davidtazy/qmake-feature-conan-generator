# qmake-feature-conan-generator
conan.io generator for qmake using QMAKEFEATURE capability



# how to try
conan create . david/testing   (or change test_generator/conanfile.txt accordingly)
mkdir build & cd build
conan install ../test_generator
qmake -recursive ../test_generator/my_big_app.pro
make
./tests/tests
