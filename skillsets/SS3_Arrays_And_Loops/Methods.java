package skillsets.SS3_Arrays_And_Loops;

public class Methods {

    // Predefined array of strings
    private static String[] animals = {"dog", "cat", "bird", "fish", "insect"};

    // Regular for loop
    public static void forLoop() {
        System.out.println("for loop:");
        for (int i = 0; i < animals.length; i++) {
            System.out.println(animals[i]);
        }
        System.out.println();
    }

    // Enhanced for loop
    public static void enhancedForLoop() {
        System.out.println("Enhanced for loop:");
        for (String animal : animals) {
            System.out.println(animal);
        }
        System.out.println();
    }

    // While loop
    public static void whileLoop() {
        System.out.println("while loop:");
        int i = 0;
        while (i < animals.length) {
            System.out.println(animals[i]);
            i++;
        }
        System.out.println();
    }

    // Do...while loop
    public static void doWhileLoop() {
        System.out.println("do...while loop:");
        int i = 0;
        do {
            System.out.println(animals[i]);
            i++;
        } while (i < animals.length);
        System.out.println();
    }
}
