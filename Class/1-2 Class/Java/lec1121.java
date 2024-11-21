public class lec1121 {
    static float[] getSumAvg(int a, int b, int c) {
        float result[] = new float[2];

        result[0] = a + b + c;
        result[1] = result[0] / 3;
        return result;
    }
    public static void main(String[] args) {

        int[][] bar = new int[3][3];

        int value = 10;
        // Loop: row 0 -> 2
        for(int row = 0; row < bar.length; row++) {
            // Loop : col 0 -> 2
            for (int col = 0; col < bar[row].length; col++) {
                bar[row][col] = value;
                value += 10;
                System.out.println(bar[row][col]);
            }
        }
        
        int[][] foo = {{10, 20, 30}, {40 , 50, 60}, {70, 80, 90} };


    }
}

