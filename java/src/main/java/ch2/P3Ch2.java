package ch2;

import java.util.LinkedList;
import java.util.ListIterator;

/**
 * Chapter 2 Question 3
 * "Delete Middle Node"
 * <p>
 * PROMPT:
 * Implement an algorithm to delete a node in the middle(i.e, any node but the first and last node, not necessarily the exact middle)
 * of a singly linked list, given only access to that node.
 * @author Benjamin Hamlin
 * @version "1.0, 12/26/2019"
 */
public class P3Ch2{
  /**
  * Deletes the given node with only acces to that node
  * @param node of MyLinkedList
  */
  public void p3(MyLinkedListNode<Integer> node){
    while(node.next().next() != null){
      node.SetData(node.next().GetData());
      node = node.next();
    }
    node.SetData(node.next().GetData());
    node.SetNext(null);
    System.out.println(node.myToString());
  }
}
