package lec0906;

public class bar {
    public static void main(String[] args) {

        byte bar = 127;
        short foo = -32768;
        int pos = 2147483647;
        long kin = 9223372036854775807L;

        float fBar = 2.0F;
        double dBar = 3.14159265358979323846;

        char sam = 85; // 아스키 코드를 이용

        System.out.println(sam);

        sam++;

        System.out.println(sam);

        for(char value = 'A'; value <= 'Z'; value++) {
            System.out.println(value);



        }
        boolean jos1 = false;
        boolean jos2 = true;

        // int sum = 2 + 3l;
        // 에러가 나온다. 2는 4byte, 3l은 8byte -> 2를 형 변환을 해서 8byte 로 만든다.
        // int 는 4 byte 니 에러가 난다.

    }
}