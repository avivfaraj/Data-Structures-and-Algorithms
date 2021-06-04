
/***************************************
 * SelectionSort.java
 * Calculates the amount to be paid by each friend.
 * 
 * @author Aviv Farag
 * @version 1.0
 ****************************************/

public class SelectionSort{

  public static void main (String args[]){

    // Variables initalization
    int[] arr = {1,4,2,5,3,9,7,8,6};
    int temp;
    int min; 

    // Outer for loop to iterate over elements
    for (int index = 0; index < arr.length-1; index++)
    {

        // Set minimum to current index
        min = index;

        // Inner loop to iterate sub-array to find next mininmum
        for (int inner = index + 1; inner < arr.length; inner++)
        {
            // Ensure the next element is smaller
            if (arr[inner] < arr[min])
            {
                // Save its index
                min = inner;
            }
        }

        // Swap elements in the array
        temp = arr[index];
        arr[index] = arr[min];
        arr[min] = temp;
    }

    // Print sorted array
    for (int num : arr)
    {
        System.out.print(num);
    }
    System.out.println();
  }
}