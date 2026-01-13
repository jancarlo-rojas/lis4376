import java.util.Scanner;

public class Methods
{
    public static void getRequirements() 
    {
        //display operational messages
        System.out.println("Developer: Jancarlo Rojas");
        System.out.println("Program evaluates the largest of three integers.");
        System.out.println("Note: Program checks for integers and non-numeric values.");
        System.out.println(); //print blank line
    }

    //value-returning method (static requires no object)
    public static void validateUserInput()
    {
        //declare variables and create Scanner object
        Scanner sc = new Scanner(System.in);
        int num1 = 0, num2 = 0, num3 = 0;

        //prompt user for three integers
        System.out.print("Please enter first number: ");
        while (!sc.hasNextInt())
        {
            System.out.println("Not valid integer!\n");
            sc.next(); 
            System.out.print("Please try again. Enter first number: ");
        }
        num1 = sc.nextInt();

        System.out.print("Please enter second number: ");
        while (!sc.hasNextInt())
        {
            System.out.println("Not valid integer!\n");
            sc.next(); 
            System.out.print("Please try again. Enter second number: ");
        }
        num2 = sc.nextInt();

        System.out.print("Please enter third number: ");
        while (!sc.hasNextInt())
        {
            System.out.println("Not valid integer!\n");
            sc.next(); 
            System.out.print("Please try again. Enter third number: ");
        }
        num3 = sc.nextInt();

        System.out.println();

        //Note: this solution is easy, however, return values should go back to the caller. Makes for easier debugging.
        getLargestNumber(num1, num2, num3);
    }

    public static void getLargestNumber(int num1, int num2, int num3)
    {
        System.out.println("Numbers entered: " + num1 + "," + num2 + "," + num3);

        if ( num1 > num2 && num1 > num3)
            System.out.println(num1 + " is largest.");
        else if ( num2 > num1 && num2 > num3)
            System.out.println(num2 + " is largest.");
        else if ( num3 > num1 && num3 > num2)
            System.out.println(num3 + " is largest.");
        else
            System.out.println("Integers are equal.");
    }

}