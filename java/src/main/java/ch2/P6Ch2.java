package ch2;

import java.util.LinkedList;
import java.util.ListIterator;
import java.lang.Math;

/**
Chapter 2 Question 6
"Palindrome"
PROMPT:
Implement a function to check if a linked list is a palindrome

 * @author Benjamin Hamlin
 * @version "1.0, 8/12/2020"
 */

 public class P6Ch2{
   /**
   * Checks if given string is a palindrome
   * @param str string to be processed
   * @return true or false
   */
   public Boolean p6(LinkedList<Character> str){
     ListIterator<Character> start = str.listIterator();
     ListIterator<Character> end = str.listIterator(str.size());
     char front = 0;
     char back = 0;
     int count = 0;
     while(start.hasNext() && end.hasPrevious() && count < Math.ceil(str.size()/2)){
       front = start.next();
       back = end.previous();
       if(front != back){
         return false;
       }
     }
     return true;
   }
 }
