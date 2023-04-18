import os

# 폴더 경로와 파일 개수를 지정합니다.
folder_path = "/Users/leebyungjik/s3backup/aws-logs-elb/fancast-api/AWSLogs/690116638181/elasticloadbalancing/ap-northeast-2/2023/04/205"

# 폴더 안의 파일을 리스트로 저장합니다.
file_list = os.listdir(folder_path)

# 파일 경로와 출력할 줄 번호를 입력합니다.
# filename = "690116638181_elasticloadbalancing_ap-northeast-2_app.FANCAST-API.f638a8a6bfb2fb6d_20230418T0300Z_15.165.184.157_32lqywfm.log"

for log_file in file_list:
    # print("===========")
    # print(log_file)
    # print("===========")
    file_path = os.path.join(folder_path, log_file)
    # 파일을 읽어와서 출력합니다.
    with open(file_path, "r") as file:
        lines = file.readlines()
        for log in lines:
            if "-1 -1 504" in log:
                print(log)


