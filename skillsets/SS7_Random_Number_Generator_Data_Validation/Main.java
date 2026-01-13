public class Main
{
    public static void main(String[] args) 
    {
        //call static void methods (i.e., no object)
        Methods.getRequirements();

        int[]userArray = Methods.creatArray();

        Methods.generatePseudoRandomNumbers(userArray);
    }
}