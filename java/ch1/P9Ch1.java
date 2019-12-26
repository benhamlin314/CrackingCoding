/**
* Chapter 1 Question 9
* "String Rotation"
* PROMPT:
* Assume you have a method isSubstring which checks if one word is a substring of another.
* Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
* call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat")
* DATE: 12/23/2019
* @author Benjamin Hamlin
* @version "1.0, 12/23/2019"
*/
public class P9Ch1{
  /**
  * Checks if s2 is a rotation of s1
  * @param s1 string to be checked against
  * @param s2 string to be checked
  * @return boolean if s2 is rotation of s1
  */
  public boolean p9(String s1, String s2){
    StringBuilder builder = new StringBuilder();
    builder.append(s1);
    builder.append(s1);
    return builder.toString().contains(s2);
  }
}
