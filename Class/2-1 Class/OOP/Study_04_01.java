import java.util.Scanner;

class Student {
    int id;
    String name;
    int scoreKorean;
    int scoreEnglish;
    int scoreMath;
    int scoreSum;
    float scoreAvg;

    void setInfo(int id, String name, int korean, int english, int math) {
        this.id = id;
        this.name = name;
        this.scoreKorean = korean;
        this.scoreEnglish = english;
        this.scoreMath = math;
    }

    int getSum() {
        scoreSum = scoreKorean + scoreEnglish + scoreMath;
        return scoreSum;
    }

    float getAvg() {
        scoreAvg = getSum() / 3.0f; // 반드시 float으로 나눠야 정확
        return scoreAvg;
    }

    void printInfo() {
        System.out.println("ID: " + id);
        System.out.println("Name: " + name);
        System.out.println("합계 점수: " + getSum());
        System.out.println("평균 점수: " + getAvg());
    }
}


class ScoreManager {
    Student[] students;
    int numOfStudents;

    ScoreManager(int mainStudents) {
        students = new Student[mainStudents];
        this.numOfStudents = mainStudents;
    }

    void inputStudents() {
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < numOfStudents; i++) {
            System.out.println("\n[" + (i + 1) + "번 학생 입력]");
            System.out.print("ID: ");
            int id = sc.nextInt();

            System.out.print("이름: ");
            String name = sc.next();

            System.out.print("국어 점수: ");
            int korean = sc.nextInt();

            System.out.print("영어 점수: ");
            int english = sc.nextInt();

            System.out.print("수학 점수: ");
            int math = sc.nextInt();

            Student student = new Student();
            student.setInfo(id, name, korean, english, math);
            students[i] = student;
        }
    }

    void printAllStudents() {
        System.out.println("\n== 전체 학생 정보 출력 ==");
        for (Student s : students) {
            s.printInfo();
            System.out.println(); // 한 줄 띄기
        }
    }

    void printClassAvg() {
        float total = 0;
        for (Student s : students) {
            total += s.getAvg(); // getAvg 안에 getSum 포함됨
        }
        float avg = total / numOfStudents;
        System.out.printf("반 평균 점수: %.2f\n", avg);
    }

    void printTopStudent() {
        Student top = students[0];
        for (int i = 1; i < students.length; i++) {
            if (students[i].getAvg() > top.getAvg()) {
                top = students[i];
            }
        }
        System.out.println("\n== 최고 평균 학생 ==");
        top.printInfo();
    }
}

public class Study_04_01 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("학생 수를 입력하세요: ");
        int mainStudents = sc.nextInt();

        ScoreManager manager = new ScoreManager(mainStudents);

        manager.inputStudents();      // 입력 받기
        manager.printAllStudents();   // 전체 출력
        manager.printClassAvg();      // 반 평균 출력
        manager.printTopStudent();    // 최고 점수 학생 출력
    }
}
