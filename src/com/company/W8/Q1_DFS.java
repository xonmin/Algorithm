package com.company.W8;

import java.util.ArrayList;
import java.util.Scanner;

public class Q1_DFS {
    public static boolean[] visit = new boolean[9];
    public static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();

    public void exe(){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // 시작 노드

        // input
        for(int i = 0; i<9; i++){
            graph.add(new ArrayList<Integer>()); // 그래프 초기화
        }

        //책에 나온 노드간의 관계 설정
        graph.get(1).add(2);
        graph.get(1).add(3);
        graph.get(1).add(8);

        graph.get(2).add(1);
        graph.get(2).add(7);

        graph.get(3).add(1);
        graph.get(3).add(4);
        graph.get(3).add(5);

        graph.get(4).add(3);
        graph.get(4).add(5);

        graph.get(5).add(3);
        graph.get(5).add(4);

        graph.get(6).add(7);

        graph.get(7).add(6);
        graph.get(7).add(8);

        graph.get(8).add(1);
        graph.get(8).add(7);

        dfs(n);
    }

    //dfs method
    public static void dfs(int n){
        //현재 노드 방문 처리하기
        visit[n] = true;
        System.out.print(n + " ");

        for(int i=0;i<graph.get(n).size();i++){
            int m = graph.get(n).get(i); //n번째 노드에 인접한 녀석들

            if(!visit[m]){ //안가봤으면
                dfs(m);
            }
        }
    }



}
