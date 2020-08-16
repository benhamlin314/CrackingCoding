#include <stdarg.h>
#include <stddef.h>
#include <setjmp.h>
#include <cmocka.h>

#include "header.h"

static void test_p1(){
  assert_int_equal(p1_single_structure("adept"), 1);
  assert_int_equal(p1_single_structure("adapt"), 0);
  assert_int_equal(p1_single_structure("abcdefghijklmnopqrstuvwxyz"), 1);
}

static void test_p2(){
  assert_int_equal(p2("care", "race"), 1);
}

static void test_p3(){
  assert_string_equal(p3("Mr John Smith", 30), "Mr%20John%20Smith");
  assert_string_equal(p3("This is a string", 30), "This%20is%20a%20string");
}

static void test_p4(){
  assert_int_equal(p4("Taco cat"), 0);
  assert_int_equal(p4("race car"), 0);
}

static void test_p5(){
  assert_int_equal(p5("chicken","chickens"), 1);
  assert_int_equal(p5("chickens", "chicken"), 1);
  assert_int_equal(p5("chicken", "chickon"), 1);
}

static void test_p6(){
  assert_string_equal(p6("aabcccccaaa"),"a2b1c5a3");
}

static void test_p7(){

}

static void test_p8(){

}

static void test_p9(){

}

int main(int argc, char **argv){
  const UnitTest tests[] = {
    unit_test(test_p1),
    unit_test(test_p2),
    //unit_test(test_p3),
    //unit_test(test_p4),
    //unit_test(test_p5),
    //unit_test(test_p6)
  };
  return run_tests(tests);
}
