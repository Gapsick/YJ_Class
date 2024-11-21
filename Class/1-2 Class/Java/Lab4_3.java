import java.util.Scanner;

public class Lab4_3 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        char grade = 'X';
        String attendance = "nool";
        char[] gradeList = {'A', 'B', 'C', 'D', 'E', 'F'};
        String[] attendanceList = {"Excellent", "Average", "Poor"};

        while (true) {
            System.out.println("성적 등급(A~F)와 출석 등급(Excellent, Average, Poor)을 입력하세요:");
            grade = Character.toUpperCase(sc.next().charAt(0)); // 성적 등급 대문자 변환
            attendance = sc.next().trim();

            // 정확히 값을 입력했는지 확인
            boolean checkGrade = false;
            boolean checkAttendance = false;

            for (char g : gradeList) {
                if (grade == g) {
                    checkGrade = true;
                    break;
                }
            }

            for (String att : attendanceList) {
                if (attendance.equalsIgnoreCase(att)) { // 대소문자 무시 비교
                    attendance = att; // 입력값을 정확한 형태로 고정
                    checkAttendance = true;
                    break;
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
            case 'A' -> switch (attendance) {
                case "Excellent" -> "전액 장학금 및 추가 지원금 지급";
                case "Average" -> "전액 장학금";
                default -> "장학금 없음";
            };
            case 'B' -> switch (attendance) {
                case "Excellent" -> "반액 장학금";
                default -> "장학금 없음";
            };
            case 'C', 'D' -> switch (attendance) {
                case "Poor" -> "장학금 없음, 재수강 권장";
                default -> "장학금 없음";
            };
            case 'F' -> "장학금 없음, 재수강 권장";
            default -> "잘못된 성적 등급입니다";
        };

        System.out.println(result);
    }
}
