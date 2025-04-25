class User2 {
    private String username;
    private String email;

    User2() {
        this.username = "Guest";
        this.email = "guest@gmail.com";
        System.out.println("디폴트 생성자로 객체 생성됨 (기본값 설정)");
    }

    User2(String username, String email) {
        this.username = username;
        this.email = email;
        System.out.println("파라미터 생성자로 객체 생성됨");
    }

    void printUserInfo() {
        System.out.println("사용자명: " + username + ", 이메일: " + email);
    }

}



public class ExamUserInfoMain2 {
    public static void main(String[] args) {
        User2 user1 = new User2();
        user1.printUserInfo();

        System.out.println("------------------------");

        User2 user2 = new User2("hong", "hong@gmail.com");
        user2.printUserInfo();
    }
}
