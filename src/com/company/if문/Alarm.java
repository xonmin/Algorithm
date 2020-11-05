package com.company.if문;

import java.util.Scanner;

public class Alarm {
    //2884번 문제
    public void Exe(){
        Scanner sc= new Scanner(System.in);
        int hour = sc.nextInt();
        int min = sc.nextInt();

        if(min>=45){
            System.out.println(hour+":"+(min-45));
        }else{
            if(hour == 0){
                hour= 23;
                System.out.println(hour + ":" +(60-(45-min)));
            }else System.out.println((hour-1) +":"+(60-(45-min)));
        }


    }

    public void Exe2(){

        Scanner sc= new Scanner(System.in);
        int hour = sc.nextInt();
        int min = sc.nextInt();

        if(min<45){
            min+=60;
            hour--;
            if(hour<0) hour =23;
        }
        System.out.println(hour + ":"+ (min-45) );
    }


}
