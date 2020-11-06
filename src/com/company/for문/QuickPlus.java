package com.company.for문;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class QuickPlus {

    public void Exe() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());


        StringTokenizer st;
        for(int i =0; i<num; i++){
        st = new StringTokenizer(br.readLine()," "); //띄어쓰기 식별
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
            System.out.println(a+b);



        }

    }

}
