interface EngineBracket1 {
    void start();
    void stop();
}

class BenzEngine1 implements EngineBracket1 {
    public void start() {
        System.out.println("Benz 시동 켜짐");
    }
    public void stop() {
        System.out.println("Benz 시동 꺼짐");
    }
}


public class Final_exam_06_24 {
    public static void main(String[] args) {
        EngineBracket1 engine = new BenzEngine1();
        engine.start();
    }
}
