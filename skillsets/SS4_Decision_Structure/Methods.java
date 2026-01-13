

import java.util.Scanner;

public class Methods
{
    public static void getRequirements() 
    {
        //display operational messages
        System.out.println("Developer: Jancarlo Rojas");
        System.out.println("Program evaluates user-entered characters.");
        System.out.println("Use following characters: W or w, C or c, H or h, N or n.");
        System.out.println("Use following decision structures: if...else, and switch.");
        System.out.println(); //print blank line

        System.out.println("Phone types: W or w (work), C or c (cell), H or h (home), N or n (none).");
    }

    public static void decisionStructures() {
            
        //initialize variables, create Scanner object, capture user input
        char charEntered = 0;
        Scanner sc = new Scanner(System.in); {

        System.out.print("Enter phone type: ");
        charEntered = sc.next().charAt(0); //capture user input
        System.out.println(); //prints blank line

    
        // for if...else statement
        System.out.println("if... else:");
        //System.out.print("Phone type: ");

        if (charEntered == 'W' || charEntered == 'w') {
            System.out.println("Phone type: work");
        }
        else if (charEntered == 'C' || charEntered == 'c') {
            System.out.println("Phone type: cell");
        }
        else if (charEntered == 'H' || charEntered == 'h') {
            System.out.println("Phone type: home");
        }
        else if (charEntered == 'N' || charEntered == 'n') {
            System.out.println("Phone type: none");
        }
        else {
            System.out.println("Incorrect character entry");
        }
        

        // for switch statement
        System.out.print("switch:");
        //System.out.print("Phone type: ");
        System.out.println(); //prints blank line

        switch (charEntered) {
            case 'w':
            System.out.println("Phone type: work");
                break;
            case 'W':
            System.out.println("Phone type: work");
                break;
            case 'c':
            System.out.println("Phone type: cell");
                break;
            case 'C':
            System.out.println("Phone type: cell");
                break;
            case 'h':
            System.out.println("Phone type: home");
                break;
            case 'H':
            System.out.println("Phone type: home");
                break;
            case 'n':
            System.out.println("Phone type: none");
                break;
            case 'N':
            System.out.println("Phone type: none");
                break;
            default:
            System.out.println("Incorrect character entry.");
                break;
        }
        
        }
        sc.close();



    }

}