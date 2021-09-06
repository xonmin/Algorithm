package com.company.삼주차;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Coin {
    int arr[];
    int count; // 동전 개수
    public Coin(int n) {
        arr = new int[n];
        Scanner sc = new Scanner(System.in);
        for(int i =0; i< n; i++) {
            arr[i] = sc.nextInt();
        }
    }

    public void exe(int n, int k ){
        // logic implement
        for(int i = n-1; i>=0;i--){
            if(k/arr[i] >= 0){
               count += k/arr[i];
               k %= arr[i];
            }
        }

        System.out.println(count);
    }

}
