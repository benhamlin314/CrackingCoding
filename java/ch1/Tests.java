import org.junit.Test;
import org.junit.Ignore;
import static org.junit.Assert.*;

public class Tests{

  @Test
  public void test_p1_true(){
    P1 problem = new P1();
    assertTrue(problem.p1("adept"));
  }

  @Test
  public void test_p1_false(){
    P1 problem = new P1();
    assertFalse(problem.p1("adapt"));
  }

  @Test
  public void test_p2_true(){
    P2 p = new P2();
    String s1 = "mane";
    String s2 = "name";
    assertTrue(p.p2(s1.toCharArray(), s2.toCharArray()));
  }

  @Test
  public void test_p2_false(){
    P2 p = new P2();
    String s1 = "chicken";
    String s2 = "notchicken";
    assertFalse(p.p2(s1.toCharArray(), s2.toCharArray()));
  }

  @Test
  public void test_p3_small(){
    P3 p = new P3();
    String s2 = "Mr John Smith    ";
    int len = 13;
    assertArrayEquals("Mr%20John%20Smith".toCharArray(),p.p3(s2.toCharArray(),len));
  }

  @Test
  public void test_p3_long(){
    P3 p = new P3();
    String s2 = "This is a test to urlify a long string with many spaces                      ";
    int len = 55;
    assertArrayEquals("This%20is%20a%20test%20to%20urlify%20a%20long%20string%20with%20many%20spaces".toCharArray(), p.p3(s2.toCharArray(),len));
  }

  @Test
  public void test_p4_nospaces(){
    P4 p = new P4();
    String s1 = "rraacce";//race car
    assertTrue(p.p4(s1));
  }

  @Test
  public void test_p4_manyspaces(){
    P4 p = new P4();
    String s1 = "Are we not pure? “No, sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man—a prisoner up to new era.";//race car
    assertTrue(p.p4(s1));
  }

  @Test
  public void test_p5_insert(){
    P5 p = new P5();
    String s1 = "indescribable";
    String s2 = "indscribable";
    assertTrue("Fail indescribable",p.p5(s1,s2));
  }

  @Test
  public void test_p5_remove(){
    P5 p = new P5();
    String s1 = "chicken";
    String s2 = "achicken";
    assertTrue("Fail chicken", p.p5(s1,s2));
  }

  @Test
  public void test_p5_replace(){
    P5 p = new P5();
    String s1 = "floofy";
    String s2 = "flooty";
    assertTrue(p.p5(s1,s2));
  }

  @Test
  public void test_p6(){
    P6 p = new P6();
    String s1 = "aabcccccaaa";
    String ans = "a2b1c5a3";
    assertEquals(ans, p.p6(s1));
  }
}
