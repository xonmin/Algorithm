package com.company;

import com.company.for문.LessThanX;
import com.company.for문.QuickPlus;
import com.company.for문.Sigma;

import com.company.if문.Alarm;
import com.company.if문.LeapYear;
import com.company.if문.Quadrant;
import com.company.사칙연산.Multiplication;
import com.company.삼주차.Coin;
import com.company.이주차.Fibonazzi;
import com.company.첫주차.PrimeNumber;
import com.company.첫주차.Remainder;
import com.company.첫주차.Star;

import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {

        Coin coin = new Coin(10);
        coin.exe(10,4200);
    }
}
