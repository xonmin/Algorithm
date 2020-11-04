package com.company.if문;

import java.util.Scanner;

public class ExamGrade {


    public void Exe(){

        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt();

        if(n1>=90 && n1<= 100) System.out.println("A");
        else if(n1>=80 && n1<90 ) System.out.println("B");
        else if(n1>=70 && n1<80) System.out.println("C");
        else if(n1>=60 && n1<70) System.out.println("D");
        else System.out.println("F");
    }

}
