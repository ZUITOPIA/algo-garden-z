import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    public static int[] arr;
    public static int N;
    public static int count = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N];

        nQueen(0);
        System.out.println(count);
    }

    private static void nQueen(int depth) {
        // 모든 원소를 다 채웠다면 count 1 증가
        if(depth == N){
            count++;
            return;
        }

        for (int i=0; i<N; i++){
            arr[depth] = i;
            // 놓을 수 없는 위치인 경우 - 재귀호출해서 놓을 수 있을 때까지 반복
            if(Possibility(depth)){
                nQueen(depth+1);
            }
        }
    }

    public static boolean Possibility(int col){
        for (int i=0; i<col;i++){

            if(arr[col] == arr[i]){ // 해당 열의 행과 i열의 행이 일치할 경우 = 같은 행에 이미 존재할 경우
                return false;
            }else if (Math.abs(col-i) == Math.abs(arr[col] - arr[i])){
                // 이미 대각선 상에 놓여있는 경우
                return false;
            }
        }
        return true;
    }
}
