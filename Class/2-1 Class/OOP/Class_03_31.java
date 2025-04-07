package oopVer;

import java.util.Scanner;

class Foo {}
// 변수
// 1) 멤버변수
//    A. 인스턴스 멤버 변수
//    B. 클래스 멤버 변수
// 2) 지역변수 -> 메서드 내 선언된 변수

class Student {
    // ID, 이름, 국어, 영어, 수학, 합계점수, 평균
    int id;
    String name;
    private int scoreKorean;
    private int scoreEnglish;
    private int scoreMath;
    private int sum;
    private float avg;

    Student(int argId, String argName) {
        id = argId;
        name = argName;
    }

    boolean setScore(int argKorean, int argEnglish, int argMath) {
        if(argKorean < 0 || argEnglish < 0 || argMath < 0) {
            return false;
        }

        if(argKorean > 100 || argEnglish > 100 || argMath > 100) {
            return false;
        }

        scoreKorean = argKorean;
        scoreEnglish = argEnglish;
        scoreMath = argMath;

        return true;
    }


    int getSum() {
        sum = scoreKorean + scoreEnglish + scoreMath;
        return sum;
    }

    float getAvg() {
        avg = (float)getSum() / 3;
        return avg;
    }
}

class StdScoreMgr{
    Student[] stdList;
    int numOfStudents;

    StdScoreMgr(int argNumOfStudents){
        stdList = new Student[argNumOfStudents];
        numOfStudents = argNumOfStudents;
    }

    void addStudent() {
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < numOfStudents; i++) {

            System.out.println("ID 입력 : ");
            int stdId = sc.nextInt();

            System.out.println("이름 입력 : ");
            String stdName = sc.next();

            Student student = new Student(stdId, stdName);

            System.out.println("국어 성적 입력 : ");
            int scoreKorean = sc.nextInt();

            System.out.println("영어 성적 입력 : ");
            int scoreEnglish = sc.nextInt();

            System.out.println("수학 성적 입력 : ");
            int scoreMath = sc.nextInt();

            if (student.setScore(scoreKorean, scoreEnglish, scoreMath)) {
                stdList[i] = student;
            }
        }
    }
}

public class Class_03_31 {
    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        System.out.println("입력 학생 수: ");
        int stdNum = sc.nextInt();

        StdScoreMgr stdMgr = new StdScoreMgr(stdNum);
        stdMgr.addStudent();

    }

}
