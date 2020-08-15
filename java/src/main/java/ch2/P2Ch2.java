package ch2;

import java.util.LinkedList;
import java.util.ListIterator;

/**
 * Chapter 2 Question 2
 * "Return Kth to Last"
 * <p>
 * PROMPT:
 * Implement an algorithm to find the kth to last element of a singly linked list
 * @author Benjamin Hamlin
 * @version "1.0, 12/26/2019"
 */
public class P2Ch2{
  /**
  * Returns kth to last element of singly linked list
  * @param list LinkedList
  * @param k integer from last element to be found
  * @return int of kth element
  */
  public int p2(LinkedList<Integer> list, int k){
    ListIterator<Integer> iter = list.listIterator();
    int count = 0;
    while(iter.hasNext()){
      count++;
      iter.next();
    }
    count--;//offset by 1
    count -= k;
    return list.get(count);
  }
}
