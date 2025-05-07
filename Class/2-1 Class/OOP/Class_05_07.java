interface Scan {
    // public abstract void doScan();
    void doScan();

    // public static final int scanNum = 2;
    int scanNum = 2;

    default void prePaper() {
        powerOn();
        System.out.println("Prepaper");
    }

    default void preWater() {
        powerOn();
        System.out.println("Prewater");
    }

    static void prePower() {
        System.out.println("Power");
    }

    private void powerOn() {
        System.out.println("PowerOn");
    }
}

class Equipment implements Scan {
    public void doScan() {
        System.out.println(Scan.scanNum);
        Scan.prePower();
    }

    @Override
    public void prePaper() {
        Scan.super.prePaper();
        System.out.println("Equipment - Prepaper");
    }
}

class Device implements Scan {
    int scanNum = 10;
    @Override
    public void doScan() {
        System.out.println(Scan.scanNum);
    }
}

public class Class_05_07 {
    public static void main(String[] args) {
        Equipment a = new Equipment();
        a.doScan();
    }
}
