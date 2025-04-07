class A {
    A() { System.out.println("A 생성자 호출"); }
}
class B extends A {
    B() { System.out.println("B 생성자 호출"); }
    B(int m, boolean n) { System.out.println("hi"); }
}
class C extends B {
    C() {
        System.out.println("C () 생성자 호출");
    }

    C(int m) {
        this();
        System.out.println("C (int m) 생성자 호출");
    }

    C(int m, int n) {
        this();
        System.out.println("C (int m, int n) 생성자 호출");
    }

}

public class Class_04_07 {
    public static void main(String[] args) {
        new C();
    }
}
