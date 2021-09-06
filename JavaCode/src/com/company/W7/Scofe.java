package com.company.W7;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Scanner;

public class Scofe {

    public int n;
    public int k;
    public int count;
    public void exe(){
        //input
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        k = sc.nextInt();

        int arr [] = new int[n];

        for(int i = 0; i< n;i ++){
            arr[i] = sc.nextInt();
        }

        //logic
        count = 0;
        Arrays.sort(arr);
        int min = arr[0];

        for(int i =0; i<n; i+=(k-1)){
            for(int j=0; j<k; j++){ //k번 만큼
                if( i + j > n-1){
                    break;
                }
                arr[i+j] = min;

            }
            count ++;
        }


        System.out.println(count);
    }


}
