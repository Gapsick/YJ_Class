package nextedClass;

class Outer0601 {
    int outer_val = 1;
//    void prt() {
//        System.out.println(inner_val);
//    }

    class Inner0601 {
        int inner_val = 1;

        void prt() {
            System.out.println(outer_val);
        }
        void set_val(int val) {
            outer_val = Outer0601.this.outer_val;
        }
    }

}


public class Class_06_02 {
    public static void main(String[] args) {
        Outer0601 outer1 = new Outer0601();
        Outer0601.Inner0601 inner1 = outer1.new Inner0601();
        Outer0601.Inner0601 inner2 = outer1.new Inner0601();

        inner1.set_val(3);
        inner2.prt();


    }
}
