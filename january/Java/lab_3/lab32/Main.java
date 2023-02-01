package lab32;



public class Main {
    public static void main(String[] args) {
        Bus bus = new Bus( "владелец", 60, 45, true, CarBrand.MAZ);
        Bus busN34 = new Bus();
        System.out.println("конструктор с параметрами: " + bus.toString());
        System.out.println("конструктор без параметров: " + busN34.toString());
        bus.input();
        bus.print();

        Taxi taxiMaxim = new Taxi("Витя",42,1,5);
        Taxi taxiYandex = new Taxi();
        System.out.println("конструктор без параметров: " + taxiYandex.toString());
        System.out.println("конструктор с параметрами: " + taxiMaxim.toString());
        taxiMaxim.input();
        taxiMaxim.print();
    }
}
