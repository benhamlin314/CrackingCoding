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
}
