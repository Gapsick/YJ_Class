package basketball;

class Player {
    protected String name;
    protected String position;

    Player(String name, String position) {
        this.name = name;
        this.position = position;
    }

    void shoot() {
        System.out.println(position + " " + name + ": 기본 슛");
    }
}

class Sg extends Player {
    Sg(String name) {
        super(name, "슈팅가드");
    }

    @Override
    void shoot() {
        System.out.println(position + " " + name + ": 3점슛!");
    }
}

class Pg extends Player {
    Pg(String name) {
        super(name, "포인트 가드");
    }

    @Override
    void shoot() {
        System.out.println(position + " " + name + ": 돌파 후 점퍼!");
    }
}

class Center extends Player {
    Center(String name) {
        super(name, "센터");
    }

    @Override
    void shoot() {
        System.out.println(position + " " + name + ": 골밑슛!");
    }
}

class Pf extends Player {
    Pf(String name) {
        super(name, "파워 포워드");
    }

    @Override
    void shoot() {
        System.out.println(position + " " + name + ": 미들슛!");
    }
}

class Sf extends Player {
    Sf(String name) {
        super(name, "스몰 포워드");
    }

    @Override
    void shoot() {
        System.out.println(position + " " + name + ": 슬래시 앤 드라이브!");
    }
}

public class game {
    public static void main(String[] args) {
        Player[] team = {
                new Pg("민수"),
                new Sg("준호"),
                new Sf("지훈"),
                new Pf("영철"),
                new Center("성민")
        };

        System.out.println("[팀 슛 연습 시작! ]\n");

        for (Player p : team) {
            p.shoot();
        }
    }
}
