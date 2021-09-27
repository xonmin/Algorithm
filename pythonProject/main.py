# 카카오 코딩 테스트 3번 주차장 요금

# fees : [180, 5000, 10, 600]
# records :
# ["05:34 5961 IN",
# "06:00 0000 IN",
# "06:34 0000 OUT",
# "07:59 5961 OUT",
# "07:59 0148 IN",
# "18:59 0000 IN",
# "19:09 0148 OUT",
# "22:59 5961 IN",
# "23:00 5961 OUT"]

def solution(fees, records):
    default_time, default_fee, per_min, per_fee = fees
    in_parking = []
    for info in records:
