package com.company.for문;

import java.util.Scanner;

public class Sigma {

    public void Exe(){
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt();
        int k=0;
        for(int i=1;i<=n1;i++){
            k+=i;
        }
        System.out.println(k);
    }
}
