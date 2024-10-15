package lec1010;

public class Lec {

    static String getBinaryValue(int argValue) {
        String binaryString = Integer.toBinaryString(argValue);

        // 32비트 int 값을 4자리씩 출력하기 위해 앞쪽에 필요한 만큼 0 추가
        binaryString = String.format("%32s", binaryString).replace(' ', '0');

        String result = "";

        // 4자리씩 끊어서 출력
        System.out.println("Binary representation (4 bits per group):");
        for (int i = 0; i < binaryString.length(); i += 4) {
            result += binaryString.substring(i, i + 4) + " ";
        }

        return result;
    }


    public static void main(String[] args) {


        int bar = 0b1000000000000000000000000000000;
        int result = bar >> 3;
        System.out.println(getBinaryValue(result) + " : " + result);

        result = bar >>> 1;
        System.out.println(getBinaryValue(result) + " : " + result);

        //result = bar << 4;
        //System.out.println(getBinaryValue(result) + " : " + result);






    }
}


