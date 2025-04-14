// 반환형, 이름, 매개변수가 부모에서 정의된 메소드와 일치
// 예외, 접근제어자

class Bar {
    private int score;
    void prt() { System.out.println(); }

    // Getter, Setter Method
    int getScore() { return score; }
    boolean setScore(int newScore) {
        if(newScore >= 0 && newScore <= 100) {
            score = newScore;
            return true;
        }
        return false;
    }
}


public class Class_04_14 {
    public static void main(String[] args) {
        // 다형성 -> 참조 변수
        // 부모형으로 자식의 객체를 가리킬 수 있다.
        Bar b = new Bar();





    }
}
