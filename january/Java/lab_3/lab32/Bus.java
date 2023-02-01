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

    //�������
    public boolean getHaveConductor() {
        return this.haveConductor;
    }
    public CarBrand ypeOfCommand() {
        return this.carBrand;
    }

    //�������
    public void setHaveConductor(boolean haveConductor) {
        this.haveConductor = haveConductor;
    }

    public void setCarBrand(CarBrand carBrand) {
        this.carBrand = carBrand;
    }

    @Override
    public String toString() {
        return "�������: " + super.toString() + " ���� �� ���������: " + this.haveConductor + " ����� ������: " + this.carBrand;
    }

    public void input() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("������� ���������");
        super.setOwner(scanner.next());
        System.out.println("��� ���������� ����");
        super.setNumberOfPassengerSeats(scanner.nextInt());
        System.out.println("��������� ������");
        super.setTicketCosts(scanner.nextInt());
        System.out.println("������� ����������");
        this.haveConductor = scanner.nextBoolean();

        System.out.println("������� ����� ������(����� �� 1 �� " + (CarBrand.values().length-1) + ")");
        CarBrand[] values = CarBrand.values();

        for (int i = 0; i < values.length; i++) {
            System.out.println(values[i].name() + " - " + values[i].ordinal());
        }

        int indexEnum = scanner.nextInt();

        while (indexEnum > (values.length -1)  || indexEnum < 0) {
            System.out.println("������� ������ �����");
            indexEnum = scanner.nextInt();
        }

        this.carBrand = values[indexEnum];

    }
    public void print() {
        System.out.println("Object:");
        System.out.println(this.toString());
    }
}
