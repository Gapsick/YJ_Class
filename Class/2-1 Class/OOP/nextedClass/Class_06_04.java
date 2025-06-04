package nextedClass;

interface Test { void print(); }

class Outer04 {
    int outer_val = 1;

    Test prt() {
        // Effectively constant
        int local_val = 2;
        class Inner04 implements Test {
            public void print() {
                System.out.println(outer_val);
                System.out.println(local_val);
            }
        }
        return new Inner04();
    }
}

public class Class_06_04 {
    public static void main (String[] args) {
        Outer04 outer = new Outer04();
        Test test = outer.prt();

        test.print();

    }
}
