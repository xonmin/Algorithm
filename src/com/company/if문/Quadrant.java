package com.company.if문;

import java.util.Scanner;

public class Quadrant {
    //14681번 문제
    public void Exe(){
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();

        if(x>0){
            if(y>0) System.out.println("1사분면");
            else System.out.println("4사분면");
        }else{
            if(y>0) System.out.println("2사분면");
            else System.out.println("3사분면");
        }
    }
}
