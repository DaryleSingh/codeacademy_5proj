// Importing the Random library
import java.util.Random;

class Magic8 {
  
  public static void main(String[] args) {
    
    String[] advice = {"A beautiful, smart, and loving person will be coming into your life", "A dubious friend may be an enemy in camouflage", "A faithful friend is a strong defense", "A fresh start will put you on your way"};  

    // Creating a random number generator
    Random randomGenerator = new Random();
    
    // Generate a number between 0 and 3
    int dieRoll = randomGenerator.nextInt(3);

    System.out.println(advice[dieRoll]);
    
    //I also did it with a switch statment as requested
    //but the above method is better.Same result

   switch(dieRoll) {
          case 0:
     System.out.println(advice[dieRoll]);
     break;
          case 1:
     System.out.println(advice[dieRoll]);
     break;
          case 2:
     System.out.println(advice[dieRoll]);
     break;
          case 3:
     System.out.println(advice[dieRoll]);
     break;
   }




    
  }
  
}