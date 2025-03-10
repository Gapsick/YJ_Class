class Student {
    // 데이터 + 함수
    int korean;
    int math;
    int english;
    int sum;
    final int NUM_OF_SUBJECT = 3;

    int id;
    String name;
    
    void setGrade(int argKorean, int argMath, int argEnglish) {
        korean = argKorean;
        math = argMath;
        english = argEnglish;
        sum = korean + math + english;
    }
     
    double getSum() {
        return sum;
    }
    
    int getId() {
        return id;
    }
    
    String getName() {
        return name;
    }
    
    double getAvg() {
        return sum / NUM_OF_SUBJECT;
    }
}
class Bar {

    String name;
    int age;

    // 생성자: 이름이 클래스명과 동일
    Bar(String argName, int argAge) {
        argName = name;
        argAge = age;

    }

    void printInfo() {
        System.out.println(name);
    }

}

// 실행 코드
public class Class03_10 {
    public static void main(String[] args) {

        Bar b1 = new Bar("Richard");

        System.out.println(b1.name + " " + b1.age);


    }

}
