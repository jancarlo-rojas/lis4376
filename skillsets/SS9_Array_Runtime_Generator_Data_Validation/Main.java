public class Main
{
    public static void main(String[] args) 
    {
        //call static methods (i.e., no object)
        Methods.getRequirements();

        //returns initialized array, array size determined by user
        int arraySize=0;
        arraySize = Methods.validateArraySize();

        //call method, passing returned array above
        //after processing, method calls another method
        Methods.calculateNumbers(arraySize);
    }
}