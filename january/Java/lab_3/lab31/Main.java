package lab31;

public class Main {
    public static void main(String[] args) {
        PublicTransport transport = new PublicTransport("��������",15,56);
        PublicTransport transport1 = new PublicTransport();
        System.out.println("����������� ��� ����������: " + transport1.toString());
        System.out.println("����������� � �����������: " + transport.toString());
        transport.input();
        transport.print();
    }
}
