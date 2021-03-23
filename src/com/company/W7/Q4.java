package com.company.W7;

import java.util.Scanner;

public class Q4 { //p118 게임개발
    static int maprow;
    static int mapcol;
    static int [][] map ; //map size
    static int locationX; //주인공 좌표 x
    static int locationY; //주인공 좌표 y
    static int view;    //주인공 시점
    //북동남서 이동 정의
    static int [] rangeX = {-1,0,1,0};
    static int [] rangeY = {0,1,0,-1};
    static boolean[][] historyVisit; // 방문기록
    public void exe() throws Exception{
        Scanner sc=  new Scanner(System.in);
        // map size
         maprow = sc.nextInt();
        mapcol = sc.nextInt();
        // 차후에 저장할 map 배열
        map = new int[maprow][mapcol];
        // 주인공 위치
        locationX = sc.nextInt();
        locationY = sc.nextInt();
        // 주인공 시점
        // 0 : 북 / 1 : 동 /2 : 남 /3 : 서
        // 시점은 왼쪽으로 돈다. 0->3->2->1 ->0
        view = sc.nextInt();
        // 좌표 방문 이력
        historyVisit = new boolean[maprow][mapcol];
        // 주인공 처음위치 방문 기록

        historyVisit[locationX][locationY] = true;

        // 갈수 잇는 곳 개수
        int visitCount =1;

        int count =1; // 해당 위치에서 4번 회전하는지 확인




        //전체 맵 정보
        for(int i=0; i<maprow; i++){
            for(int j=0; j<mapcol; j++){
                map[i][j] = sc.nextInt();
            }
        }

        //input 끝

        //logic
        while (true){
            turn();
            if((map[locationX + rangeX[view]][locationY+rangeY[view]] == 0) //주인공이 바라보는 곳이 육지라면 !
                    && (historyVisit[locationX + rangeX[view]][locationY + rangeY[view]] == false)){ //가려는 곳이 방문이력이 없다면
                historyVisit[locationX + rangeX[view]][locationY+rangeY[view]] = true; //갔다고 치고 !
                visitCount++; //방문한 곳 하나 더 증가

                //그리로 이동
                locationX += rangeX[view];
                locationY += rangeY[view];
                // 둘러보기 0으로 초기화
                count =0;
            }else{
                count++;
            }
            if(count == 4) { //동서남북 다 봤어
                if (map[locationX - rangeX[view]][locationY - rangeY[view]] == 1) { //한칸뒤로 갈라니까 뒤에가 마주친 곳이 바다라면!
                    break;
                } else {    // 한칸 뒤로 가기
                    count = 0;
                    locationX -= rangeX[view];
                    locationY -= rangeY[view];
                }
            }
        }
        System.out.println(visitCount);

    }

    public void turn(){ //시점변환 함수
        view -=1;
        if(view < 0){
            view = 3;
        }
    }

}
