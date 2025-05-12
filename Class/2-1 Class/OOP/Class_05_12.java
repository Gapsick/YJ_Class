// 예외 전파 흐름 확인용 클래스
class Bar0512 {
    // level1 호출 -> 내부족으로 level2 호출
    void level1() {
        level2();   // 호출 스택: level1 -> level2
    }

    // level2 호출 -> 내부적으로 level3 호출
    void level2() {
        level3();
    }

    // level3에서 예외 발생
    void level3() {
        // RuntimeException은 Unchecked Exception
        // 예외를 처리하지 않고 그대로 던지므로 호출한 꼭으로 전달됨
        throw new RuntimeException("예외 발생 위치: level3()");
    }
}

// main 클래스
public class Class_05_12 {
    public static void main(String[] args) {
        // Bar 클래스의 level1()을 호출 -> 결국 level3()에서 예외 발생
        new Bar0512().level1();

        // 예외가 발생하면 아래 코드는 실행되지 않고 프로그램은 비정상 종료됨
        System.out.println("이 코드는 실행되지 않습니다.");
    }
}
