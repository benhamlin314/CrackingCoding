/*
CREATED BY: Benjamin Hamlin
Chapter 1 Question 6
"String Compression"
PROMPT:
Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would
not become smaller than the original string, your method should return the original string.
You can assume the string has only uppercase and lowercase letters.
DATE: 12/2/2019
*/

#include "header.h"

char* p6(char* s){
  char * comp = (char*)malloc(sizeof(char) * strlen(s));
  int count = 0;
  int i = 0;
  char temp = s[i];
  while(i < strlen(s) && s[i] != '\0'){
    if(s[i] == temp){
      count++;
    }
    else{
      strcat(comp, temp);
      strcat(comp, count);
      count = 0;
      temp = s[i];
    }
    ++i;
  }
  if(i < strlen(s)){
    strcpy(s, comp);
  }
  free(comp);
  return s;
}
