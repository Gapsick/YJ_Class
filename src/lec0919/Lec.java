package lec0919;

public class Lec {
    public static void main(String[] args) {

        // 화면에 A ~ Z 까지 출력

        char bar = 'A';
        for (; bar <= 'Z'; bar += 2) {
            System.out.print(bar + "\t");

        }
        System.out.println();
        // 화면에 z ~ a 까지 출력
        for (char foo = 'z'; foo >= 'a'; foo --) {
            System.out.print(foo + "\t");
        }
        System.out.println();

        // 증감 연산자
        int bar1 = 2;

        System.out.println(bar1++);

        System.out.println(++bar1);

        // 배열
        int[] numbers = {1, 2, 3, 4, 5, 6};
        int index = 0;

        // 1. 후위 증감 연산자 활용 예: 배열 요소 탐색 (인덱스를 처리할 때)
        System.out.println("후위 증감 연산자 활용 예:");

        // 배열을 순차적으로 탐색하면서 값으 ㄹ출력
        while (index < numbers.length) {
            System.out.println("현재 요소 (후위): " + numbers[index++]);
        }

        String str1 = new String("Hello");  // new : Operator 우측의 Class를 찍어라
        String str2 = "Hello";

        // 참조 비교: 서로 다른 객체이므로 false
        System.out.println(str1 == str2); // false

        // 내용 비교: 같은 문자열 내용을 가지고 있으므로 True
        System.out.println(str1.equals(str2)); // True



    }


}
