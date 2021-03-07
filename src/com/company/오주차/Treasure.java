package com.company.오주차;

import java.util.*;
import java.util.stream.Collectors;

public class Treasure {

    public void exe(){

        Scanner sc = new Scanner(System.in);

        int S = sc.nextInt();

        Integer []  A =  new Integer[S];
        Integer []  B =  new Integer[S];

        //data input
        for(int i = 0; i<S ; i++ ){
            A[i] = sc.nextInt();
        }
        for (int i= 0; i<S; i++){
            B[i]  = sc.nextInt();
        }

        //logic
        // A를 오름 차순 / B를 내림차순
        Arrays.sort(A);
        Arrays.sort(B, Collections.reverseOrder());

        //출력
        int sum =0;
        for(int i=0;i<S;i++){
            sum += A[i] * B[i];
        }
        System.out.println(sum);
    }


}
