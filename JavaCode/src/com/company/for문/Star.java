package com.company.for문;

public class Star {
 //2439 번 문제
   public void Exe(int k) {
       for (int i= 1;i<=k;i++){
           for(int j = 1; j<=k-i; j++){
               System.out.printf(" ");
           }
           for(int u=1; u<=i; u++){
               System.out.printf("*");
           }
           System.out.printf("\n");
       }
   }
}
