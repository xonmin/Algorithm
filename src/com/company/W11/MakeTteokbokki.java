package com.company.W11;

import java.util.Scanner;

public class MakeTteokbokki {

    public static int N , M ;

    public static int[] riceCake;

    public void exe(){

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt(); // 떡 개수
        M = sc.nextInt(); //손님이 받아가는 양

        riceCake  = new int[N];


        for(int i =0; i<riceCake.length;i++){
            riceCake[i] = sc.nextInt();
        }

        sc.close();

        //input 끝

        //logic
        //최대값 찾기
        int max = riceCake[0];

        for(int i=1; i<riceCake.length;i++){
            if(max < riceCake[i]){
                max = riceCake[i];
            }
        }

        while(true){
            if(cutting(max,riceCake)>= M){
                break;
            }
            max--;
        }

        System.out.println(max);
    }

    public int cutting(int length, int[] arr){
        int sum = 0;

        for(int dduck : arr) {
            if (dduck - length < 0) {
                continue;
            }
            sum += (dduck - length);
        }
        return sum;
    }

}
