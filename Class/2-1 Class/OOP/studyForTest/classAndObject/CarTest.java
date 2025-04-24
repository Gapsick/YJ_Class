class Car {
    String brand;
    int speed;

    Car(String brand, int speed) {
        this.brand = brand;
        this.speed = speed;
    }

    void accelerate() {
        speed += 10;
        System.out.println(brand + "속도증가: " + speed + "km/h");
    }

    void brake() {
        speed -= 10;
        System.out.println(brand + " 속도 감소: " + speed + "km/h");
    }

}

public class CarTest {
    public static void main(String[] args) {
        Car car1 = new Car("Hyundai", 0);
        Car car2 = new Car("BMW", 20);

        car1.accelerate();
        car2.brake();
        car1.brake();
        car2.accelerate();
        car2.accelerate();

    }
}
