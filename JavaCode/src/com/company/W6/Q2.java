package com.company.W6;

import java.util.*;

public class Q2 {
    // 2. 큰 수의 법칙
    public void exe(){

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();   //숫자의 개수
        int m = sc.nextInt();  //더해지는 횟수
        int k = sc.nextInt();  // 같은 숫자 연속 덧셈의 제한
        int sum = 0;
        Integer [] arr = new Integer[n];
        sc.nextLine();

        for(int i=0;i<n;i++){
            arr[i] =  sc.nextInt();
        }
    // input 끝
        // logic
        // 정렬
        Arrays.sort(arr, Collections.reverseOrder());
       int max  =  arr[0];
       int semi = arr[1];
       while(true){
           for(int i =0; i<k; i++) {
               if (m == 0) {
                   break;
               }
               sum += max;
               m -= 1;
           }
           if(m == 0 ){
               break;
           }
           sum += semi;
           m -=1;
       }

        System.out.println(sum);
    }

}
