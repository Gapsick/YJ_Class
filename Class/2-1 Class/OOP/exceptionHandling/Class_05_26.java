package exceptionHandling;


import java.io.IOException;
import java.util.Scanner;

class Bar1 implements AutoCloseable {
    @Override
    public void close() throws Exception {
        System.out.println("Bar - close");

//         자원 정리 중 예외 발생을 테스트하려면 아래 주석 해제
//         throw new Exception("Bar 자원 정리 중 예외 발생");
    }
}


public class Class_05_26 {
    public static void main(String[] args) {
    // try-with-resources 구문: Bar 객체는 try 블록이 끝나는 즉시 자동으로 close() 호출 됨
        try (Bar1 bar1 = new Bar1()) {
            System.out.print("숫자를 입력하세요 (1: 정상 실행, 그 외: IOException 발생): ");
            int input = new Scanner(System.in).nextInt();

            if (input == 1) {
                System.out.println("try 블록 정상 실행");
            }   else {
                throw new IOException("입력값이 1이 아님");
            }

        } catch (IOException e) {
            // IOException이 발생한 경우 (입력값이 1이 아닌 경우)
            System.out.println("catch - IOException: " + e.getMessage());

            // 억제된 예외(suppressed exception)가 있는 경우 출력
            for (Throwable suppressed : e.getSuppressed()) {
                System.out.println("-> Suppressed: " + suppressed);
            }

        } catch (Exception e) {
            // 기타 Exception 처리 (Bar.close() 중 발생할 수 있음 )
            System.out.println("catch - Exception: " + e.getMessage());
        }


    }
}
