import java.util.Scanner;

public class Lab4_3 {
    public static void main(String[] args) {

        // 학생의 성적 등급과 출석 등급을 입력받는다
        // switchExpression, yield를 사용하여 구현
        // 성적 등급은 A ~ F, 출석 등급은 Excellent, Average, Poor 중 하나로 입력
        // 키보드로 입력받은 영문자는 모두 대문자로 변환하여 처리
        // 잘못된 입력이 있을 경우 다시 입력받도록 한다

        Scanner sc = new Scanner(System.in);


        char grade = 'X';
        String attendance = "nool";
        char[] gradeList = {'A', 'B', 'C', 'D', 'E', 'F'};
        String[] attendanceList = {"Excellent", "Average", "Poor"};

        while (true) {
            grade = sc.next().charAt(0);
            attendance = sc.next().trim();

            // 정확히 값을 입력했는지 확인
            boolean checkGrade = false;
            boolean checkAttendance = false;

            for (char g : gradeList) {
                if (grade == g) {
                    checkGrade = true;
                }
            }

            for (String att : attendanceList) {
                if (attendance.equals(att)) {
                    checkAttendance = true;
                }

            }

            // 정확히 값을 입력했으면 탈출
            if (checkGrade && checkAttendance) {
                break;
            }

            // 정확히 값을 입력하지 않았을 경우
            System.out.println("잘못된 입력입니다. 다시 입력하세요");

        }

        String result = switch (grade) {
            case 'A' -> {
                switch (attendance) {
                    case "Excellent" -> yield "전액 장학금 및 추가 지원금 지급";
                    case "Average" -> yield "전액 장학금";
                    default -> yield "장학금 없음";
                } ;
            }
            case 'B' -> {
                switch (attendance) {
                    case "Excellent" -> yield "반액 장학금";
                    default -> "장학금 없음";
                } ;
            }
            case 'C', 'D' -> {
                switch (attendance) {
                    case "Poor" -> yield "장학금 없음, 재수강 권장";
                    default -> "장학금 없음";
                } ;
            }
            case 'F' -> yield "장학금 없음, 재수강 권장";

            default -> "잘못된 성적 등급입니다";
            };



        System.out.println(result);


    }
}
