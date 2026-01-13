import java.util.Scanner;

public class Methods
{

    static final Scanner sc = new Scanner(System.in);
    public static void getRequirements() 
    {
        //display operational messages
        System.out.println("Developer: Jancarlo Rojas");
        System.out.println("1) Program creates array size run-time.");
        System.out.println("2) Program displays array size.");
        System.out.println("3) Program rounds sum and average of numbers to two decimal places.");
        System.out.println("4) Numbers *must* be float data type, not double.");
       
        System.out.println(); //print blank line
    }

    //value-returning method (statis requires no object)
    public static int validateArraySize()
    {
        //declare variables and create Scanner object
        //Scanner sc = new Scanner(System.in);
        int arraySize = 0;

        //prompt user for array size
        System.out.print("Please enter array size: ");
        while(!sc.hasNextInt())
        {
            System.out.println("Not valid integer!\n");
            sc.next();
            System.out.print("Please try again. Enter array size: ");
        }
        arraySize = sc.nextInt();
        System.out.println(); // print blank line

        //return array size to calling environment
        return arraySize;
    }

    //non-value-returning method (static requires no object)
    public static void calculateNumbers(int arraySize)
    {
        float sum = 0.0f;
        float average = 0.0F;

        //indicate number of values required baed on user input
        System.out.print("Please enter " + arraySize + " numbers.\n");

        //create array for sotring user input, based on user-entered array size
        float numsArray[] = new float[arraySize];

        //validate data entry
        for(int i = 0; i < arraySize ; i++)
            {
                System.out.print("Enter num " + (i+1) + ": ");

                while (!sc.hasNextFloat())
                {
                    System.out.println("Not valid number!\n");
                    sc.next();
                    System.out.print("Please try again. Enter num " + (i + 1) + ": ");
                }
                numsArray[i] = sc.nextFloat(); //capture validated user input
                sum = sum + numsArray[i]; //process data entry
            }

            average = sum / arraySize;

            //print numbers entered
            System.out.print("\nNumbers entered: ");
            for (int i = 0; i < numsArray.length; i++)
            {
                System.out.print(numsArray[i] +" ");
            }

            //call method to print and format numbers
            printNumbers(sum, average);
    }

    //non-value-returning method (static requires no object)
    public static void printNumbers(float sum, float average)
    {
        System.out.println("\nSum: " + String.format("%.2f", sum));
        System.out.println("Average: " + String.format("%.2f", average));
    }

}