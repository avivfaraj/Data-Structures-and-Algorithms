/***************************************
 * InsertionSort.java
 * Sorting numbers using Insertion sort
 * @author Aviv Farag
 * @version 1.0
 ****************************************/

public class InsertionSort{

  public static void main (String args[]){

    int[] arr = {1,4,2,5,3,9,7,8,6};

    boolean sorted = false;
    int temp = -1;
    int index = 0,counter = -1;

    while (index < arr.length-1)
    {
        if (arr[index + 1] < arr[index])
        {
            if(index == 0){
                temp = arr[index + 1];
                arr[index + 1] = arr[index];
                arr[index] = temp;
            }
            else
            {
                sorted = false;
                temp = arr[index + 1];
                System.out.println(temp);
                // counter = index;
                while(!sorted)
                {
                    if (arr[index] > temp)
                    {
                        // temp = arr[index + 1];
                        arr[index + 1] = arr[index];
                        index--;
                    }
                    else
                    {
                        arr[index + 1] = temp;
                        sorted = true;
                        index = index + 1;
                    }
                    
                }
            }  
        }

        index++;
    }

    for (int num : arr)
    {
        System.out.print(num);
    }
    System.out.println();

  // }
}
}