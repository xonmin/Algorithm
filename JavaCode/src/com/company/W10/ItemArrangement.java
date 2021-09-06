package com.company.W10;

import java.util.Scanner;

public class ItemArrangement {

    public static int [][] map ; // 전체 진열대
  //  public static int [][] comp; // 상품 크기
    public int N ; // map size
    public static int [] count;
    public int sum;
    public void exe() {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        map = new int[N][N];
        sc.nextLine();

        for (int i = 0; i < N; i++) {     //map input
            String input = sc.nextLine();
            for (int j = 0; j < N; j++) {
                map[i][j] = input.charAt(j) - '0';
            }
        }
        count = new int[N+1];
        sc.close();
        //input  종료

        // 밑에 방식으로 하게되면 배열은 우측과 하단으로 찾으러 가는데 map[i][j] 에 값을 넣어버리면 그의 우측과 하단은 값이 변하지 않게 됨

//        for(int i=0; i<N; i++){
//            for(int j =0; j<N; j++){
//                if( map[i][j] == 1){
//                    if(i+1<N && j+1<N && map[i+1][j] ==1 && map[i][j+1] == 1 && map[i+1][j+1] == 1) {
//                            map[i][j] = Math.min(map[i + 1][j], Math.min(map[i][j + 1], map[i + 1][j + 1])) + 1;  //가능한 정사각형 파악
//                        }
//                }
//            }
//        }
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if(map[i][j]>0){
                    if(i>0 && j>0 && map[i-1][j]>0&& map[i][j-1] >0 && map[i-1][j-1] >0){
                        map[i][j] = Math.min(map[i-1][j],Math.min(map[i][j-1],map[i-1][j-1]))+1;
                    }
                }
            }
        }

        int M = 0;
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                 M = Math.max(M,map[i][j]); //정사각형 최대 사이즈 파악
            }
        }

        for(int i=0; i<N; i++){
            count[i] = 0; //count 값 초기화
        }

        for(int k =1; k<=M; k++){
            for(int i=0; i<N;i++){
                for(int j = 0; j<N; j++){
                    if(map[i][j] >=k){
                        count[k]++;
                    }
                }
            }
        }

        for(int i=0; i<=M; i++){
            sum += count[i];  // 각 사이즈 별 가능한 정사각형 sum 총합 더하기
        }

        System.out.println("총 가능한 배치 개수 : "+sum);
        for(int i=1; i<=M; i++){
            System.out.printf("size[%d] :  %d\n",i,count[i]);
        }

    }



}

