import java.util.Scanner;

public class Lab4_2 {
    public static void main(String[] args) {

        // 사용자로 부터 1 ~ 7 까지의 정수를 입력받아 해당 숫자에 맞는 요일 출력
        // switch 사용할 것
        // 잘못된 숫자를 입력할 경우, "X" 출력 후 재입력을 받음
        // 토, 일은 "주말", 그 외는 "주중"으로 구분

        Scanner sc = new Scanner(System.in);

        int num = -1;
        String[] daysOfWeek = {"월", "화", "수", "목", "금", "토", "일"};

        while (true) {

            System.out.print("1 ~ 7 사이의 숫자를 입력하세요: ");
            num = sc.nextInt();

            if (1 <= num && num <= 7) {
                break;
            }

            System.out.println("유효하지 않은 숫자입니다. 1 ~ 7 사이의 숫자를 입력하세요.");

        }

        String day = daysOfWeek[num-1];

        switch (num) {
            case 6, 7 -> System.out.println(day + "," + "주말");
            default -> System.out.println(day + "," + "주중");
        }


    }
}
