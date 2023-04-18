import os
import re


# 문자열에서 IP 주소를 추출하는 함수를 정의합니다.
def extract_ip_address(string):
    # IP 주소를 추출하는 정규식 패턴을 지정합니다.
    pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

    # 정규식 패턴과 일치하는 문자열을 모두 추출합니다.
    matches = re.findall(pattern, string)

    # 추출한 IP 주소 리스트를 반환합니다.
    return matches


# 예시 문자열을 지정합니다.
# string = "This is an example text with IP address 192.168.0.1 and 10.0.0.1"

# 문자열에서 IP 주소를 추출합니다.
# ip_addresses = extract_ip_address(string)

# 추출된 IP 주소를 출력합니다.
# print(ip_addresses)


# 폴더 경로와 파일 개수를 지정합니다.
folder_path = "/Users/leebyungjik/s3backup"

# 폴더 안의 파일을 리스트로 저장합니다.
file_list = os.listdir(folder_path)

ip_set = {1}

Array_one = []

for log_file in file_list:
    print(log_file)
    if ".DS_Store" != log_file:
        file_path = os.path.join(folder_path, log_file)
        # 파일을 읽어와서 출력합니다.
        try:
            with open(file_path, "r") as file:
                lines = file.readlines()
                for log in lines:
                    if len(log) > 1:
                        # print(extract_ip_address(log))
                        ip_set.add(extract_ip_address(log)[0])
        except:
            print("error")
        finally:
            print(ip_set)
