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

    //геттеры
    public int getRating() {
        return this.rating;
    }

    //сеттеры
    public void setRating(int hour) {
        this.rating = hour;
    }

    @Override
    public String toString() {
        return "Такси: " + super.toString() + " рейтинг " + this.rating;
    }

    public void input() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("введите владельца");
        super.setOwner(scanner.next());
        System.out.println("кол посадочных мест");
        super.setNumberOfPassengerSeats(scanner.nextInt());
        System.out.println("Стоимость билета");
        super.setTicketCosts(scanner.nextInt());
        System.out.println("рейтинг");
        this.rating = scanner.nextInt();
    }
    public void print() {
        System.out.println("Object:");
        System.out.println(this.toString());
    }
}
