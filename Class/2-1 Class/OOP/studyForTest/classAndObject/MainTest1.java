class Student {

    private String name;
    private int age;

    static String schoolName = "영진전문대";

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void introduce() {
        System.out.println("이름: " + name + ", 나이: " + age + ", 학교: " + schoolName);
    }

    public static void changeSchool(String newName) {
        schoolName = newName;
    }


}


public class MainTest1 {
    public static void main(String[] args) {
        Student s1 = new Student("철수", 20);
        Student s2 = new Student("영희", 21);

        s1.introduce();
        s2.introduce();

        Student.changeSchool("영진전문대학교");

        s1.introduce();
        s2.introduce();
    }
}
