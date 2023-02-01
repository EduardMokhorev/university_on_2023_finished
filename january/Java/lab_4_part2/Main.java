// Удалить все лишние пробелы, ну и спереди и сзади тоже.
import java.util.Scanner;

public class Main {

    public static  Integer sum_number_in_string(String text){
        text = text.trim();
        String [] arr_text = text.split("");
        int sum_number_result = 0;
        System.out.println();

        //it is checking you text and sum number
        for(int i = 0; i < arr_text.length; i++){
            try {
                sum_number_result = sum_number_result + Integer.parseInt(arr_text[i]);
            } catch (Exception ex) {
                continue;
            }
    }
        return sum_number_result;
    }


    public static void main(String[] args) { //why????
        System.out.println("Put your text, please");
        Scanner input = new Scanner(System.in); // Scanner
        String text = input.nextLine();

        System.out.println("Sum number in your text = "+ sum_number_in_string(text));
    }
}