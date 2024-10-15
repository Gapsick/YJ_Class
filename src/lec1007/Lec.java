package lec1007;

public class Lec {
    public static void main(String[] args) {

        // 비트 연산자 (Bitwsie opeartor)

        // 왜 사용할까?
        /* int addr1 = 210;    // 1101 0010
        int addr2 = 101;    // 0110 0101
        int addr3 = 236;    // 1110 1100
        int addr4 = 181;    // 1011 0101

        int mask1 = 255;    // 1111 1111
        int mask2 = 255;    // 1111 1111
        int mask3 = 255;    // 1111 1111
        int mask4 = 0;      // 0000 0000

        int subAddr1 = addr1 & mask1;   // 1100 0010
        int subAddr2 = addr2 & mask2;   // 0110 0101
        int subAddr3 = addr3 & mask3;   // 1011 0101
        int subAddr4 = addr4 & mask4;   // 0000 0000


        System.out.println(subAddr1 + " " + subAddr2 + " " + subAddr3 + " " + subAddr4);


        int bar = 1;
        int foo = 16;
        System.out.println(bar << 1);
        System.out.println(bar << 2);
        System.out.println(bar << 3);
        System.out.println(bar << 4);
        System.out.println();
        System.out.println(foo >> 1);
        System.out.println(foo >> 2);
        System.out.println(foo >> 3);
        System.out.println(foo >> 4);
         */


        int myIpAddr = 0xD265ECA4;

        int ipAddr1 = (myIpAddr >> 24) & 0xFF; // D2
        int ipAddr2 = (myIpAddr >> 16) & 0xFF; // 65
        int ipAddr3 = (myIpAddr >> 8) & 0xFF; // EC
        int ipAddr4 = myIpAddr & 0xFF; // A4

        System.out.println(ipAddr1 + " " + ipAddr2 + " " + ipAddr3 + " " + ipAddr4);



    }

}
