package com.company;

import com.company.for문.QuickPlus;
import com.company.for문.Sigma;
import com.company.for문.Star;
import com.company.if문.Alarm;
import com.company.if문.LeapYear;
import com.company.if문.Quadrant;
import com.company.사칙연산.Multiplication;

import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {
        Scanner sc= new Scanner(System.in);
        int k = sc.nextInt();
        Star star = new Star();
        star.Exe(k);

    }
}
