package com.company.이주차;

import java.util.Arrays;
import java.util.Scanner;

public class Atm {
    public void exe(){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int total[] = new int[n];

        for(int i = 0 ; i < n; i++){
            total[i] = sc.nextInt();
        }

        int min = 0; // 맨 앞에 대기하는 놈 대기 시간 = 0
        // 제일 적게 걸리는 놈이 맨 앞에와야 제일 적은 시간이 걸린다.
        Arrays.sort(total);
        int sum = 0; // 총 소요시간
        for(int i =0; i<total.length;i++){
            min += total[i];
            sum += min;
        }
        System.out.println(sum);
    }
}
