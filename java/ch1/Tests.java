import org.junit.Test;
import static org.junit.Assert.*;

public class Tests{

  @Test
  public void test_p1_true(){
    p1 problem = new p1();
    assertTrue(problem.p1("adept"));
  }

  @Test
  public void test_p1_false(){
    p1 problem = new p1();
    assertFalse(problem.p1("adapt"));
  }
}
