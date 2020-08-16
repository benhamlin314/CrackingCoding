/*
CREATED BY: Benjamin Hamlin
Chapter 1 Question 5
"One Away"
PROMPT:
There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character.
Given two strings, write function to check if they are one edit (or zero edits) away.
DATE: 11/24/2019
*/

#include "header.h"

int insertChar(char* s1, char* s2, int loc){
  char* temp = (char*)malloc(strlen(s1)+1);
  strncpy(temp, s2, loc-1);
  temp[loc] = s1[loc];
  for(int i = loc; s2[i] != '\0'; ++i){
    temp[i] = s2[i];
  }
  temp[i] = '\0';
  if(strcmp(temp, s1) == 0){
    return 1;
  }
  return 0;
}

int removeChar(char* s1, char* s2, int loc){
  char* temp = (char*)malloc(strlent(s1)+1);
  strncpy(temp, s2, loc-1);
  for(int i = loc+1; s2[i] != '\0'; ++i){
    temp[i] = s2[i];
  }
  temp[i] = '\0';
  if(strcmp(temp, s1) == 0){
    return 1;
  }
  return 0;
}

int replaceChar(char* s1, char* s2, int loc){
  char temp = s2[loc];
  s2[loc] = s1[loc];
  if(strcmp(s1, s2) == 0){
    s2[loc] = temp;
    return 1;
  }
  return 0;
}

//finds the index of the first difference in the string
int diffLocation(char* s1, char* s2){
  int i = 0;
  while(s1[i] != s2[i]){
    i++;
  }
  return i;
}

int p5(char* s1, char* s2){
  int loc = diffLocation(s1, s2);
  if(strlen(s1) == strlen(s2)){
    return replaceChar(s1, s2, loc);
  }
  else if(strlen(s1) > strlen(s2)){
    return insertChar(s1, s2, loc);
  }
  else{
    return removeChar(s1, s2, loc);
  }
}

/*
int main(int argc, char* argv[]){
  if(argc > 1){
    if(strcmp("-d", argv[1]) == 0 ){
      //tests remove
      if(p5("chicken","chickens")==1){
        printf("ok");
      }
      else{
        printf("Failed");
      }
      //test insert
      if(p5("chickens", "chicken")==1){
        printf("ok");
      }
      else{
        printf("Failed");
      }
      //test replaceChar
      if(p5("chicken", "chickon")==1){
        printf("ok");
      }
      else{
        printf("Failed");
      }
    }
  }
}
*/
