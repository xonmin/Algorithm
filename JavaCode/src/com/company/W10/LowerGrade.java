package com.company.W10;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class LowerGrade {



    public void exe(){
        Scanner sc = new Scanner(System.in);

        int n  = sc.nextInt();

       List<Student> studentList = new ArrayList<>();

       //input
       for(int i =0; i<n; i++){
           String name = sc.next();
           int grade = sc.nextInt();

           studentList.add(new Student(name,grade));
       }

        for(int i=0; i<n-1;i++){
            for(int j = 0; j<n-1-i; j++){
                Student first = studentList.get(j);
                Student second = studentList.get(j+1);
               int  fvalue = studentList.get(j).grade;
                int svalue = studentList.get(j+1).grade;
                int temp;
                if(fvalue > svalue){
                    temp = studentList.get(j).grade;
                    studentList.add(j,second);
                    studentList.remove(j+1);
                    studentList.add(j+1,first);
                    studentList.remove(j+2);
                }


            }
        }

        for(int i=0; i<n; i++){
            System.out.println(studentList.get(i).name);
        }

    }



    class Student implements Comparable<Student>{

        private String name;
        private int grade;


        public Student(String name, int grade) {
            this.name = name;
            this.grade = grade;
        }

        public String getName() {
            return name;
        }

        public int getGrade() {
            return grade;
        }


        @Override
        public int compareTo(Student o) {
            if(this.grade < o.grade){
                return -1;
            }
            return 1;
        }
    }





}
