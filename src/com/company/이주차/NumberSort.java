package com.company.이주차;

import java.util.ArrayList;
import java.util.List;

public class NumberSort {

    public void exe( int[] arr) {
            for(int i=0; i<arr.length;i++){
                for(int j= i+1;j<arr.length;j++){
                    if(arr[i]> arr[j]){
                        int swap = arr[i];
                        arr[i] = arr[j];
                        arr[j] = swap;
                    }
                }
        }
           for(int i=0; i<arr.length;i++){
               System.out.println(arr[i]);
           }
    }

    public void exe2(){
        // scaner 쓰고
        // for 문쓰고
        List<Integer> arr = new ArrayList<>();
        arr.sort(null);
        System.out.println(arr.toString());
    }
}
