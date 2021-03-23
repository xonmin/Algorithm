package com.company.W7;

import java.util.Scanner;

public class Q3 {
    public void exe(){
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine(); //a1

       int row = s.charAt(1) - '0';
       int column = s.charAt(0) - 'a'+1;

       int[] rangeX = {-2,-1,1,2,2,1,-1,-2};
       int[] rangeY = {-1,-2,-2,-1,1,2,2,1};

       int count =0;

       for(int i=0; i<8;i++){

           int tmprow = row + rangeX[i];
           int tempcolumn = column +rangeY[i];

           if((1<=tmprow && tmprow <= 8 )  && (1<= tempcolumn && tempcolumn <=8)){
               count++;
           }
       }
        System.out.println(count);




    }
}
