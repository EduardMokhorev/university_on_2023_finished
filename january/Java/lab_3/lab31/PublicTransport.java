package lab31;


import java.util.Scanner;

public class PublicTransport {
    private String owner;
    private int ticketCosts;
    private int numberOfPassengerSeats;

    //конструктор
    public PublicTransport(String owner, int ticketCosts, int numberOfPassengerSeats) {
        this.owner = owner;
        this.ticketCosts = ticketCosts;
        this.numberOfPassengerSeats = numberOfPassengerSeats;

    }

    //конструктор без параметров
    public PublicTransport() {
        this.owner = "владелец";
        this.ticketCosts = 60;
        this.numberOfPassengerSeats = 15;
    }

    //геттеры
    public String getOwner() {
        return this.owner;
    }

    public int getTicketCosts() {
        return this.ticketCosts;
    }

    public int getNumberOfPassengerSeats() {
        return this.numberOfPassengerSeats;
    }

    //сеттеры
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
        System.out.println("введите владельца");
        this.owner = scanner.next();
        System.out.println("введите стоимость проезда");
        this.ticketCosts = scanner.nextInt();
        System.out.println("введите количество пассажирских мест");
        this.numberOfPassengerSeats = scanner.nextInt();
    }
    public void print() {
        System.out.println("Object:");
        System.out.println(this.toString());
    }

    @Override
    public String toString() {
        return "владелец: " + this.getOwner() + " ,стоимость проезда: " + this.getTicketCosts() +  " ,кол-во посадочных мест: " + this.getNumberOfPassengerSeats();
    }

}
