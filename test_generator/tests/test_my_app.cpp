#include <iostream>
#include <string>
#include <gtest/gtest.h>

using namespace std;

class Salutation
{
public:
  static string greet(const string& name);
};

///////////////////////////////////////
// In the class implementation file

string Salutation::greet(const string& name) {
  ostringstream s;
  s << "Hello " << name << "!";
  return s.str();
}

TEST(SalutationTest, Static) {
  EXPECT_EQ(string("Hello World!"), Salutation::greet("World"));
}