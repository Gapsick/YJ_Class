import java.util.Scanner;

public class lab4_1 {
    public static void main(String[] args) {

        // 사용자로부터 나이를 입력 받는다
        // 음수일 경우, "음수X" 출력후 올바른 값이 입력할 때까지 다시 입력
        // 0 ~ 12 어린이, 13 ~ 17 청소년, 18 ~ 64 성인, 65 이상 노인

        Scanner sc = new Scanner(System.in);

        int age = -1;

        while (true) {

            System.out.print("나이를 입력하세요: ");
            age = sc.nextInt();

            if (age >= 0) {
                break;
            }

            System.out.println("나이는 음수가 될 수 없습니다. 다시 입력하세요.");
        }

        if (0 <= age && age <= 12 ) {
            System.out.println("어린이");
        }
        else if (13 <= age && age <= 17 ) {
            System.out.println("청소년");
        }
        else if (18 <= age && age <= 64 ) {
            System.out.println("성인");
        }
        else {
            System.out.println("노인");
        }


    }
}
