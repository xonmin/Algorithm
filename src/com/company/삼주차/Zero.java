package com.company.삼주차;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Stack;

public class Zero {


    public void exe(){
        Scanner sc = new Scanner(System.in);
        int sum=0;
        int size = sc.nextInt();
        Stack<Integer> stack = new Stack<>();

        for(int i =0;i<size;i++){
            int input = sc.nextInt();
            if(input ==0){
                stack.pop();
            }else{
                stack.push(input);
            }

        }
        sc.close();
        for(int i : stack){
           sum += i;
        }
        System.out.println(sum);
    }
}
