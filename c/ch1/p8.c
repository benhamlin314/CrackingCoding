/*
CREATED BY: Benjamin Hamlin
Chapter 1 Question 8
"Zero Matrix"
PROMPT:
Write an algorithm such that if an element in an MxN matrix is 0, its entire row
and column are set to 0.
DATE: 12/3/2019
*/

typedef struct zeroNode{
  int row;
  int col;
}ZeroNode;

ZeroNode* findZeros(int[][] matrix, int m, int n){
  ZeroNode* array = (ZeroNode*)malloc(sizeof(ZeroNode)*(m*n));//accounts for all
  int count = 0;
  for(int i = 0; i < m; i++){
    for(int j = 0; j < n; j++){
      if(matrix[i][j] == 0){
        array[count].row = i;
        array[count++].col = j;
      }
    }
  }
  array[count].row = -1;
  array[count].col = -1;
  return array;
}

void zero(int** matrix, int row, int col, int m, int n){
  for(int i = 0; i < n; i++){
    matrix[row][i] = 0;
  }
  for(int j = 0; j < m; j++){
    matrix[i][col] = 0;
  }
}

int[][] p8(int[][] matrix, int m, int n){
  ZeroNode* arr = findZeros(matrix, m, n);
  for(int i = 0; i < (m*n) && arr[i].row != -1; i++){
    zero(matrix, arr[i].row, arr[i].col, m, n);
  }
  return matrix;
}
