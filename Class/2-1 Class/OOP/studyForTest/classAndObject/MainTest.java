class Bar {
    int myId;           // 인스턴스 변수
    static int value;   // 클래스 변수
    static int count;   // 클래스 변수

    void setValue(int argValue) {
        value = argValue;
    }

    Bar() {
        myId = count++;  // myId에 count를 대입하고, count를 1 증가시킴
    }
}

public class MainTest {
    public static void main(String[] args) {
        Bar b1 = new Bar();
        Bar b2 = new Bar();
        Bar b3 = new Bar();

        b3.setValue(10);

        System.out.println(b1.myId + ":" + b1.value);
        System.out.println(b2.myId + ":" + b2.value);
        System.out.println(b3.myId + ":" + b3.value);
    }
}
