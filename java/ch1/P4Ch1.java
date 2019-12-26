/**
* Chapter 1 Question 4
* "Palindrome Permutation"
* PROMPT:
* Given a string, write a function to check if it is a permutation of a palindrome.
* a palindrome is a word or phrase that is the same forwards and backwards.
* A permutation is a rearrangement of letters.
* The palindrome does not need to be limited to just dictionary words.
* You can ignore casing and non-letter characters.
* DATE: 12/19/2019
* @author Benjamin Hamlin
* @version "1.0, 12/19/2019"
*/
import java.util.Map;
import java.util.HashMap;
import java.util.Collection;

public class P4Ch1{
  /**
  * Checks if the given string is a permutation of a palindrome
  * @param s1 String to be checked
  * @return boolean value of check
  */
  public boolean p4(String s1){
    String s2 = s1.replaceAll("[^a-zA-Z\\d]*", "");
    s2 = s2.toLowerCase();
    char[] s = s2.toCharArray();
    Map<Character,Integer> dict = new HashMap<Character,Integer>();
    for(char c : s){
      if(dict.containsKey(c)){
        dict.put(c, dict.get(c)+1);
      }else{
        dict.put(c, 1);
      }
    }
    boolean flag = false;
    boolean pass = true;
    Collection<Integer> vals;
    vals = dict.values();
    for(int i : vals){
      if(i%2 != 0){
        if(!flag){
          flag = true;
        }else{
          pass = false;
          break;
        }
      }
    }
    return pass;
  }
}
