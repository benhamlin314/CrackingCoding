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
   char* arr = (char*)malloc(sizeof(char) * length);
   char* token = strtok(str, " ");
   while(token != NULL && token != 0){
      strcat(arr,token);
      token = strtok(NULL, " ");
      if(token != NULL){
        strcat(arr,"%20");
      }
   }
   strcpy(str, arr);
   free(arr);
   return str;
}

// int main(int argc, char const *argv[]) {
//   char * string = (char *)malloc(sizeof(char) * 18);
//   strcpy(string, "Mr John Smith");
//   char * temp;
//   temp = p3(string, 18);
//   printf("%s\n", temp);
//   free(string);
//   return 0;
// }
