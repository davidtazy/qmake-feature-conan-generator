message("build dir is $$BUILD_DIR")

TEMPLATE =app
CONFIG -= qt
CONFIG += gtest
SOURCES += test_my_app.cpp
