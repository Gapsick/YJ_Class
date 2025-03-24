

// 붕어빵 클래스 (붕어빵을 만들기 위한 설계도)
class Bungeoppang {
    String filling; // 속 재료 (팥, 크림 등)

    // 생성자: 붕어빵 속을 설정
    Bungeoppang(String filling) {
        this.filling = filling;
    }

    // 붕어빵 정보 출력
    void printInfo() {
        System.out.println("이 붕어빵의 속은 " + filling + "입니다.");
    }

}
// 붕어빵 객체 생성 및 사용
public class MainTest {
    public static void main(String[] args) {
        Bungeoppang redBean = new Bungeoppang("팥"); // 팥 붕어빵 생성
        Bungeoppang cream = new Bungeoppang("크림");  // 크림 붕어빵 생성

        redBean.printInfo();    // "이 붕어빵의 속은 팥입니다."
        cream.printInfo();      // "이 붕어빵의 속은 크림입니다."
    }
}