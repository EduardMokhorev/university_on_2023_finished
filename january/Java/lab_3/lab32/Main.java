package lab32;



public class Main {
    public static void main(String[] args) {
        Bus bus = new Bus( "��������", 60, 45, true, CarBrand.MAZ);
        Bus busN34 = new Bus();
        System.out.println("����������� � �����������: " + bus.toString());
        System.out.println("����������� ��� ����������: " + busN34.toString());
        bus.input();
        bus.print();

        Taxi taxiMaxim = new Taxi("����",42,1,5);
        Taxi taxiYandex = new Taxi();
        System.out.println("����������� ��� ����������: " + taxiYandex.toString());
        System.out.println("����������� � �����������: " + taxiMaxim.toString());
        taxiMaxim.input();
        taxiMaxim.print();
    }
}
