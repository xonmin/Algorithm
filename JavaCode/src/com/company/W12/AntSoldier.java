package com.company.W12;

import java.util.Scanner;

public class AntSoldier {


    public void exe(){

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int [] arr =  new int[N];
        int [] food = new int[N] ;

        for(int i=0; i<arr.length;i++){
            arr[i] = sc.nextInt();
        }

        food[0] = arr[0];

        if(arr[0] > arr[1]){
            food[1] =arr[0];
        }else{
            food[1] = arr[1];
        }

        for(int i =2; i<N; i++){
            food[i] = Math.max(food[i-1],food[i-2]+arr[i]);
        }

        System.out.println(food[N-1]);
    }
}
