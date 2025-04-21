

class A1{
    int x = 2;
}
class B1 extends A1{ int y = 3; }
class C1 extends B1{ int z = 4; }

public class Class_04_21 {

    public static void main(String[] args) {

        A1 bar = new B1();

        if (bar instanceof C1) {
           System.out.println("This is a C");
        } else {
            System.out.println( ((B1)bar).y );
        }



    }
}
