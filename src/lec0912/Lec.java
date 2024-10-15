package lec0912;

public class Lec {

    public static void main(String[] args) {

        final int bar = 10;

        // 리터럴 상수의 구조

        // 접두사 + 상수 값 + 접미사

        System.out.println(10);  // int
        System.out.println(10L); // long
        System.out.println(10.0f); // float
        System.out.println(10.0); // double
        System.out.println('1'); // char
        System.out.println(true); // boolean
        System.out.println(false); // boolean

        float pos = 2.0f + 3.0f;

        float kin = (float) (2.0 + 3.0);

        byte bar1 = 127; // overflow
        bar1++; // bar = bar + 1
        System.out.println(bar1);

        bar1 = -128; // underflow
        bar1--; // bar = bar - 1
        System.out.println(bar1);

        long pos1 = (long)2147483647 + 2;
        System.out.println(pos1);

        double kin1 = (450 + 3) / 2.0;

        System.out.println(kin1);





    }
}
