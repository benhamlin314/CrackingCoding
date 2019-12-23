/**
 * Chapter 1 Question 3
 * "URLify"
 * PROMPT:
 * Write a method to replace all spaces in a string with '%20'.
 * You may assume that the string has sufficient space at the end to hold the additional characters,
 * and that you are given the 'true' length of the string
 * (Note: if implementing in java, please use a character array so that you can perform this operation in place)
 * DATE: 12/19/2019
 * @author Benjamin Hamlin
 * @version "1.0, 12/19/2019"
 */
public class P3{
  /**
  * Replaces spaces with '%20' for urls
  * @param s1 char array to be altered
  * @param len the 'true' length of the string
  * @return the urlified string as a char array
  */
  public char[] p3(char[] s1, int len){
    int index = 0;
    while(index < len){
      if(s1[index] == ' '){
        char temp1, temp2, temp3;
        s1[index++] = '%';
        temp1 = s1[index];
        s1[index++] = '2';
        temp2 = s1[index];
        s1[index++] = '0';
        len += 2;
        for(int i = index; i < len ; ++i){
          temp3 = s1[i];
          s1[i] = temp1;
          temp1 = temp2;
          temp2 = temp3;
        }
      }else{
        ++index;
      }
    }
    return s1;
  }
}
