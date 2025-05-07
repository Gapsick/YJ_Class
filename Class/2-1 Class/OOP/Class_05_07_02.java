interface Car0507 {
    void drive();
}

interface Airplane0507 {
    void drive();
}

interface Pos0507 extends Car0507, Airplane0507 {
}

class Kin0507 implements Pos0507 {
    @Override
    public void drive() {
        System.out.println("Kin drive");
    }
}

public class Class_05_07_02 {
}
