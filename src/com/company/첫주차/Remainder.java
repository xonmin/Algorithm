package com.company.첫주차;

public class Remainder {

    public void play() {
        int arr[] = new int[10];    // 입력 값
        int brr[] = new int[10];    // 나머지 값
        int k = 0; // 다른 나머지 개수
        for (int i = 0; i < arr.length; i++) {
            arr[i] = i + 1;
            brr[i] = arr[i] % 42; //brr[i] = sc.nextInt()%42;
        }


        for (int i = 0; i < brr.length; i++) {
            for (int j = 0; j < brr.length; j++) {
                if (brr[i] == brr[j]) {
                    k++;            //O(n^)
                }
            }
        }

        System.out.printf("다른 나머지 값 : %d", k);

    }
}
