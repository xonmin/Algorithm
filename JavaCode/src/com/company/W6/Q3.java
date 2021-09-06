package com.company.W6;

import java.util.Arrays;
import java.util.Scanner;

public class Q3 { //숫자 카드 게임
    public void exe() {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // 행
        int m = sc.nextInt(); // 열
        //input
        Integer[][] arr = new Integer[m][n];
        for(int i=0; i<m; i++){
            for(int j=0;j<n;j++){
                arr[i][j] = sc.nextInt();
            }
        }
        //낮은 수 정렬
        Arrays.sort(arr[0]);
        Arrays.sort(arr[1]);
        Arrays.sort(arr[2]);
        int max = arr[0][0];
        // 최대 값 출력
        if(max  < arr[1][0]){
            max = arr[1][0];
        }
        if(max < arr[2][0])
            max = arr[2][0];
        System.out.println(max);
    }


}
