package nextedClass;

class Bar implements Runnable{
    @Override
    public void run(){
        try {
            for (int i = 0; i < 10; i++) {
                System.out.println("* ");
                Thread.sleep(500);
            }
        } catch (Exception e) {}
    }
}

class Foo implements Runnable{
    @Override
    public void run(){
        try {
            for (int i = 0; i < 10; i++) {
                System.out.println("- ");
                Thread.sleep(500);
            }
        } catch (Exception e) {}
    }
}


public class Class_06_09 {
    public static void main(String[] args) {

        Bar bar = new Bar();
        Foo foo = new Foo();

        Thread myThread1 = new Thread(bar);
        Thread myThread2 = new Thread(new Runnable() {
            @Override
            public void run(){
                try {
                    for (int i = 0; i < 10; i++) {
                        System.out.println("* ");
                        Thread.sleep(500);
                    }
                } catch (Exception e) {}
            }
        });

        myThread1.start();
        myThread2.start();
    }
}
