/**
 * Chapter 1 Question 2
 * "Check Permutation"
 * PROMPT:
 * Given two stings, write a method to decide if one is a permutation of the other
 * DATE: 12/18/2019
 * @author Benjamin Hamlin
 * @version "1.0, 12/18/2019"
 */
import java.util.Map;
import java.util.HashMap;
import java.util.Collection;

public class P2{
  /**
  * Determines if string 2 is a permutation of string 1
  * @param s1 The string to be checked against
  * @param s2 The string to be checked
  * @return boolean result of check
  */
  public boolean p2(char[] s1, char[] s2){
    Map<Character,Integer> dict = new HashMap<Character,Integer>();
    for(char c : s1){
      if(dict.containsKey(c)){
        dict.put(c, dict.get(c)+1);
      }else{
        dict.put(c, 1);
      }
    }
    for(char c2 : s2){
      if(dict.containsKey(c2)){
        dict.put(c2, dict.get(c2)-1);
      }else{
        return false;
      }
    }
    Collection<Integer> vals;
    vals = dict.values();
    for(int i : vals){
      if(i != 0){
        return false;
      }
    }
    return true;
  }
}
