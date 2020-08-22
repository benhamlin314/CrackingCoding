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
  for(int i = 0; i < length || str[i] != '\0'; i++){
    if(str[i] == ' '){
      char temp1, temp2, temp3, temp4;
      str[i++] = '%';
      temp1 = str[i];
      str[i++] = '2';
      temp2 = str[i];
      str[i++] = '0';
      for(int j = i; j < length || str[j] != '\0'; j+=2){
        temp3 = str[j];
        temp4 = str[j+1];
        str[j] = temp1;
        str[j+1] = temp2;
        temp1 = temp3;
        temp2 = temp4;
      }
    }
  }
  return str;
   // char* arr = (char*)malloc(sizeof(char) * length);
   // char* token = strtok(str, " ");
   // while(token != NULL && token != 0){
   //    strcat(arr,token);
   //    token = strtok(NULL, " ");
   //    if(token != NULL){
   //      strcat(arr,"%20");
   //    }
   // }
   // strcpy(str, arr);
   // free(arr);
   // return str;
}

// int main(int argc, char const *argv[]) {
//   char * string = (char *)malloc(sizeof(char) * 18);
//   strcpy(string, "Mr John Smith");
//   printf("%i\n", strlen(string));
//   char * temp;
//   temp = p3(string, 18);
//   printf("%s\n", temp);
//   free(string);
//   return 0;
// }
