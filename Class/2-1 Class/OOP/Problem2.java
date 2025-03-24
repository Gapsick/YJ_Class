class Person {
    String name;
    int age;

    void introduce() {
        System.out.println("Hi, I'm " + name + "and I'm " + age + "years old.");
    }
}

public class Problem2 {
    public static void main(String[] args) {
        Person p1 = new Person();
        p1.name = "Alice";
        p1.age = 25;

        Person p2 = new Person();
        p2.name = "Bob";
        p2.age = 35;

        p1.introduce();
        p2.introduce();
    }
}
