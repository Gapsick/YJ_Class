package nextedClass;

interface Test09 {
    void print();
}
public class Class_06_09_02 {
    public static void main(String[] args) {
//        //         1) class 이름없음 extends Object  {
//        //            }
//        //         2) new 이름없음();
//        Object obj = new Object() {};
//
//        interface Test {};
//        //         1) class 이름없음 implements Test  {
//        //            }
//        //         2) new 이름없음();
//        Test test = new Test() {};
        Test09 test = new Test09() {
            @Override
            public void print() {
                System.out.println("Hello World");
            }
        };



    }
}
