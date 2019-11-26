/*
CREATED BY: Benjamin Hamlin
Chapter 1 Question 4
"Palindrom Permutation"
PROMPT:
Given a string, write a function to check if it is a permutation of a palindrome.
a palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
You can ignore casing and non-letter characters.
DATE: 11/24/2019
*/

#include "header.h"

// O(n)
int p4(char* str){
   int alpha[26] = {0};
   int flag = 0;
   for(int i = 0; str[i] != '\0'; ++i){
      if(isalpha(str[i])){
         alpha[tolower(str[i])-'a']++;
      }
   }

   // O(1)
   for(int i = 0; i < 26; ++i){
      if(alpha[i]%2 != 0 && flag == 0){
         flag = 1;
      }else if(alpha[i]%2 != 0 && flag != 0){
         return 0;
      }
   }
   return 1;
}

int main(int argc, char* argv[]){
   if(argc > 1){
      if(strcmp("-d", argv[1]) == 0 ){
         if(p4("Taco cat") == 0){
            printf("ok");
         }
         else{
            printf("Failed");
         }
         if(p4("race car") == 0){
            printf("ok");
         }
         else{
            printf("Failed");
         }
         if(p4("taco$ cat") == 0){
            printf("ok");
         }
         else{
            printf("Failed");
         }
      }
   }
}
