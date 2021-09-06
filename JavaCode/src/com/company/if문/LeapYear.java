package com.company.if문;

import java.util.Scanner;

public class LeapYear {
    //2753번 문제
    public void Exe(){
        Scanner sc = new Scanner(System.in);
        int year = sc.nextInt();

        if(year%400 == 0){
            System.out.println("윤년");
        }else if(year%4== 0 && year%10!=0){
            System.out.println("윤년");
        }else System.out.println("not 윤년");
    sc.close();
    }



}
