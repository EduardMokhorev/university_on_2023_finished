/*
Определить есть ли столбец все эллементы которые одинаковые
Отсортировать главную диогональ по возврастанию
 */

import java.util.Arrays;
import java.util.Scanner;
public class lab22 {

    /*
1 2 3 4 5
1 5 3 6 8
7 4 3 8 1
4 2 3 9 5
1 2 3 4 5

    * */


    //Input and check integer
    public static int check() {
        while (true) {
            try {
                Scanner input = new Scanner(System.in);
                return input.nextInt();
            } catch (Exception ex) {
                System.out.println("Please input integer");
                continue;
            }
        }
    }



    public static void main(String[] args) {
        //Input array length
        System.out.println("Please input array length (n)");
        int n = check();
        while (n < 2){
            System.out.println("Please input integer > 1");
            n = check();
        }

        Scanner input = new Scanner(System.in);

          //Input array numbers
        int[][] arr = new int[n][n];
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
//                arr[i][j] = check();
                arr[i][j] = input.nextInt();
            }
        }



        //Show array
        System.out.println();
        System.out.println("Array");
        for (int[] anArr : arr) {
            for (int anAnArr : anArr) {
                System.out.print(anAnArr + " ");
            }
            System.out.println();
        }


        //It is checking similar elements
        System.out.println();
        System.out.println("Results");
        int count = 0;
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < n-1; i++) {
                if (arr[i][j] == arr[i+1][j]){
                    if (i == n-2){
                        System.out.println(j+" Column has similar elements");
                        count = count + 1;
                    }
                }
                else {break;}
            }
        }
        System.out.println("total number of recurrence cases of column recurrence count = " + count);



        //sort diogonal
        int temp = 0;
        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < n - 1; j++) {
                if (arr[j][j] > arr[j + 1][j + 1]) {
                    temp = arr[j + 1][j + 1];
                    arr[j + 1][j + 1] = arr[j][j];
                    arr[j][j] = temp;
                }
            }
        }

        //Show array
        System.out.println();
        System.out.println("Diagonal Array has been sorted");
        for (int[] a: arr) {
            System.out.println(Arrays.toString(a));
        }
//        for (int[] anArr : arr) {
//            for (int anAnArr : anArr) {
//                System.out.print(anAnArr + " ");
//            }
//            System.out.println();
//        }



    }



}

