[![Build Status](https://travis-ci.org/davidtazy/qmake-feature-conan-generator.svg?branch=master)](https://travis-ci.org/davidtazy/qmake-feature-conan-generator)

#  Reduce number of lines in your .pro files and enhance lisibility

## how generator works

using QMAKEFEATURE capability
ref [http://doc.qt.io/qt-5/qmake-advanced-usage.html](http://doc.qt.io/qt-5/qmake-advanced-usage.html)

* create a conan.pri file to help user to register .prf directory
* create one prf file by dependency, for exemple, gtest.prf

## usage in your qmake projects

* create a .qmake.conf in the root dir of your project include conan.pri 
* in your pro file add your dependencies simply by appending dependency name to CONFIG variable (see test_generator/tests/tests.pro

# how to try
```bash
git clone https://github.com/davidtazy/qmake-feature-conan-generator.git
cd qmake-feature-conan-generator
conan create . david/testing   #or change test_generator/conanfile.txt accordingly
mkdir build & cd build

# install third parts libs and prf files
conan install ../test_generator
#create make file
qmake -recursive ../test_generator/my_big_app.pro
#build
make
#test
./tests/tests
```


