package ch1;

import java.util.*;

/**
* Chapter 1 Question 6
* "String Compression"
* PROMPT:
* Implement a method to perform basic string compression using the counts of repeated characters.
* For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would
* not become smaller than the original string, your method should return the original string.
* You can assume the string has only uppercase and lowercase letters.
* DATE: 12/23/2019
* @author Benjamin Hamlin
* @version "1.0, 12/23/2019"
*/


public class P6Ch1{
  /**
  * Compresses a string by putting the character followed by the integer its repeated
  * @param str String to be compressed
  * @return Compressed string
  */
  public String p6(String str){
    StringBuilder build = new StringBuilder();
    char[] s = str.toCharArray();
    int count = 1;
    char prev = s[0];
    for(int i = 1; i < s.length; i++){
      if(prev == s[i]){
        count++;
      }else{
        build.append(prev);
        build.append(count);
        count = 1;
        prev = s[i];
      }
    }
    build.append(prev);
    build.append(count);
    if(build.length()>str.length()){
      return str;
    }
    return build.toString();
  }
}
