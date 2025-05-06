interface EngineBracket {

    // 자동차에 엔진을 장착했을 때 반드시 제공되어야 하는 기능: 시동 걸기
    void start();

    // 자동차에 엔진을 장착했을 때 반드시 제공되어야 하는 기능: 시동 끄기
    void stop();
}

// 벤츠사에서 LandRover의 엔진 브라켓을 보고 자신들의 엔진 방식에 맞게 구현
class BenzEngine implements EngineBracket {

    @Override
    public void start() {
        // 벤츠 엔진 시동 방식
        System.out.println("벤츠 엔진이 조용하게 시동을 겁니다.");
    }

    @Override
    public void stop() {
        // 벤츠 엔진 정지 방식
        System.out.println("벤츠 엔진이 부드럽게 정지합니다.");
    }
}

// BMW사에서 구현
class BMWEngine implements EngineBracket {

    @Override
    public void start() {
        // BMW 특유의 즉각적인 반응 구현
        System.out.println("BMW 엔진지 강력하게 시동을 겁니다.");
    }

    @Override
    public void stop() {
        System.out.println("BMW 엔진이 빠르게 정지합니다.");
    }
}

// AUDI 엔진 구현
class AudiEngine implements EngineBracket {

    @Override
    public void start() {
        System.out.println("아우디 엔진이 정숙하게 시동됩니다.");
    }

    @Override
    public void stop() {
        System.out.println("아우디 엔진이 안정적으로 정지합니다.");
    }
}

// LandRover 자동차는 어떤 회사의 엔진이든 EngineBracket 규격만 맞추면 장착가능
class LandRover {
    private EngineBracket engine;   // 인터페이스 타입으로 엔진 참조 -> 다형성 적용

    // 생성자: 엔진을 장착받는 시점에 EngineBracket 규격만 맞으면 어떤 엔진이든 가능
    public LandRover(EngineBracket engine) {
        this.engine = engine;
    }

    // 엔진 시동 및 주행
    public void drive() {
        engine.start();
        System.out.println("랜드로버가 주행을 시작합니다.");
    }

    // 엔진 정지
    public void stop() {
        engine.stop();
        System.out.println("랜드로버가 정차합니다.");
    }
}

public class studyInterface {
    public static void main(String[] args) {

        // 1. BMW 엔진을 장착
        EngineBracket bmwEngine = new BMWEngine();
        LandRover car1 = new LandRover(bmwEngine);
        System.out.println("[BMW 엔진 장착 테스트]");
        car1.drive();
        car1.stop();

        System.out.println();

    }
}
