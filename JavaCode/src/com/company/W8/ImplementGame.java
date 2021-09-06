package com.company.W8;

import java.util.Scanner;

public class ImplementGame {

    public static int [] rangeX = {-1,0,1,0};
    public static int [] rangeY = {0,1,0,-1};
    public static int n,m,view;
    public static int [][] map ;
    public static boolean [] visit;
    public static int visitcount;
    public static int locationX, locationY;
    public void exe(){

        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();
        map = new int [n][m];
        locationX = sc.nextInt();
        locationY = sc.nextInt();
        view = sc.nextInt();
        visitcount = 0;
        sc.nextLine();
        for(int i = 0 ;i<n; i++){
            String input = sc.nextLine();
            for(int j =0; j<m;j++){
                map[i][j] = input.charAt(j)-'0';
            }
        }
        //input 끝

        for(int i=locationX;i<n;i++){
            for(int j =locationY;j<m;j++ ){
                dfs(i,j);
            }
        }
        System.out.println(visitcount);
    }

    public static boolean dfs(int x, int y){
        if(x<=-1 || x>= n || y<= -1 || y>= m ){
            return false;
        }
        if(map[x][y] == 0){
            map[x][y] = 1;
            visitcount++;
            turn();
            for(int view = 0; view<4; view ++)
                dfs(x+rangeX[view],y+rangeY[view]);

            return true;
        }
        return false;
    }

    public static void turn(){ // 시점 변환
        view -=1;
        if(view < 0){
            view = 3;
        }
    }



}
