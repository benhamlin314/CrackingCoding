/**
* Chapter 1 Question 5
* "One Away"
* PROMPT:
* There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character.
* Given two strings, write function to check if they are one edit (or zero edits) away.
* DATE: 12/19/2019
* @author Benjamin Hamlin
* @version "1.0, 12/22/2019"
*/
import java.util.Arrays;

public class P5Ch1{
  /**
  * finds the index of the first difference between s1 and s2
  * @param s1 String to be checked against
  * @param s2 String to be checked
  * @return int value of location
  */
  public int findDiff(char[] s1, char[] s2){
    int index = 0;
    while(s1[index] == s2[index]){
      index++;
    }
    return index;
  }

  /**
  * Checks if s2 is one insert away from s1
  * @param s1 String to be checked against
  * @param s2 String to be checked
  * @param index index of the difference between s1 and s2
  * @return boolean value of check
  */
  public boolean checkInsert(char[] s1, String s2, int index){
    char toInsert = s1[index];
    char[] str2 = new char[s1.length];
    for(int i = 0; i < s2.length(); ++i){
      str2[i] = s2.charAt(i);
    }
    char temp = str2[index];
    char temp2 = str2[index+1];
    str2[index] = toInsert;
    for(int i = index+2; i < s1.length; i++){
      str2[i-1] = temp;
      temp = temp2;
      temp2 = str2[i];
    }
    str2[s1.length-1] = temp;
    return Arrays.equals(s1,str2);
  }

  /**
  * Checks if s2 is one remove away from s1
  * @param s1 String to be checked against
  * @param s2 String to be checked
  * @param index index of the difference between s1 and s2
  * @return boolean value of check
  */
  public boolean checkRemove(char[] s1, String s2, int index){
    char[] str2 = new char[s1.length];
    int j = 0;
    for(int i = 0; i < s2.length(); ++i){
      if(i != index){
        str2[j] = s2.charAt(i);
        j++;
      }
    }
    return Arrays.equals(s1,str2);
  }

  /**
  * Checks if s2 is one replace away from s1
  * @param s1 String to be checked against
  * @param s2 String to be checked
  * @param index index of the difference between s1 and s2
  * @return boolean value of check
  */
  public boolean checkReplace(char[] s1, String s2, int index){
    char[] str2 = s2.toCharArray();
    str2[index] = s1[index];
    return Arrays.equals(s1,str2);
  }

  /**
  * Checks if s2 is one edit away from s1
  * @param s1 String to be checked against
  * @param s2 String to be checked
  * @return boolean value of check
  */
  public boolean p5(String s1, String s2){
    char[] str1 = s1.toCharArray();
    int index = findDiff(str1, s2.toCharArray());
    if(s1.length() > s2.length()){
      return checkInsert(str1, s2, index);
    }else if(s1.length() < s2.length()){
      return checkRemove(str1, s2, index);
    }else{
      return checkReplace(str1, s2, index);
    }
  }
}
