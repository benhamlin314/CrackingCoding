package ch2;

import java.util.LinkedList;
import java.util.ListIterator;

/**
 * Chapter 2 Question 4
 * "Partition"
 * <p>
 * PROMPT:
 * Write code to partition a linked list around a value x, such that all nodes
 * less than x come before all nodes greater than or equal to x. (IMPORTANT: the
 * partition element x can appear anywhere in the "right partition"; it does not
 * need to appear between the left and right partitions)
 * @author Benjamin Hamlin
 * @version "1.0, 12/27/2019"
 */
public class P4Ch2{
  /**
  * Partitions a linkedlist around a given value
  * @param list LinkedList to be partitioned
  * @param x value to be partitioned on
  * @return partitioned list
  */
  public LinkedList<Integer> p4(LinkedList<Integer> list, int x){
    ListIterator<Integer> li = list.listIterator();
    int temp;
    while(li.hasNext()){
      temp = li.next();
      if(temp < x){
        li.remove();
        list.addFirst(temp);
      }
    }
    return list;
  }
}
