package com.company.사칙연산;

import java.util.Scanner;

public class Multiplication {
    //백준 2588 문
    public void Play() {
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt(); //1
        int n2 = sc.nextInt();//2


        System.out.println(n1*(n2%10)); // 3
        System.out.println(n1*((n2%100)/10)); // 4
        System.out.println(n1*(n2/100)); //5
        System.out.println(n1*n2);
    }
}
