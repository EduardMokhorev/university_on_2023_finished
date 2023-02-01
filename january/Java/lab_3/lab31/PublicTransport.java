package lab31;


import java.util.Scanner;

public class PublicTransport {
    private String owner;
    private int ticketCosts;
    private int numberOfPassengerSeats;

    //�����������
    public PublicTransport(String owner, int ticketCosts, int numberOfPassengerSeats) {
        this.owner = owner;
        this.ticketCosts = ticketCosts;
        this.numberOfPassengerSeats = numberOfPassengerSeats;

    }

    //����������� ��� ����������
    public PublicTransport() {
        this.owner = "��������";
        this.ticketCosts = 60;
        this.numberOfPassengerSeats = 15;
    }

    //�������
    public String getOwner() {
        return this.owner;
    }

    public int getTicketCosts() {
        return this.ticketCosts;
    }

    public int getNumberOfPassengerSeats() {
        return this.numberOfPassengerSeats;
    }

    //�������
    public void setOwner(String owner) {
        this.owner = owner;
    }

    public void setTicketCosts(int ticketCosts) {
        this.ticketCosts = ticketCosts;
    }

    public void setNumberOfPassengerSeats(int numberOfPassengerSeats) {
        this.numberOfPassengerSeats = numberOfPassengerSeats;
    }

    public void input() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("������� ���������");
        this.owner = scanner.next();
        System.out.println("������� ��������� �������");
        this.ticketCosts = scanner.nextInt();
        System.out.println("������� ���������� ������������ ����");
        this.numberOfPassengerSeats = scanner.nextInt();
    }
    public void print() {
        System.out.println("Object:");
        System.out.println(this.toString());
    }

    @Override
    public String toString() {
        return "��������: " + this.getOwner() + " ,��������� �������: " + this.getTicketCosts() +  " ,���-�� ���������� ����: " + this.getNumberOfPassengerSeats();
    }

}
