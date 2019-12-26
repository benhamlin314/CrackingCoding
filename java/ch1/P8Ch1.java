/**
* Chapter 1 Question 8
* "Zero Matrix"
* PROMPT:
* Write an algorithm such that if an element in an MxN matrix is 0, its entire row
* and column are set to 0.
* DATE: 12/23/2019
* @author Benjamin Hamlin
* @version "1.0, 12/23/2019"
*/
import java.util.Map;
import java.util.HashMap;
import java.util.LinkedList;

public class P8Ch1{
  /**
  * Private class to hold row, column of zeros
  */
  private class Zero{
    private int row = 0;
    private int column = 0;

    public Zero(int row, int col){
      this.row = row;
      this.column = col;
    }

    public int GetRow(){
      return this.row;
    }

    public int GetColumn(){
      return this.column;
    }
  }
  /**
  * Sets entire row and column to 0 when a 0 is found
  * @param arr array to be zeroed
  * @return zeroed array
  */
  public int[][] p8(int[][] arr, int m, int n){
    LinkedList<Zero> zeros = new LinkedList<Zero>();
    for(int i = 0; i < n; ++i){
      for(int j = 0; j < m; ++j){
        if(arr[i][j] == 0){
          zeros.add(new Zero(i,j));
        }
      }
    }
    Zero cur = zeros.pop();
    while(cur != null){
      for(int i = 0; i < m; ++i){
        arr[cur.GetRow()][i] = 0;
      }
      for(int j = 0; j < n; ++j){
        arr[j][cur.GetColumn()] = 0;
      }
      if(zeros.isEmpty()){
        break;
      }
      cur = zeros.pop();
    }
    return arr;
  }
}
