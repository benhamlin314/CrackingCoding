/**
* Implementation of LinkedList for this problem
* @author Benjamin Hamlin
* @version "1.0, 12/26/19"
*/
public class MyLinkedListNode<T>{
  private T data;
  private MyLinkedListNode<T> next;

  /**
  * Constructor of My LinkedList
  * @param data The data to be stored in this node
  */
  public MyLinkedListNode(T data){
    this.data = data;
    this.next = null;
  }

  /**
  * Gets the data contained in the node
  * @return The data contained
  */
  public T GetData(){
    return this.data;
  }

  /**
  * Set data of node
  * @param data data to be set
  */
  public void SetData(T data){
    this.data = data;
  }

  /**
  * Set next
  * @param next Next node
  */
  public void SetNext(MyLinkedListNode<T> next){
    this.next = next;
  }

  /**
  * Gets the next node
  * @return the next node
  */
  public MyLinkedListNode<T> next(){
    return this.next;
  }

  public String myToString(){
    StringBuilder builder = new StringBuilder();
    MyLinkedListNode<T> cur = next;
    builder.append('[');
    builder.append(this.data);
    builder.append(',');
    while(cur.next() != null){
      builder.append(cur.GetData());
      builder.append(',');
      cur = cur.next();
    }
    builder.append(cur.next().GetData());
    builder.append(']');
    return builder.toString();
  }
}
