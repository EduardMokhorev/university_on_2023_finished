package lab32;

import lab31.PublicTransport;

import java.util.Scanner;

public class Taxi extends PublicTransport {
    private int rating;

    public Taxi(String owner, int ticketCosts, int numberOfPassengerSeats, int rating) {
        super(owner,ticketCosts,numberOfPassengerSeats);
        this.rating = rating;
    }

    public Taxi() {
        super();
        this.rating = 24;
    }

    //�������
    public int getRating() {
        return this.rating;
    }

    //�������
    public void setRating(int hour) {
        this.rating = hour;
    }

    @Override
    public String toString() {
        return "�����: " + super.toString() + " ������� " + this.rating;
    }

    public void input() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("������� ���������");
        super.setOwner(scanner.next());
        System.out.println("��� ���������� ����");
        super.setNumberOfPassengerSeats(scanner.nextInt());
        System.out.println("��������� ������");
        super.setTicketCosts(scanner.nextInt());
        System.out.println("�������");
        this.rating = scanner.nextInt();
    }
    public void print() {
        System.out.println("Object:");
        System.out.println(this.toString());
    }
}
