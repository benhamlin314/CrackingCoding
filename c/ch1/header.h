#ifndef HEADER
#define HEADER

#include <stdio.h>
#include <string.h>
#include <ctype.h>

typedef struct zeroNode{
  int row;
  int col;
}ZeroNode;

int p1_single_structure(char *str);
int p2(char* s1, char* s2);
char* p3(char* str, int length);
int p4(char* str);
int insertChar(char* s1, char* s2, int loc);
int removeChar(char* s1, char* s2, int loc);
int replaceChar(char* s1, char* s2, int loc);
int diffLocation(char* s1, char* s2);
int p5(char* s1, char* s2);
char* p6(char* s);
int[][] p7(int[][] matrix);
ZeroNode* findZeros(int[][] matrix, int m, int n);
void zero(int** matrix, int row, int col, int m, int n);
int[][] p8(int[][] matrix, int m, int n);
int isSubstring(char* str1, char* str2);
int p9(char* s1, char* s2);

#endif
