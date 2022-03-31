/***************************************
 * LinearSearch.java
 * Implementation of Linear search
 * @author Aviv Farag
 * @version 1.0
 ****************************************/

public class LinearSearch{

  public static void main (String args[]){

    // Initialization
    int[] arr = {1,4,2,5,3,9,7,8,6};
    int index = -1,counter = 0;
    boolean found = false;

    // Number to search in the array
    int look_for = 10;

    // Iterate over the array
    while (counter < arr.length && !found)
    {
        // Ensure element is equal look_for
        if (arr[counter] == look_for )
        {
            // Save index
            index = counter;

            // Stop loop
            found = true;
        }

        // Increment counter 
        counter++;
    }

    // Ensure item exist
    if (index != -1)
        // Print a msg
        System.out.println(look_for +" was found at index: "+index);
    else
        // Item does not exist 
        System.out.println(look_for +" does not exist");
}
}