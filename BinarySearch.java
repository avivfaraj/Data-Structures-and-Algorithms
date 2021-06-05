/***************************************
 * BinarySearch.java
 * Implementation of Binary search
 * @author Aviv Farag
 * @version 1.0
 ****************************************/

public class BinarySearch{

  public static void main (String args[]){

        // Initialization
        int[] arr = {1,2,3,4,5,6,7,20,30};

        // Element we are looking for
        int look_for = 29;

        // Next index
        int next = -1;

        // Maximum and minimum range
        int max = arr.length, min = 0;

        // Element found or not
        boolean found = false;

        // Iterate if not found
        while (!found)
        {
            // Next index 
            next = Math.round((max + min )/2);

            // If item does not exist
            if (next == max || next == min) 
            {
                // Stop loop
                break;
            }

            // Item exists
            else
            {
                // Ensure element is greater than look_for
                if (arr[next] > look_for)
                    // define new maximum index
                    max = next;

                // Ensure element is smaller than look_for 
                else if (arr[next] < look_for)
                    // Define new minimum index
                    min = next;

                // Ensure element is equal to look_for
                else
                    // Stop iteration
                    found = true;
                System.out.println(next);
            }
        }

        // Ensure item was found
        if(!found)
            System.out.println("Not Found " + (next+1));
        else
            System.out.println(look_for + " Was found at index: " + next);

    }
}