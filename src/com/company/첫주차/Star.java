package com.company.첫주차;

public class Star {

    public void play(int num){

        for(int i = 1; i<=num ;i++ ){
            for(int j = 1; j<=num-i ;j++){
                System.out.printf(" ");
            }
            for(int k = 1; k<= i; k++){
                System.out.printf("*");
            }
            System.out.printf("\n");
        }

    }

}
