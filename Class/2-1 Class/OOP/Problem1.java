class Car {
    String color;
    int speed;

    void drive() {
        System.out.println("Driving at speed: " + speed);
    }
}


public class Problem1 {
    public static void main(String[] args) {
        Car car1 = new Car();
        car1.color = "Red";
        car1.speed = 10;

        Car car2 = new Car();
        car2.color = "Blue";
        car2.speed = 80;

        car1.drive();   // Red car
        car2.drive();   // Blue car
    }
}
