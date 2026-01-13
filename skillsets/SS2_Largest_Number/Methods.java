package skillsets.SS2_Largest_Number;

import java.util.Scanner;

public class Methods {

    public static void getRequirements() {
        System.out.println("Developer: Jancarlo Rojas");
        System.out.println("Program evaluates largest of two numbers");
        System.out.println("Note: Program does NOT check for non-numeric characters unless using getNum().");
        System.out.println();
    }

    public static int getNum() {
        Scanner sc = new Scanner(System.in);
        while (true) {
            try {
                return sc.nextInt();
            } catch (Exception e) {
                System.out.print("Invalid input. Please enter an integer: ");
                sc.nextLine(); // clear invalid input
            }
        }
    }

    public static void evaluateNumber(int num1, int num2) {
        System.out.println();
        if (num1 > num2)
            System.out.println(num1 + " is larger than " + num2);
        else if (num2 > num1)
            System.out.println(num2 + " is larger than " + num1);
        else
            System.out.println("Integers are equal");
    }

    // Optional original version using internal input logic
    public static void largestNumber() {
        int num1, num2;
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter First Integer: ");
        num1 = sc.nextInt();

        System.out.print("Enter Second Integer: ");
        num2 = sc.nextInt();

        System.out.println();
        if (num1 > num2)
            System.out.println(num1 + " is larger than " + num2);
        else if (num2 > num1)
            System.out.println(num2 + " is larger than " + num1);
        else
            System.out.println("Integers are equal");

        sc.close();
    }
}
