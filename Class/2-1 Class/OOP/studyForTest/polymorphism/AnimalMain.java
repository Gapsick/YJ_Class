class Animal1{
     void sound() {
        System.out.println("동물이 소리를 냅니다.");
    }
}

class Dog1 extends Animal1{
    @Override
    void sound() {
        System.out.println("강아지: 멍멍!");
    }
}

class Cat1 extends Animal1 {
    @Override
    void sound() {
        System.out.println("고양이: 야옹!");
    }
}

class Cow1 extends Animal1 {
    @Override
    void sound() {
        System.out.println("소: 음머~");
    }
}



public class AnimalMain {
    public static void main(String[] args) {
        Animal1[] animals = {
                new Dog1(),
                new Cat1(),
                new Cow1()
        };

        System.out.println("[ 동물 소리 내기 연습! ]");

        for (Animal1 a : animals) {
            a.sound();
        }



    }
}
