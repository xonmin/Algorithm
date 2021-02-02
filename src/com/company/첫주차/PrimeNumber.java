package com.company.첫주차;

import java.util.ArrayList;
import java.util.List;

public class PrimeNumber {

    public void play(int num){

        int i=2;
        List list = new ArrayList();

        while(num != 1){
            if(num % i ==0){
                num /= i;
                System.out.println(i);
            }else{
                i++;
            }

        }
    }
}
