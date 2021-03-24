package com.company.W7;

import java.util.Scanner;

public class Combination {
    public void exe(){

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); //n 값 할당
        int r = sc.nextInt(); // r 개 뽑기
        int [] arr  = new int[n]; //n개의 원소 배열
        boolean[] visit = new boolean[n]; // 중복을 제거하기위한 식별자
        int depth =0; // 건들이는 인자 위치
        //input
        for(int i=0; i<n;i++){
            arr[i] = sc.nextInt();
        }

        comb(arr,visit,0,n,r);

    }

    public void comb(int[] arr,boolean[] visit, int depth, int n , int r){
        if(r ==0){ // 이미 뽑을 애들이 다 선택 되어있을 떄
            for(int i =0; i<n;i ++){
                if(visit[i]){
                    System.out.print(arr[i]+ " ");
                }

            }
            System.out.println("");
            return;
        }
        if(depth == n){  //다돌앗을 떄
            return;
        }
        visit[depth] = true;
        comb(arr,visit,depth+1,n,r-1); // 이번 루프에서 뽑은 1개를 뽑은 상태 n-1Cr-1

        visit[depth] = false;
        comb(arr,visit,depth+1,n,r); //이번 루프에서 이놈을 안 뽑은 상태 n-1Cr
    }
}
