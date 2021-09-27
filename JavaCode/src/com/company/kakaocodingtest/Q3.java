package com.company.kakaocodingtest;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class Q3 {

    public static int [] solution(int [] fees, String[] records){
        ArrayList<String> car_num = new ArrayList<>() ;
        Map<String, ParkingLotInfo> parkingInfoHashMap= new HashMap<>();

        for( String info : records){
            String[] park_info = info.split(" ");
            String car_license = park_info[1]; //차번호
            String InO = park_info[2];
            String time_info = park_info[0];

            if(InO.equals("IN")){
                ParkingLotInfo chk_past = parkingInfoHashMap.get(car_license);
                if (chk_past == null){ // 첫 입차
                    parkingInfoHashMap.put(car_license,new ParkingLotInfo(car_license,time_info));
                    car_num.add(car_license);
                }
                else {
                    chk_past.setIn_time(time_info);
                    System.out.println("입차 확인 : 차 번호 - " + car_license + "입차 :"+time_info);
                }

            }else{ //out
                ParkingLotInfo car = parkingInfoHashMap.get(car_license);
                car.setOut_time(time_info);
                //주차 시간 저장
                accumulate_time(car);
            }

        }
        // 차 별로 비용 계산
        // 만약 fee가 0 이라면 입차만 하고 출차를 안한 것 따라서 outime 23:59로 설정 후 계산
        car_num.sort(null);
        int [] answer = new int[car_num.size()];

       for (String key : car_num){
           ParkingLotInfo car = parkingInfoHashMap.get(key);
           System.out.println("차 번호 : " + key);
           int acc_time = car.getAcc_time();
           if (acc_time == 0){
               car.setOut_time("23:59");
               accumulate_time(car);
               acc_time = car.getAcc_time();
           }
           // 계산
           int the_fee = costcalc(fees, acc_time);

           // 배열에 넣기
            for (int i=0; i<answer.length;i++){
                answer[i] = the_fee;
                System.out.println("리턴된 값 :" + answer[i]);
            }
       }
        return answer;
    }

    private static int costcalc(int[] fees , int acc_time) {
        int default_time =  fees[0];
        int default_fee =  fees[1];
        int per_min= fees[2];
        int per_fee = fees[3];
        int cost = 0;
        System.out.println("누적된 시간 : "+ acc_time);
        if(acc_time < default_time){
            return default_fee;
        }
        cost = default_fee + (int)(Math.ceil((acc_time-default_time)/per_min)) * per_fee;
        System.out.println("기격 : "+ cost);
        return cost;
    }

    public static void accumulate_time(ParkingLotInfo car){
        String in_time = car.getIn_time();
        String out_time = car.getOut_time();

        String[] in_time_splited = in_time.split(":");
        int intime = Integer.parseInt(in_time_splited[0]) * 60 + Integer.parseInt(in_time_splited[1]);

        String[] out_time_splited = out_time.split(":");
        int outtime = Integer.parseInt(out_time_splited[0]) * 60 + Integer.parseInt(out_time_splited[1]);

        int exist_time = car.getAcc_time();
        car.setAcc_time(exist_time+ (outtime - intime));


    }
}


class ParkingLotInfo{
    String car_num;
    String in_time;
    String out_time;
    int acc_time  ;
    int fee;

    public int getAcc_time() {
        return acc_time;
    }

    public void setAcc_time(int acc_time) {
        this.acc_time = acc_time;
    }


    public ParkingLotInfo(String car_num, String in_time) {
        this.car_num = car_num;
        this.in_time = in_time;
        acc_time = 0;
        fee = 0;
    }

    public String getCar_num() {
        return car_num;
    }

    public void setCar_num(String car_num) {
        this.car_num = car_num;
    }

    public String getIn_time() {
        return in_time;
    }

    public void setIn_time(String in_time) {
        this.in_time = in_time;
    }

    public String getOut_time() {
        return out_time;
    }

    public void setOut_time(String out_time) {
        this.out_time = out_time;
    }

    public int getFee() {
        return fee;
    }

    public void setFee(int fee) {
        this.fee = fee;
    }
}
