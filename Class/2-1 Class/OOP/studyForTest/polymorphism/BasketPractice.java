class Player1 {
    protected String name;
    protected String position;

    Player1(String name, String position) {
        this.name = name;
        this.position = "";
    }

    void shoot() {
        System.out.println(position + " " + name + "기본 슛");
    }
}

class Sg1 extends Player1 {
    Sg1(String name) {
        super(name, "슈팅가드");
    }

    @Override
    void shoot() {
        System.out.println( position + " " + name + "3점슛!");
    }
}

class Pg1 extends Player1 {
    Pg1(String name) {
        super(name, "포인트 가드");
    }

    @Override
    void shoot() {
        System.out.println(position + " " + name + ": 돌파 후 점퍼!");
    }
}

public class BasketPractice {
    public static void main(String[] args) {
        Player1[] team = {
                new Sg1("민수"),
                new Pg1("준호"),
        };

        System.out.println(" [팀 슛 연습 시작! ]\n");

        for (Player1 p : team) {
            p.shoot();
        }



    }
}
