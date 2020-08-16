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

}

static void test_p3(){

}

static void test_p4(){

}

static void test_p5(){

}

static void test_p6(){

}

static void test_p7(){

}

static void test_p8(){

}

static void test_p9(){

}

int main(int argc, char **argv)
{
  const UnitTest tests[] = {
    unit_test(test_p1)
  };
  return run_tests(tests);
}
