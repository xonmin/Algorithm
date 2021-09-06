package com.company.W7;

import java.util.Scanner;

public class Q2 {
    public void exe(){
        Scanner sc =  new Scanner(System.in);

        int n =  sc.nextInt();
        int cnt = 0;
        for(int i= 0; i<n+1;i++){
            for(int j =0; j< 60; j++){
                for(int q = 0; q<60; q++){
                    if(i/10 ==3 || j/10 ==3 || q/10 ==3 ||i % 10 == 3 || j % 10 == 3 || q %10 == 3)
                        cnt++;
                }
            }
        }
        System.out.println(cnt);
    }
}
