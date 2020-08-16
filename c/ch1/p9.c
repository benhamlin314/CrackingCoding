/*
CREATED BY: Benjamin Hamlin
Chapter 1 Question 9
"String Rotation"
PROMPT:
Assume you have a method isSubstring which checks if one word is a substring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat")
DATE: 12/4/2019
*/

int isSubstring(char* str1, char* str2){
  char * temp = strstr(str1, str2);
  if(temp == 0){
    return 1;
  }
  return 0;
}

int p9(char* s1, char* s2){
  char* temp = (char*)malloc(strlen(s1)*2);
  strcat(temp, s1);
  strcat(temp, s1);
  if(isSubstring(temp, s2)){
    return 1;
  }
  return 0;
}
