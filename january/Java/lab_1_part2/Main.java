package lab12;

import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean flag;
        flag = true;
        // add values
        System.out.println("add value a");
        int a = scanner.nextInt();

        System.out.println("add value b");
        int b = scanner.nextInt();

        System.out.println("add value u");
        int u = scanner.nextInt();

        System.out.println("add value x");
        int x = scanner.nextInt();

        //check

        if (b < a) {
            int r = a;
            a = b;
            b = r;
        }

        if (Math.tan(x) == 0) {
            System.out.println("can't devide to zero");
            System.exit(0);
        }

        if (5*x == 0){
            System.out.println("can't devide to zero");
            System.exit(0);
        }

        if (u - Math.pow(x, 2) < 0) {
            System.out.println("it is impossible to take the root of a negative number");
            System.exit(0);
        }

        if (x < 0) {
            System.out.println("it is impossible to square a negative number");
            System.exit(0);
        }

     // solutions
            double result;
            if (x < a) {
                result = Math.log(x+(u/(5*x)));
            }
            else if (x >= a | x <= b) {
                result = Math.sqrt(u - Math.pow(x, 2));
            } else {
                result = (x + 5) / Math.tan(x);

            System.out.println("result: ");
            System.out.println(result);
        }
    }
}
