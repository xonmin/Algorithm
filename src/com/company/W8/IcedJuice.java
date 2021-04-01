package com.company.W8;

import java.util.ArrayList;
import java.util.Scanner;

public class IcedJuice {
    public static boolean[] visit;
    public static int [][] graph;
    public static int n,m;
    public void exe(){
        Scanner sc =  new Scanner(System.in);
         n = sc.nextInt();
         m = sc.nextInt();
        int count = 0;
        graph = new int[n][m];
        sc.nextLine();
        for(int i=0;i<n;i++){
            String input = sc.nextLine();
            for(int j =0; j<m;j++){
                graph[i][j] = input.charAt(j)-'0';
            }
        }
        for(int i = 0; i <n; i++){
            for(int j=0;j <m; j++){
                if(dfs(i,j)){
                    count++;
                }
            }
        }
        System.out.println(count);
    }
    public static boolean dfs(int x, int y){
        if(x <= -1 || x>=n || y<= -1 || y>=m){//범위초과
            return false;
        }
        // 현재 노드 방문 안했다면,
        if(graph[x][y] == 0){
            graph[x][y] =1; //방문
            dfs(x-1,y);
            dfs(x,y-1);
            dfs(x+1,y);
            dfs(x,y+1);
                return true;
        }
        return false; //방문했었다면
    }
}
