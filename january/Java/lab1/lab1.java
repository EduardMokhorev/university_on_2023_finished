import java.util.Scanner;
//Mokhorev Eduard Poz31 variant 11
//it needs to find the volume of a regular 3-sided pyramid
public class lab1 {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the height of the pyramid: "); //Высоту пирамиды
        double height = sc.nextDouble();
        if (height <=0){
            System.out.println("conditionally you must enter number > 0, program is closing");
            System.exit(0);
        }
        System.out.println("Enter the lenght base side : "); //длина стороны основания
        double baseSide = sc.nextDouble();
        if (baseSide <=0){
            System.out.println("conditionally you must enter number > 0, program is closing");
            System.exit(0);
        }
        double volume;
        if ((4*Math.sqrt(3)) == 0){
            System.out.println("dev.... zero");
            System.exit(0);
        }
        volume = ((height*(baseSide*baseSide))/(4*Math.sqrt(3))); //(h*a^2)/4*sqr(3)
        // site with online calculator for testes https://mnogoformul.ru/obem-piramidy
        System.out.println("Pyramid Volume = "+volume); //Обьем пирамиды
    }
}