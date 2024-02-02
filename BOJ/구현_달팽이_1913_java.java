// 47992kb, 520ms

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class java_구현_달팽이_1913 {
    static int N, x, d, cur, target_i, target_j, i, j;
    static int[] di = {1, 0, -1, 0};
    static int[] dj = {0, 1, 0, -1};
    static int[][] map;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        x = Integer.parseInt(br.readLine());

        map = new int[N][N];

        cur = N*N;
        i = 0; j = 0;
        target_i = 0; target_j = 0;
        d = 0;
        map[0][0] = cur;

        while (cur > 1) {
            int ni = i+di[d];
            int nj = j+dj[d];

            if (!in_boundary(ni, nj) || map[ni][nj] != 0) {
                d = (d+1) % 4;
                ni = i+di[d];
                nj = j+dj[d];
            }

            if (map[ni][nj] == 0) {
                cur--;
                map[ni][nj] = cur;
                if (cur == x) {
                    target_i = ni;
                    target_j = nj;
                }
                i = ni;
                j = nj;
            }
        }

        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                sb.append(map[i][j]).append(' ');
            }
            sb.append('\n');
        }

        sb.append(target_i+1).append(" ").append(target_j+1);
        System.out.println(sb);

    }

    static boolean in_boundary(int i, int j) {
        return 0<=i && i<N && 0<=j && j<N;
    }
}