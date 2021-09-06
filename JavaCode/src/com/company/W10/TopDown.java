package com.company.W10;

import java.awt.print.Pageable;
import java.util.Scanner;

public class TopDown {

    public int n;

    public void exe() {

        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        int arr[] = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        sc.close();

        array(arr);

       for(int k : arr){
           System.out.printf( "%d, ", k);
       }
    }

    public void array(int[] arr){
            for(int i=1; i<arr.length; i++){
                for(int j=1; j<arr.length; j++){
                    if(arr[j-1] <= arr[j]){
                        int tmp = arr[j-1];
                        arr[j-1] = arr[j];
                        arr[j] = tmp;
                    }
                }
            }
    }
}
