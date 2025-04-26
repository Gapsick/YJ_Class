class Animal{
    String name;

    Animal(String name) {
        this.name = name;
    }

    void sound() {
        System.out.println(name + "가 소리를 낸다.");
    }
}

class Dog extends Animal{
    Dog(String name) {
        super(name);
    }

    @Override
    void sound() {
        System.out.println(name + "가 멍멍 짖는다.");
    }
}

class Cat extends Animal{
    Cat(String name) {
        super(name);
    }

    @Override
    void sound() {
        System.out.println(name + "가 야옹 운다.");
    }
}



public class MainAnimal {
    public static void main(String[] args) {
        Dog dog = new Dog("바둑이");
        Cat cat = new Cat("나비");

        dog.sound();
        cat.sound();

        // 부모 타입으로 참조
        Animal animal = new Dog("초코");
        animal.sound();

        Animal anotherAnimal = new Cat("하양이");
        anotherAnimal.sound();

    }
}
