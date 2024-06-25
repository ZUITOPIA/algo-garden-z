import java.util.Scanner;

public class Main {
    static int N, S;
    static int count = 0;
    static int[] arr;

    public static void main(String[] args) throws Exception{
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        S = sc.nextInt();

        arr = new int[N];

        for (int i=0;i<N;i++){
            arr[i] = sc.nextInt();
        }

        dfs(0,0);

        if(S==0) count-=1;
        System.out.println(count);
    }// main

    static void dfs(int depth, int sum){
        if(depth == N){
            if(sum == S)  count++;
            return;
        }
        dfs(depth+1, sum + arr[depth] );
        dfs(depth+1, sum);
    }
}
