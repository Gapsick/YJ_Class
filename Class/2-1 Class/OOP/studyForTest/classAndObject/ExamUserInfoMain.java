class User {
    private String username;
    private String email;

    User(String username, String email) {
        if (username.isEmpty() || email.isEmpty()) {
            throw new IllegalArgumentException("사용자명과 이메일은 필수 입력값입니다.");
        }
        this.username = username;
        this.email = email;
    }

    void printUserInfo() {
        System.out.println("사용자명: " + username + ", 이메일: " + email);
    }
}



public class ExamUserInfoMain {
    public static void main(String[] args) {
        try {
            User user1 = new User("hong", "hong@gmail.com");
            user1.printUserInfo();

            // 잘못된 사용자 생성
            User user2 = new User("", "invalid@gmail.com");
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }
}
