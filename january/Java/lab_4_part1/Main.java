// Удалить все лишние пробелы, ну и спереди и сзади тоже.
import java.util.Scanner;

public class Main {


    public static StringBuilder delete_space (String text){
        text = text.trim();
        String [] arr_text = text.split("");
        StringBuilder result_text = new StringBuilder("");
        for(int i = 0; i < arr_text.length-1; i++){
            if (arr_text[i].equals(" ") && arr_text[i+1].equals(" ")){
                continue;
            }
            result_text.append(arr_text[i]);
        }
        result_text.append(arr_text[arr_text.length-1]);
        return result_text;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in); // Scanner
        System.out.println("put in your text");
        String text = input.nextLine();
        System.out.println("result text");
        System.out.println(delete_space(text));
    }
}
