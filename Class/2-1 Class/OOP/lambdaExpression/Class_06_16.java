package lambdaExpression;
import java.util.ArrayList;
import java.util.function.Consumer;

class Person {
    String name;
    int age;
    Person(String name, int age) { this.name = name; this.age = age; }
}

public class Class_06_16 {
    public static void main(String[] args) {

        // Collection Framework : package for Data Structure
        ArrayList<Person> list = new ArrayList<>();

        list.add(new Person("John", 20));
        list.add(new Person("Jane", 31));
        list.add(new Person("Jack", 41));
        list.add(new Person("Jill", 51));

        Consumer<Person> prt = (obj) -> System.out.println(obj.name + ":" + obj.age);

        list.stream().filter((obj) -> obj.age > 30).forEach(prt);

    }
}
