/*******************************
 CREATED BY: Benjamin Hamlin
 Chapter 1 Question 1
 "Is Unique"
 PROMPT:
 Implement an algorithm to determine if a string has all unique characters.
 What if you cannot use additional data structures?
 DATE: 11/14/2019
*******************************/
#include "header.h"

// O(n!) where n is the length of the string
// Horribly inefficient, thinking of a more efficient algorithm
int p1_single_structure(char *str){
  int len = strlen(str);
  for(int loc = 0; loc < len; ++loc){
    for(int i = loc+1; i < len; ++i){
      if(str[i] == str[loc]){
        return 0;//returns false if same character found
      }
    }
  }
  return 1;
}
