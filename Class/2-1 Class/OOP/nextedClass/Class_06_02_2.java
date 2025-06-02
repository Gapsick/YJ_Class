package nextedClass;
interface myInterface { void prt(); };

class Outer0602 {
    int outer_val = 1;

    void getSomething() {
        class test implements myInterface {

            public void prt() {
                int local_val = 2;
                System.out.println(outer_val + local_val);
            }
        }

        test test = new test();
        test prt();
    }
}

public class Class_06_02_2 {
    public static void main(String[] args) {
        myInterface f = new Outer().prtSomething();
    }
}
