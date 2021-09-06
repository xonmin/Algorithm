package com.company.W9;


import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Node{
        int x,y;

        public Node(int x, int y){
            this.x =x;
            this.y =y;
        }
}
public class EscapeMaze {


     Scanner sc = new Scanner(System.in);
    public int [] rangeX = {-1,0,1,0};
    public int [] rangeY = {0,1,0,-1};
    public int n;
    public int m ;
    public int [][] map ;
  public void exe() {
       n = sc.nextInt();
       m = sc.nextInt();
       map = new int[n][m];

      sc.nextLine();

      for (int i = 0; i < n; i++) {
          String input = sc.nextLine();
          for (int j = 0; j < m; j++) {
              map[i][j] = input.charAt(j) - '0';
          }
      }

      bfs(0,0);
      System.out.println(map[n-1][m-1]);

  }
      //input 끝

    public void bfs(int x, int y ){
      Queue<Node> q = new LinkedList<>();
      q.offer(new Node(x,y)); //push
      while(!q.isEmpty()){

          Node node = q.poll(); //pop
          x = node.x;
          y = node.y;
          // 사주경계
          for(int i=0;i<4;i++){
              int dx = x+rangeX[i];
              int dy = y + rangeY[i];

              // 범위 밖인지
              if(dx <0 || dx>= n || dy<0|| dy>=m ){
                  continue;
              }
              if(map[dx][dy] ==  0){ // 벽이면 안가
                  continue;
              }
              if(map[dx][dy] == 1){
                  map[dx][dy] = map[x][y]+1;
                  q.offer(new Node(dx,dy));
              }
          }
      }


      }


}
