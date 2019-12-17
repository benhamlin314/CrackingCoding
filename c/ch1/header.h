#ifndef HEADER
#define HEADER

//cmocka defines
#define 	unit_test(f)   { #f, f, UNIT_TEST_FUNCTION_TYPE_TEST }
#define 	_unit_test_setup(test, setup)   { #test "_" #setup, setup, UNIT_TEST_FUNCTION_TYPE_SETUP }
#define 	unit_test_setup(test, setup)
#define 	_unit_test_teardown(test, teardown)   { #test "_" #teardown, teardown, UNIT_TEST_FUNCTION_TYPE_TEARDOWN }
#define 	unit_test_teardown(test, teardown)
#define 	group_test_setup(setup)   { "group_" #setup, setup, UNIT_TEST_FUNCTION_TYPE_GROUP_SETUP }
#define 	group_test_teardown(teardown)   { "group_" #teardown, teardown, UNIT_TEST_FUNCTION_TYPE_GROUP_TEARDOWN }
#define 	unit_test_setup_teardown(test, setup, teardown)
#define 	cmocka_unit_test(f)   { #f, f, NULL, NULL, NULL }
#define 	cmocka_unit_test_setup(f, setup)   { #f, f, setup, NULL, NULL }
#define 	cmocka_unit_test_teardown(f, teardown)   { #f, f, NULL, teardown, NULL }
#define 	cmocka_unit_test_setup_teardown(f, setup, teardown)   { #f, f, setup, teardown, NULL }
#define 	cmocka_unit_test_prestate(f, state)   { #f, f, NULL, NULL, state }
#define 	cmocka_unit_test_prestate_setup_teardown(f, setup, teardown, state)   { #f, f, setup, teardown, state }
#define 	run_tests(tests)   _run_tests(tests, sizeof(tests) / sizeof((tests)[0]))
#define 	run_group_tests(tests)   _run_group_tests(tests, sizeof(tests) / sizeof((tests)[0]))

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdarg.h>
#include <stddef.h>
#include <setjmp.h>
#include <cmocka.h>


#endif
