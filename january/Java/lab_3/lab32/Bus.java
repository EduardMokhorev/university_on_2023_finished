package lab32;

import lab31.PublicTransport;

import java.util.Scanner;

public class Bus extends PublicTransport {
    private boolean haveConductor;
    private CarBrand carBrand;

    public Bus(String owner, int ticketCosts, int numberOfPassengerSeats, boolean haveConductor, CarBrand carBrand) {
        super(owner,ticketCosts,numberOfPassengerSeats);
        this.haveConductor = haveConductor;
        this.carBrand = carBrand;
    }

    public Bus() {
        super();
        this.haveConductor = true;
        this.carBrand = CarBrand.NO_NAME;
    }

    //геттеры
    public boolean getHaveConductor() {
        return this.haveConductor;
    }
    public CarBrand ypeOfCommand() {
        return this.carBrand;
    }

    //сеттеры
    public void setHaveConductor(boolean haveConductor) {
        this.haveConductor = haveConductor;
    }

    public void setCarBrand(CarBrand carBrand) {
        this.carBrand = carBrand;
    }

    @Override
    public String toString() {
        return "Автобус: " + super.toString() + " есть ли кондуктор: " + this.haveConductor + " марка машины: " + this.carBrand;
    }

    public void input() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("введите владельца");
        super.setOwner(scanner.next());
        System.out.println("кол посадочных мест");
        super.setNumberOfPassengerSeats(scanner.nextInt());
        System.out.println("Стоимость билета");
        super.setTicketCosts(scanner.nextInt());
        System.out.println("наличие кондуктора");
        this.haveConductor = scanner.nextBoolean();

        System.out.println("Введите марку машины(число от 1 до " + (CarBrand.values().length-1) + ")");
        CarBrand[] values = CarBrand.values();

        for (int i = 0; i < values.length; i++) {
            System.out.println(values[i].name() + " - " + values[i].ordinal());
        }

        int indexEnum = scanner.nextInt();

        while (indexEnum > (values.length -1)  || indexEnum < 0) {
            System.out.println("введите другое число");
            indexEnum = scanner.nextInt();
        }

        this.carBrand = values[indexEnum];

    }
    public void print() {
        System.out.println("Object:");
        System.out.println(this.toString());
    }
}
