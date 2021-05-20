package com.company.W12;

import java.util.Scanner;

public class MakeOne {
    //DP 사용하기

    public void exe(){

        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int[] a = new int[x+1];
        sc.close();
        a[1] = 0;
        a[2] = 1;

        for(int i= 3; i<a.length; i++) {
            a[i] = a[i - 1] + 1; //일단 1을 빼 그리고 1을 뺀 연산 횟수 더해


            // 1을 뺀 것과 나누어 떨어지는 연산을 햇을 때의 횟수를 비교하여 최소값 저장
            // 모두 나누어질 수 잇어 else if x

            if(i %5 == 0){
                a[i] = Math.min(a[i],a[i/5]+1);
            }
            if(i% 3 == 0){
                a[i] = Math.min(a[i],a[i/3]+1);
            }
            if(i%2 ==0){
                a[i] = Math.min(a[i],a[i/2]+1);
            }
        }
        System.out.println(a[x]);
    }

}
