// 지금부터 클래스를 정의 할꺼야
class Car {
    // Data + Function
    // Data -> Member variable (멤버 변수)
    String name;

    // Function -> Member method (멤버 메서드)
    void prtName() {
        System.out.println(name);
    }

}

public class MainTest {
    public static void main(String[] args) {

        int bar[] = new int[5];

        Car car1 = new Car();
        Car car2 = new Car();

        car2.name = "Tesla";

        car2.prtName();


    }
}
