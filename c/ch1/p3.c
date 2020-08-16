/*
CREATED BY: Benjamin Hamlin
Chapter 1 Question 3
"URLify"
PROMPT:
Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold the additional characters,
and that you are given the 'true' length of the string
(Note: if implementing in java, please use a character array so that you can perform this operation in place)
DATE: 11/23/2019
*/

#include "header.h"

char* p3(char* str, int length){
   char* arr = (char*)malloc(length);
   char* token = strtok(str, ' ');
   while(token != NULL){
      strcat(arr,token);
      strcat(arr,"%20");
      token = strtok(NULL, ' ');
   }
   return arr;
}
