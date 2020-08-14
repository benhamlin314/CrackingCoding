package ch1;

/**
 * Chapter 1 Question 1
 * "Is Unique"
 * PROMPT:
 * Implement an algorithm to determine if a string has all unique characters.
 * What if you cannot use additional data structures?
 * DATE: 12/18/2019
 * @author Benjamin Hamlin
 * @version "1.0, 12/18/2019"
 */

 
public class P1Ch1{
  /**
  * Determines if a string has all unique characters
  * @param s1 The string to be checked for unique characters
  * @return boolean result of check
  */
  public boolean p1(String s1){
    int len = s1.length();
    char[] str;
    str = s1.toCharArray();
    for (int i = 0; i < len; ++i){
      for (int j = i+1; j < len; ++j){
        if(str[i] == str[j]){
          return false;
        }
      }
    }
    return true;
  }
}
