package nextedClass;

interface bracket { void prt(); }

class Outer {
    bracket getObject() {
        class Test implements bracket {
            public void prt() { }

        }

        Test test = new Test();

        return test;
    }

}

public class Class_05_28 {
    public static void main(String[] args) {
        bracket b = new Outer().getObject();

    }
}
