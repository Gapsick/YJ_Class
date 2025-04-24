class Car1 {
    String brand;
    int speed;

    Car1() {
        this.brand = "Unknown";
        this.speed = 0;
        System.out.println("기본 생성자로 객체 생성");
    }

    Car1(String brand) {
        this.brand = brand;
        this.speed = 0;
        System.out.println("브랜드 지정: " + brand);
    }

    Car1(String brand, int speed) {
        this.brand = brand;
        this.speed = speed;
        System.out.println("브랜드: " + brand + ", 속도: " + speed + "km/h");
    }

}





public class OverloadingExamMain {
    public static void main(String[] args) {
        Car1 car1 = new Car1();
        Car1 car2 = new Car1("Hyundai");
        Car1 car3 = new Car1("BMW", 120);

    }
}
