import java.util.Scanner;

public class Methods
{
    public static void getRequirements() 
    {
        //display operational messages
        System.out.println("Developer: Jancarlo Rojas");
        System.out.println("Program prompts the user for first name and age, then prints the results.");
        System.out.println("Create four methods from the following requirements:");
        System.out.println("1) getRequirements(): Void method displays program requirements.");
        System.out.println("2) getUserInput(): Void method prompts for user input, \n\tthen calls two methods:myVoidMethod() and myValueReturningMethod().");
        System.out.println("3) myVoidMethod():\n" +
        "\ta. Accepts two arguments: String and int. \n" +
        "\tb. Prints user's first name and age.");
        System.out.println("4) myValueReturningMethod():\n" +
        "\ta. Accepts two arguments: String and int. \n" +
        "\tb. Returns String containing first name and age.");
        System.out.println(); //print blank line

        
    }

    public static void getUserInput() {
        //initialize variables, create Scanner object, capture user input
        String firstName="";
        int userAge = 0;
        String myStr="";
        Scanner sc  = new Scanner(System.in);

        //input
        System.out.print("Enter first name: ");
        firstName=sc.next();

        System.out.print("Enter age: ");
        userAge = sc.nextInt();

        System.out.println(); // print blank line

        //Note: done for simplicity--method/function calls *should* go back to their calling environment
        //call void method
        System.out.print("void method call: ");
        myVoidMethod(firstName, userAge);

        //call value-returning method
        System.out.print("value-returning method call: ");
        myStr = myValueReturningMethod(firstName, userAge);
        System.out.println(myStr);

        //myValueReturningMethod(firstName, userAge); // works, but discarded!
     }
    
    //Note: both methods use *same* named parameters-- which are *local* variables!
    //Also, both methods are static-- that is, can be used w/o instantiating objects
    public static void myVoidMethod(String first, int age) {
        System.out.println(first + " is " + age);
        //return; //OK with or without return statement
     }
    
    public static String myValueReturningMethod(String first, int age) {
        //not: implicit string conversion of age (int)
        return first + " is " + age;
     }

    public static void generatePseudoRandomNumbers(int[] userArray) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'generatePseudoRandomNumbers'");
    }

    public static int[] createArray() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'createArray'");
    }

    
}