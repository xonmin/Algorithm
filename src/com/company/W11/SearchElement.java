package com.company.W11;

import java.util.Arrays;
import java.util.Scanner;

public class SearchElement {
        //p197 부품찾기
    public static int N , M;
    public static int[] arr1, arr2;

    public void exe(){

        Scanner sc =  new Scanner(System.in);
        N = sc.nextInt();
        arr1  = new int[N];

        for( int i=0; i<arr1.length; i++){
            arr1[i] = sc.nextInt();
        }

        M = sc.nextInt();
        arr2  = new int[M];

        for(int i=0 ; i<arr2.length; i++){
            arr2[i] = sc.nextInt();
        }

        Arrays.sort(arr1);

        for(int n : arr2){
            String s = search(n,arr1);
            System.out.println(s+" ");
        }


    }

    public String search(int n , int [] arr ){
        int start = 0;
        int last  = arr.length-1;

        while(start <= last){
            int mid = (start+last)/2;
            if(arr[mid] == n){
                return "yes";
            }else if(arr[mid] > n){
                last = mid-1;
            } else {
                start = mid +1;
            }
        }
        return "no";
    }
}
