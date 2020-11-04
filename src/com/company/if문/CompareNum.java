package com.company.if문;

import java.util.Scanner;

public class CompareNum {

    public void Compare(){
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt();
        int n2  =sc.nextInt();


        if(n1<n2) System.out.println(">");
        else if(n1<n2) System.out.println("<");
        else System.out.println("==");

        sc.close();
    }


}
