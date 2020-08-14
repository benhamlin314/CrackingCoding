import java.util.LinkedList;
import java.util.ListIterator;

/**
Chapter 2 Question 5
"Sum Lists"
PROMPT:
You have two numbers represented by a linked list, where each node contains
 a single digit. The digits are stored in reverse order, such that the 1's
digit is at the head of the list. Write a function that adds the two numbers
and returns the sum as a linked list. (You are not allowed to "cheat" and just
convert the linked list to an integer.)

FOLLOW UP
Solve the above problem with the digits stored in forward order.
DATE: 12/8/2019
 * @author Benjamin Hamlin
 * @version "1.0, 8/11/2020"
 */

public class P5Ch2{
  /**
  * Sums two numbers represented by linkedlists
  * @param num1
  * @param num2
  * @return sum of the two numbers
  */
  public LinkedList<int> p5(LinkedList<int> num1, LinkedList<int> num2){
    LinkedList<int> sum = new LinkedList<int>();
    int carry = 0;
    int temp = 0;
    ListIterator<int> li = num1.listIterator();
    ListIterator<int> li2 = num2.listIterator();
    while(li.hasNext() || li2.hasNext()){
      if(li.hasNext() && li2.hasNext()){
        temp = li.next() + li2.next() + carry;
      }else if(li.hasNext()){
        temp = li.next() + carry;
      }else{//li2 has next only
        temp = li2.next() + carry;
      }
      carry = temp % 10;
      temp /= 10;
      sum.add(temp);
    }
    return sum;
  }
}
