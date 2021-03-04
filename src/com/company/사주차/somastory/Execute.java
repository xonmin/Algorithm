package com.company.사주차.somastory;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Execute {

    public  void exe() {
        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine();
        String[] arr = input.split(" ");
        List<Node> allSkill = new ArrayList<>(); // 첫 스킬 종류를 담아놓을 Node List


        for(String s : arr){
            Node node = new Node(s); //각 스킬 노드 생성
          allSkill.add(node);
        }


        int size = sc.nextInt(); // 스킬셋 연계 개수

        // Node currentNode = new Node();
        sc.nextLine();
        for(int i=0;i <size;i++){

            String set = sc.nextLine(); // input : skill 연계 ex) x y
            String [] arr2 = set.split(" ");

//        for(String s : arr2){ // 스킬 연계 문자하나하나
//            for(i = 0; i<allSkill.size();i++){
//                Node tmp = allSkill.get(i);
//            if(s == tmp.data){
//
//            }
            for(Node p : allSkill){
               if( p.data.equals(arr2[0])){  //첫번째 문자와 맞는 노드 찾기
                  for(Node c : allSkill){
                      if(c.data.equals(arr2[1])){ // 두번째 문자와 맞는 데이터를 가진 노드 찾기
                          p.setChild(c);  // 자식 조건 부여
                          c.setPre(p); // 부모 조건 부여
                            break;
                      }
                    }
               }
               break;
            }
        }

     // 출력


     }
}
