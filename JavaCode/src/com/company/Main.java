package com.company;

import com.company.W10.ElementChange;
import com.company.W10.ItemArrangement;
import com.company.W10.LowerGrade;
import com.company.W10.TopDown;
import com.company.W11.MakeTteokbokki;
import com.company.W11.NoShowContents;
import com.company.W11.SearchElement;
import com.company.W12.AntSoldier;
import com.company.W12.FloorWork;
import com.company.W12.MakeOne;
import com.company.W12.SightMoving;
import com.company.W7.*;
import com.company.W8.IcedJuice;
import com.company.W8.ImplementGame;
import com.company.W8.Q1_DFS;
import com.company.W9.DeliveryStrategy;
import com.company.W9.EscapeMaze;
import com.company.for문.LessThanX;
import com.company.for문.QuickPlus;
import com.company.for문.Sigma;

import com.company.if문.Alarm;
import com.company.if문.LeapYear;
import com.company.if문.Quadrant;
import com.company.kakaocodingtest.Q3;
import com.company.사주차.somastory.Execute;
import com.company.사칙연산.Multiplication;
import com.company.삼주차.Coin;
import com.company.삼주차.Zero;
import com.company.오주차.Treasure;
import com.company.이주차.Fibonazzi;
import com.company.첫주차.PrimeNumber;
import com.company.첫주차.Remainder;
import com.company.첫주차.Star;

import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws Exception {

        Q3 q3 = new Q3();

        int[] ans = q3.solution(new int[]{180, 5000, 10, 600}, new String[]{"05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"});
        for (int k : ans){
            System.out.println(k);
        }

    }


}
