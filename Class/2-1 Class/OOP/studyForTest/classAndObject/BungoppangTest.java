class Bungoppang {
    String filling;

    Bungoppang(String filling) {
        this.filling = filling;
    }

    void printInfo() {
        System.out.println("이 붕어빵의 속은 " + filling + "입니다.");
    }
}


public class BungoppangTest {
    public static void main(String[] args) {
        Bungoppang redBean = new Bungoppang("팥");
        Bungoppang cream = new Bungoppang("크림");

        redBean.printInfo();
        cream.printInfo();

    }
}
