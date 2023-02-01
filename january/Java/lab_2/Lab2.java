import java.util.Scanner;
    public class Lab2 {

    public static void main(String[] args) {
        int indexIfWeHaveMultiplicityFive = -1;
        int size = 0;
        Scanner input = new Scanner(System.in); // Scanner

        System.out.println("Enter array length, please: ");
        if (input.hasNextInt()) {
            size = input.nextInt();
        }
        else {
            System.out.println("conditionally you must enter an integer, program is closing");
            System.exit(0);
        }
        if (size<0){
            System.out.println("Please use integer >0, programm is closing");
            System.exit(0);
        }
        int array[] = new int[size]; // Создаём массив int размером в size
        System.out.println("Insert array elements:");

        /*Пройдёмся по всему массиву, заполняя его*/
        for (int i = 0; i < size; i++) {

            if (input.hasNextInt()) {
                array[i] = input.nextInt();
            }
            else {
                System.out.println("conditionally you must enter an integer, program is closing");
                System.exit(0);
            }

            //It is checking Multiplicity
            if (array[i] % 5 == 0) {
                indexIfWeHaveMultiplicityFive = i;
            }
        }
        System.out.print("Inserted array elements:");
        for (int i = 0; i < size; i++) {
            System.out.print(" " + array[i]); // show the resulting array
        }
        System.out.println();


        if (indexIfWeHaveMultiplicityFive != -1) {
            System.out.println("index of last multiple element = " + (indexIfWeHaveMultiplicityFive));
            System.out.println("Count numbers of elements after it = " + (array.length - indexIfWeHaveMultiplicityFive - 1));
        } else {
            System.out.println("Don't have elements ");
        }


    }
}
