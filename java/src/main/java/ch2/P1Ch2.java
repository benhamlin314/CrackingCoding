package ch2;

import java.util.LinkedList;
import java.util.ListIterator;
/**
 * Chapter 2 Question 1
 * "Remove Dups"
 * <p>
 * PROMPT:
 * Write code to remove duplicates form an unsorted linked list.
 * FOLLOW UP
 * How would you solve this problem if a temporary buffer is not allowed?
 * DATE: 12/26/2019
 * @author Benjamin Hamlin
 * @version "1.0, 12/26/2019"
 */
public class P1Ch2{
  /**
  * Removes duplicates from an unsorted linked list
  * time- O(n)    space- O(2n)
  * @param list LinkedList dups will be removed
  * @return LinkedList with removed dups
  */
  public LinkedList<Integer> p1(LinkedList<Integer> list){
    LinkedList<Integer> list2 = new LinkedList<Integer>();
    int temp;
    while(!list.isEmpty()){
      temp = list.pop();
      if(!list2.contains(temp)){
        list2.add(temp);
      }
    }
    return list2;
  }

  /*
  /**
  * Removes duplicates from an unsorted linked list in place
  * @param list LinkedList dups will be removed
  * @return LinkedList with removed dups
  */
  /*public LinkedList<Integer> p1_inplace(LinkedList<Integer> list){
    ListIterator<Integer> it = list.listIterator(index);

    return list;
  }
  */
}
