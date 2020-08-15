package ch2;

import org.junit.Test;
import org.junit.Ignore;
import static org.junit.Assert.*;
import java.util.LinkedList;

public class TestsCh2{
  @Test
  public void test_p1(){
    P1Ch2 p = new P1Ch2();
    int[] arr = {5,1,3,2,4,5,3,6,1,7,8,5};
    Object[] ans = {5,1,3,2,4,6,7,8};
    LinkedList<Integer> l1 = new LinkedList<Integer>();
    for(int i: arr){
      l1.add(i);
    }
    assertArrayEquals(ans, p.p1(l1).toArray());
  }

  @Test
  public void test_p2(){
    P2Ch2 p = new P2Ch2();
    int[] arr = {5,1,3,2,4,5,3,6,1,7,8,5};
    LinkedList<Integer> l1 = new LinkedList<Integer>();
    for(int i: arr){
      l1.add(i);
    }
    assertEquals(1, p.p2(l1,3));
  }

  //further debugging needed
  @Ignore
  @Test
  public void test_p3(){
    P3Ch2 p = new P3Ch2();
    MyLinkedListNode<Integer> list = new MyLinkedListNode<Integer>(5);
    list.SetNext(new MyLinkedListNode<Integer>(4));
    MyLinkedListNode<Integer> mid = new MyLinkedListNode<Integer>(3);
    list.next().SetNext(mid);
    mid.SetNext(new MyLinkedListNode<Integer>(2));
    mid.next().SetNext(new MyLinkedListNode<Integer>(1));
    p.p3(mid);
    assertArrayEquals("Node not deleted", "[5,4,2,1]".toCharArray(), list.myToString().toCharArray());
  }
}
