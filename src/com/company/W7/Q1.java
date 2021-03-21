package com.company.W7;

import java.util.List;
import java.util.Scanner;

public class Q1 {

    int [] rangeX = {0,0,-1,1};
    int [] rangeY = {-1,1,0,0};
    String []  move = {"L","R","U","D"};

    public void exe(){
        //input
        Scanner sc=  new Scanner(System.in);
        int  n = sc.nextInt();
        sc.nextLine();
        String input = sc.nextLine();
        String [] arr = input.split(" ");

        //Logic
        int x =1, y=1;
        for(String moving : arr){
            for(int i =0; i<move.length;i++){
                int tempx=1, tempy=1;
                if(moving.equals(move[i])){

                   tempx  = x+rangeX[i];
                   tempy =  y+rangeY[i];
                   if(tempx < 1 || tempy <1 || tempx > n || tempy > n)
                        continue;
                   x =tempx;
                   y = tempy;
                }



            }


        }

        System.out.print(x+","+y);




    }
}
