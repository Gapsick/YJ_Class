

// 자동차 클래스 (설계도)
class Car {
    // 필드(멤버 변수): 객체의 속성
    String brand;
    int speed;

    // 생성자: 객체가 만들어질 때 실행되는 초기화 코드
    Car(String brand, int speed) {
        this.brand = brand;
        this.speed = speed;
    }

    // 메서드(멤버 함수): 객체의 행동
    void accelrate() {
        speed += 10;
        System.out.println(brand + " 속도 증가: " + speed + "km/h");
    }

    void brake() {
        speed -= 10;
        System.out.println(brand + " 속도 감소: " + speed + "km/h");
    }
}

// 실행 코드
public class ObjectInstantiation {
    public static void main(String[] args) {
        // 객체 생성 (설계도로 자동차를 만드는 과정)
        Car car1 = new Car("Hyundai", 0);
        Car car2 = new Car("BMW", 20);

        // 객체의 메서드 호출 (자동차 운전)
        car1.accelrate();   // Hyundai 속도 증가: 10km/h
        car2.brake();       // BMW 속도 감소: 10km/h
    }
}
