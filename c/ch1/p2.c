/*
CREATED BY: Benjamin Hamlin
Chapter 1 Question 2
"Check Permutation"
PROMPT:
Given two stings, write a method to decide if one is a permutation of the other
DATE: 11/23/2019
*/

#include "header.h"

// O(n) where n is the length of the strings
int p2(char* s1, char* s2){
   int alpha[93] = {0};
   if(strlen(s1) == strlen(s2)){
      for(int i = 0; s1[i] != '\0'; ++i){
         if(s1[i] != ' '){
            alpha[s1[i]-'!']++;
         }
         if(s2[i] != ' '){
            alpha[s2[i]-'!']++;
         }
      }
      // O(1)
      for(int i = 0; i < 93; ++i){
         if(alpha[i]%2 != 0){
            return 0;
         }
      }
      return 1;
   }
   return 0;
}

int main(int argc, char* argv[]){
   if(argc > 1){
      if(strcmp("-d", argv[1]) == 0 ){
         if(p2("care", "race") == 1){
            printf("ok");
         }
         else{
            printf("Failed");
         }
      }
   }
}
