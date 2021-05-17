package com.company.W11;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;


class Contents implements Comparable<Contents>{

    char reading;
    char genre;
    int index;
    double eval ;
    int col;
    int row;

    public Contents(char reading, char genre, double eval, int index, int row, int col) {
        this.reading = reading;
        this.genre = genre;
        this.index = index;
        this.eval = eval;
        this.col = col;
        this.row = row;
    }



    //우선순위가 높으면 음수를 리턴
    // 같으면 0
    // 우선순위가 낮으면 양수를 리턴

      /*
        - 'O' → 유저가 열람했으나 끝까지 보지 않은 컨텐츠
        - 'W' → 유저가 열람했으며 끝까지 본 콘텐츠
        - 'Y' → 유저가 열람한 적 없는 콘텐츠
         */

    // 정렬 기준  : 1. 유저가 열람한 적 없는
    //            2. 장르의 선호도가 높은
    @Override
    public int compareTo(Contents c) {
        if(this.reading == 'Y'){
            if(c.reading == 'Y'){ //둘다 안본 컨텐츠 일 때
                if(this.eval > c.eval){ //기준의 장르 선호도가 더 높으면
                    return -1;

                }else if(this.eval == c.eval){ //다같아
                    if(this.index < c.index){ //먼저 입력된 놈 먼저 출력
                        return  -1;
                    }
                    return 1;
                }
                //비교하는 애의 장르 선호도가 더 높으면
                return 1;
            }
            //비교하는 애의 열람여부가 본적이 있다면
            return -1;

        }else if(this.reading == 'O'){
            if(c.reading == 'Y'){
                return 1;
            }else if(c.reading == 'O'){
                if(this.eval > c.eval){
                    return -1;
                }else if(this.eval == c.eval){

                    if(this.index < c.index){
                        return  -1;
                    }
                    return 1;
                }
                return 1;
            }
            return -1; //비교하는 친구가 다 본 놈일 때
        }else{
            if(c.reading == 'W'){
                if(this.eval > c.eval){
                    return -1;
                }else if(this.eval == c.eval){
                    if(this.index < c.index){
                        return  -1;
                    }
                    return 1;
                }
            }else {
                return 1;
            }
        }
        return  1;
    }
}


public class NoShowContents {

    public static int N , M ;

    public static char [][]  progress;  //열람정보

    public static char [][] genre ; // 장르정보  01234 / ABCDE

    public void exe(){
        //장르별 선호도 평가
        double [] eval = new double[5];

        Scanner  sc = new Scanner(System.in);
        for(int i=0; i<5;i++){
            eval[i] = sc.nextDouble();
        }

        N = sc.nextInt();
        M = sc.nextInt();

        progress = new char[N][M];
        genre = new char[N][M];
        sc.nextLine();

        for(int i=0;i <N;i++){
            String input  = sc.nextLine();
            for(int j = 0; j<M; j++){
                progress[i][j] = input.charAt(j);
            }
        }

        for(int i=0; i<N;i++){
            String input = sc.nextLine();
            for(int j=0;j<M; j++) {
            genre[i][j] = input.charAt(j);
            }
        }
        //input 종료
        sc.close();

        /*
        - 'O' → 유저가 열람했으나 끝까지 보지 않은 컨텐츠
        - 'W' → 유저가 열람했으며 끝까지 본 콘텐츠
        - 'Y' → 유저가 열람한 적 없는 콘텐츠
         */

        // 정렬 기준  : 1. 유저가 열람한 적 없는
        //            2. 장르의 선호도가 높은


        List<Contents> contentsList = new ArrayList<>();
        int index = 0;

        for(int i=0 ;i<N;i++){
            for(int j=0;j <M; j++){
                if(genre[i][j] == 'A') {
                    contentsList.add(new Contents(progress[i][j], genre[i][j],eval[0], index,i,j));
                }else if(genre[i][j] == 'B'){
                    contentsList.add(new Contents(progress[i][j], genre[i][j],eval[1], index,i,j));
                }else if(genre[i][j] == 'C'){
                    contentsList.add(new Contents(progress[i][j], genre[i][j],eval[2], index,i,j));
                }else if(genre[i][j] == 'D'){
                    contentsList.add(new Contents(progress[i][j], genre[i][j],eval[3], index,i,j));
                }else{
                    contentsList.add(new Contents(progress[i][j], genre[i][j],eval[4], index,i,j));
                }
                index++;
            }
        }

        Collections.sort(contentsList);

        for(Contents c : contentsList){
            System.out.printf("%c %.1f %d %d \n",c.genre,c.eval,c.row,c.col);
        }

    }





}

