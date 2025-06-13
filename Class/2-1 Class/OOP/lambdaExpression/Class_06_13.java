package lambdaExpression;

interface MathOperator {
    int opeartor(int a, int b);
}

public class Class_06_13 {
    public static void main(String[] args) {

        MathOperator opAdd = (a, b) -> a + b;
        MathOperator opMul = (a, b) -> a * b;

        System.out.println(opAdd.opeartor(1, 2));
        System.out.println(opMul.opeartor(1, 2));

    }
}
