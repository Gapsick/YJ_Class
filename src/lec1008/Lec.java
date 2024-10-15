package lec1008;

public class Lec {
    public static void main(String[] args) {

        int bar = 0b01010001010100010101000101010001;

        int bitPosition = 30;
        int smartMask = 1 << bitPosition;

        // get
        /*
        boolean result = (bar & smartMask) != 0;
        int resultInt = (bar & smartMask) != 0 ? 1 : 0;
        System.out.println(result);
        System.out.println(resultInt);
         */

        // set
        int foo = 0b01010001010100010101000101010001;
        int setPossition = 31;
        boolean value = true;

        int mask = 1 << 31;

        int result2 = foo | mask;





    }
}
