package com.company.for문;

import java.lang.reflect.Array;
import java.util.Scanner;

public class LessThanX {

    public void Exe(int n, int x){
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[n];
        for(int i=0;i< arr.length; i++){
            arr[i] = sc.nextInt();
            System.out.printf("%d ",arr[i]);
        }
        System.out.println("");
        for(int i=0;i<arr.length;i++){
            if(arr[i]<x) System.out.printf("%d ",arr[i]);
        }
    }
}
