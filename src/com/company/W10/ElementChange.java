package com.company.W10;

import java.util.Scanner;

public class ElementChange {

    public void exe(){


        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K =  sc.nextInt();
        int maxSum =0;
        int [] arrA = new int[N];
        int [] arrB = new int[N];

        for(int i=0; i<N; i++){
            arrA[i] = sc.nextInt();
        }
        for(int i=0; i<N; i++){
            arrB[i] = sc.nextInt();
        }

        sc.close();

        //input 끝
        upBubbleSort(arrA);
        upBubbleSort(arrB);


        for (int i=0; i<K; i++){
            if(arrA[i] < arrB[N-1-i]){
                int tmp = arrA[i];
                arrA[i] = arrB[N-1-i];
                arrB[N-1-i] = tmp;

            }else{
                break;
            }
        }

        for(int i= 0; i<arrA.length;i++){
            maxSum += arrA[i];
        }

        System.out.println(maxSum);
    }

     public void upBubbleSort(int[] arr){
        for(int i =1 ; i< arr.length; i++){
            for(int j =1; j<arr.length; j++){
                if(arr[j-1] >= arr[j]){
                    int tmp = arr[j-1];
                    arr[j-1] = arr[j];
                    arr[j] = tmp;
                }
            }
        }

     }

}
