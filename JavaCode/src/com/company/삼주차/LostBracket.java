package com.company.삼주차;

import java.util.Scanner;

public class LostBracket {

    public void exe(){
       Scanner sc = new Scanner(System.in);

       String str = sc.next();
       sc.close();
       String [] arr = str.split("-"); // - 기준으로  나눠서 배열에 담기

        int sum =0;
        for(String t : arr){    // - 이전까지 다 더하기
            // parseInt 로 string -> Int 형 리턴
            sum += Integer.parseInt(t);
        }

        int minus = 0; // - 이후 나오는 숫자들의 합
        for(int i= 1; i<arr.length;i++){    // arr[0] => 양의 값 sum 에 다 들어가 있기 때문에 - 이후 시작인 i=1 부터 시작
            String []tmp = arr[i].split("\\+"); // '+' 앞에는 \\를 붙여야 인식가능
            for(String t : tmp){
                minus += Integer.parseInt(t);
            }
        }

        System.out.println("결과 : "+ (sum-minus) );


    }

}
