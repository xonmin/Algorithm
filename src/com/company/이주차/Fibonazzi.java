package com.company.이주차;

public class Fibonazzi {
    public int exe(int n){

        if(n ==1){

            return 1;
        }else if(n ==0){
            return 0;
        }else{



            return exe(n-1 ) + exe(n-2);



        }


    }
}
