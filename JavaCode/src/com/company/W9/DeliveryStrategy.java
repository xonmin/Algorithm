package com.company.W9;

import java.util.Scanner;

public class DeliveryStrategy {

//    1. 배송해야 할 경로를 직선화한 다음 방문해야 하는 곳을 1로, 방문하지 말아야 할 곳을 0으로 표기했다.
//    2. 이 실험은 가장 기초적인 단계이기 때문에 우선 각 문자 사이의 간격을 1칸으로 정의했다.
//    3. 해당 경로를 지나는 택배기사는 한 번에 1칸 또는 2칸 움직일 수 있다.
// input : 경로의 길이 N : (3<=N<=50)
// 두 번째 줄에 길이가 N이며 0과 1로 구성된 경로구성이 주어진다.
// 첫 문자와 끝 문자는 항상 1이며, 0이 두 번 연속으로 들어오는 경우는 없다.
// output : 배송기사가 왼쪽끝에서 오른쪽 끝가지 도달할 수 있는 경우의 수


    public void exe(){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        String input = sc.nextLine();
        int path [] = new int[N];

        for(int i =0; i<N;i++){
            path[i] = input.charAt(i)-'0';
        }
        //input 종료

        //logic
        int count=1;
        int tmp = N-2; //양 끝 제외
        int group = tmp/2;
        int rmd = tmp%2;

        for(int i=1; i<N;i +=2){
                if(path[i] == 0){//01
                    count *= 1 ;
                }else{
                    //10
                    if(i+1 == N){
                        break;
                    }
                    if(path[i+1] == 0){
                        count *=1;
                    }else{ // 11
                        count *=2;
                    }
                }
        }
        System.out.println(count);

    }
}
