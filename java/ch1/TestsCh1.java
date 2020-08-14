import org.junit.Test;
import org.junit.Ignore;
import static org.junit.Assert.*;

public class TestsCh1{

  @Test
  public void test_p1_true(){
    P1Ch1 problem = new P1Ch1();
    assertTrue(problem.p1("adept"));
  }

  @Test
  public void test_p1_false(){
    P1Ch1 problem = new P1Ch1();
    assertFalse(problem.p1("adapt"));
  }

  @Test
  public void test_p2_true(){
    P2Ch1 p = new P2Ch1();
    String s1 = "mane";
    String s2 = "name";
    assertTrue(p.p2(s1.toCharArray(), s2.toCharArray()));
  }

  @Test
  public void test_p2_false(){
    P2Ch1 p = new P2Ch1();
    String s1 = "chicken";
    String s2 = "notchicken";
    assertFalse(p.p2(s1.toCharArray(), s2.toCharArray()));
  }

  @Test
  public void test_p3_small(){
    P3Ch1 p = new P3Ch1();
    String s2 = "Mr John Smith    ";
    int len = 13;
    assertArrayEquals("Mr%20John%20Smith".toCharArray(),p.p3(s2.toCharArray(),len));
  }

  @Test
  public void test_p3_long(){
    P3Ch1 p = new P3Ch1();
    String s2 = "This is a test to urlify a long string with many spaces                      ";
    int len = 55;
    assertArrayEquals("This%20is%20a%20test%20to%20urlify%20a%20long%20string%20with%20many%20spaces".toCharArray(), p.p3(s2.toCharArray(),len));
  }

  @Test
  public void test_p4_nospaces(){
    P4Ch1 p = new P4Ch1();
    String s1 = "rraacce";//race car
    assertTrue(p.p4(s1));
  }

  @Test
  public void test_p4_manyspaces(){
    P4Ch1 p = new P4Ch1();
    String s1 = "Are we not pure? “No, sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man—a prisoner up to new era.";//race car
    assertTrue(p.p4(s1));
  }

  @Test
  public void test_p5_insert(){
    P5Ch1 p = new P5Ch1();
    String s1 = "indescribable";
    String s2 = "indscribable";
    assertTrue("Fail indescribable",p.p5(s1,s2));
  }

  @Test
  public void test_p5_remove(){
    P5Ch1 p = new P5Ch1();
    String s1 = "chicken";
    String s2 = "achicken";
    assertTrue("Fail chicken", p.p5(s1,s2));
  }

  @Test
  public void test_p5_replace(){
    P5Ch1 p = new P5Ch1();
    String s1 = "floofy";
    String s2 = "flooty";
    assertTrue(p.p5(s1,s2));
  }

  @Test
  public void test_p6(){
    P6Ch1 p = new P6Ch1();
    String s1 = "aabcccccaaa";
    String ans = "a2b1c5a3";
    assertEquals(ans, p.p6(s1));
  }

  //Place p7 tests here

  @Test
  public void test_p8(){
    P8Ch1 p = new P8Ch1();
    int[][] arr = {
      {5,4,6,3,5},
      {4,0,3,2,4},
      {0,2,2,3,4}
      };
    int[][] ans = {
      {0,0,6,3,5},
      {0,0,0,0,0},
      {0,0,0,0,0}
      };
    assertEquals(ans,p.p8(arr, 5, 3));
  }

  @Test
  public void test_p9(){
    P9Ch1 p = new P9Ch1();
    String s1 = "waterbottle";
    String s2 = "erbottlewat";
    assertTrue(p.p9(s1, s2));
  }
}
