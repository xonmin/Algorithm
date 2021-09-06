package com.company.사주차;

import java.util.Scanner;

public class SugarDelivery { // 2839 번

    public int exe() {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); // input
        int count = 0;


        if (N % 5 == 0) {
            return N / 5;
        } else {
            int fivesuger = N / 5;
            for (int i = fivesuger; i > 0; i--) {
                int c = N - (i * 5);
                if (c % 3 == 0) {
                    return i + (c / 3);
                }

            }
        }
        if (N % 3 == 0) {
            return N / 3;
        } else {
            return -1;
        }


    }

}
