package skillsets.SS2_Largest_Number;

class Main {

    public static void main(String[] args) {
        Methods.getRequirements();
        Methods.largestNumber(); // Optional; can remove if you're only using manual input version

        int myNum1 = 0, myNum2 = 0;
        System.out.print("Enter First Int: ");
        myNum1 = Methods.getNum();

        System.out.print("Enter Second Int: ");
        myNum2 = Methods.getNum();

        Methods.evaluateNumber(myNum1, myNum2);
    }
}
