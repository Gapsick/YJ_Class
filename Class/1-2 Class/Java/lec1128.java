public class lec1128 {
    public static void main(String[] args) {
        float[] noiseList;  // 단순하게 생각해라! 그냥 변수 선언
        // 근데 Primitive 변수가 아니고 Refernce 변수
        // 즉 Reference 변수는 메모리 주소 값을 저장한다.
        // 근데 현재 저장된 메모리 주소 값이 없다.

        //noiseList[2] = 2.0f;
        // noiseList 변수에 저장된 메모리 주소로 이동
        // 근데 변수에 저장된 메모리 주소 값이 null 이다.
        // 따라서 Error

        // 2초마다 평균 값을 계산해서 출력하는데
        // 2초마다 측정 된 값을 1 frame 이라고 가정하고
        // 현재까지 측정된 모든 프레임의 값들을 저장하고 싶어.
        // 2차원으로 만든다는 것을 예측을 해야한다!

        // 배열을 선언 할때 안의 값을 Literal 상수로 적지 말고, 상수를 선언하자!
        final int FRAME_NUM = 10000;
        final int ITEM_NUM = 20;

        float[][] noiseMatrix;

        //noiseMatrix = new float[FRAME_NUM][ITEM_NUM];

        noiseMatrix = new float[FRAME_NUM][];

    }
}
