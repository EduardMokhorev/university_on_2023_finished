package lab31;

public class Main {
    public static void main(String[] args) {
        PublicTransport transport = new PublicTransport("владелец",15,56);
        PublicTransport transport1 = new PublicTransport();
        System.out.println("конструктор без параметров: " + transport1.toString());
        System.out.println("конструктор с параметрами: " + transport.toString());
        transport.input();
        transport.print();
    }
}
