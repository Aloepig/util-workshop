# 파일 경로와 출력할 줄 번호를 입력합니다.
filename = "690116638181_elasticloadbalancing_ap-northeast-2_app.FANCAST-API.f638a8a6bfb2fb6d_20230418T0300Z_15.165.184.157_32lqywfm.log"

# 파일을 읽어와서 출력합니다.
with open(filename, "r") as file:
    lines = file.readlines()
    for log in lines:
        if "-1 -1 504" in log:
            print(log)
