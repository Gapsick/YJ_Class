
// Inheritance (상속)
// 부모 클래스로부터 멤버들을 물려 받는다
// 다중상속: 부모 클래스가 2개 이상
// 단일상속: 부모 클래스가 반드시 1개
//
class Student1 {
    int id = 2;
    String name = "Student";
    int age = 30;
}

class GscStudent extends Student1 {
    int id = 20;
    String name = "GscStudent";
    GscStudent() {
        System.out.println("id: " + this.id + ", name: " + super.name + ", age: " + age);
    }
}

public class Class_04_02 {
    static void main (String[] args) {
        GscStudent s = new GscStudent();
    }
}
