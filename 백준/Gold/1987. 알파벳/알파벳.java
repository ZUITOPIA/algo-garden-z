import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int R; // 행
    static int C; // 열
    static char ansMatrix[][]; // 입력받은 배열
    static boolean visited[];  // 방문 여부 담아둘 배열
    static int maxCount = 0;  // 출력할 값 (최대 칸 수) 저장

    static int[] dx = {-1,1,0,0};  // 상, 하, 좌, 우
    static int[] dy = {0,0,-1,1};  // 상, 하, 좌, 우

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        ansMatrix = new char[R][C];
        visited = new boolean[26]; // 알파벳 방문 여부

        for(int i=0;i<R;i++){
            String word = br.readLine();
            for (int j=0;j<C;j++) {
                ansMatrix[i][j] = word.charAt(j);
            }
        }

        dfs(0,0,1); // 행, 렬, 지금까지 방문한 수 count
        System.out.println(maxCount);
        br.close();
    } //main

    static void dfs(int x, int y, int count){
        int current = ansMatrix[x][y]-'A'; // 현재 위치의 알파벳을 인덱스로 변경
        visited[current] = true;

        maxCount = Math.max(maxCount, count); // 카운트 갱신

        for (int i=0; i<4;i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx >= 0 && ny >= 0 && nx < R && ny < C){
                int nextCharIndex = ansMatrix[nx][ny]-'A';
                if(!visited[nextCharIndex]){
                    dfs(nx,ny,count+1);
                }
            }
        }
        visited[current] = false;
    }
}
