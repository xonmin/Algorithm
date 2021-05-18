package com.company.W12;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
class Node {
    int count ;
    int x;
    int y;

    public Node(int count, int x, int y) {
        this.count = count;
        this.x = x;
        this.y = y;
    }
}


public class SightMoving {

    public static char [][] map;
    public static int count;
    public static int N, M;
    public static int [] rangeX = {0,-1,1};
    public static int [] rangeY = {1,0,0};
    public static boolean [][] visitCheck;

    public void exe(){
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        map = new char[M][N];
        sc.nextLine();

        for(int i=0;i<M;i++){
            String input = sc.nextLine();
            for(int j=0; j<N;j++){
                map[i][j] = input.charAt(j);
            }
        }

        sc.close();
        //input 종료
        int rtn = 0;

        visitCheck = new boolean[M][N];

        for(int i=0; i<N; i++){
            for(int k=0;k<M;k++){
                for(int j=0; j<N;j++){
                    visitCheck[k][j] = false;
                }
            }
            if(map[0][i] == 'c'){
                rtn = Math.min(rtn,bfs(i,0));
            }
        }

        System.out.println(rtn);
    }

    public static int bfs(int x, int y){
        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(0,x,y));
        visitCheck[y][x] = true;
        while(!q.isEmpty()){
            Node node  = q.poll();
            int count = node.count;
            x = node.x;
            y= node.y;

            if( y == M-1){
                return count;
            }
            for(int i= 0;i<3;i++){
                int nx =  x+ rangeX[i];
                int ny =  y +rangeY[i];
                if( nx >= 0 && nx <N && ny >=0 && ny<M){
                    if(!visitCheck[ny][nx] && (map[ny][nx] == '.' || map[ny][nx] == 'c')){
                        visitCheck[ny][nx] = true;
                        if( i == 0){
                            q.offer(new Node(count,nx,ny));
                        }else{
                            q.offer(new Node(count+1, nx,ny));
                        }
                    }
                }
            }
        }
        return -1;

    }


}
