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
  char * test1 = (char *) malloc(sizeof(char) * 18);
  strcpy(test1, "Mr John Smith");
  char * test2 = (char *) malloc(sizeof(char) * 22);
  strcpy(test2, "This is a stringh");
  assert_string_equal(p3(test1, 18), "Mr%20John%20Smith");
  assert_string_equal(p3(test2, 22), "This%20is%20a%20string");
  free(test1);
  free(test2);
}

static void test_p4(){
  assert_int_equal(p4("Taco cat"), 0);
  assert_int_equal(p4("race car"), 0);
}

static void test_p5(){
  char * chicken = (char *)malloc(sizeof(char) * 8);
  strcpy(chicken, "chicken");
  char * chickens = (char *)malloc(sizeof(char) * 8);
  strcpy(chickens, "chickens");
  char * chickon = (char *)malloc(sizeof(char) * 8);
  strcpy(chickon, "chickon");
  assert_int_equal(p5(chicken,chickens), 1);
  assert_int_equal(p5(chickens, chicken), 1);
  assert_int_equal(p5(chicken, chickon), 1);
  free(chicken);
  free(chickens);
  free(chickon);
}

static void test_p6(){
  char * test1 = (char *)malloc(sizeof(char) * 12);
  strcpy(test1, "aabcccccaaa");
  assert_string_equal(p6(test1),"a2b1c5a3");
  free(test1);
}

static void test_p7(){
  //TODO: add matrix test
  assert_int_equal(0, 0);
}

static void test_p8(){
  //TODO: add matrix test
}

static void test_p9(){
  char * test1 = (char *)malloc(sizeof(char) * 11);
  strcpy(test1, "waterbottle");
  char * test2 = (char *)malloc(sizeof(char) * 11);
  strcpy(test2, "erbottlewat");
  assert_int_equal(p9(test1,test2), 1);
  free(test1);
  free(test2);
}

int main(int argc, char **argv){
  const UnitTest tests[] = {
    unit_test(test_p1),
    unit_test(test_p2),
    unit_test(test_p3),
    unit_test(test_p4),
    unit_test(test_p5),
    unit_test(test_p6),
    unit_test(test_p7),
    unit_test(test_p8),
    unit_test(test_p9)
  };
  return run_tests(tests);
}
