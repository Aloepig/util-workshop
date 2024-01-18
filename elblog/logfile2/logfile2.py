import re


# 파일에서 https://를 추출하여 새 파일에 저장하는 함수
def extract_https(file_path, new_file_path):
    # 파일 읽기
    with open(file_path, 'r') as f:
        file_content = f.read()

    # https:// 추출
    https_list = re.findall(r'\w+ https://api.fanca.io+:443/[\w|/]+', file_content)
    total_count = 0

    with open(new_file_path, 'w') as f:
        for https in set(https_list):
            f.write(https + "," + str(https_list.count(https)) + '\n')
            total_count = total_count + https_list.count(https)

        f.write(new_file_path + " list:" + str(len(https_list)) + " count:" + str(total_count) + '\n')

    print(new_file_path + ' 파일에 https://가 저장되었습니다.')


# 로그파일명을 줄이는 함수
def get_save_list(log_list):
    file_list = []

    for file_name in log_list:
        file_list.append(re.sub("690116638181_elasticloadbalancing_ap-northeast-2_app.FANCAST-API.f638a8a6bfb2fb6d",
                                "FANCAST-API", file_name) + ".csv")

    return file_list


# 로그 파일 여러개를 한번에 분석
def create_log_analysis_file():
    folder_path = "/Users/leebyungjik/Documents/2024년 업무파일/2024년 1월/elblog240117/"
    log_list = [
        "690116638181_elasticloadbalancing_ap-northeast-2_app.FANCAST-API.f638a8a6bfb2fb6d_20240117T1400Z_3.37.22.240_dr1r2ls6",
        "690116638181_elasticloadbalancing_ap-northeast-2_app.FANCAST-API.f638a8a6bfb2fb6d_20240117T1400Z_3.37.22.240_dr1r2ls6 2",
        "690116638181_elasticloadbalancing_ap-northeast-2_app.FANCAST-API.f638a8a6bfb2fb6d_20240117T1400Z_43.202.161.149_445zhtw7",
        "690116638181_elasticloadbalancing_ap-northeast-2_app.FANCAST-API.f638a8a6bfb2fb6d_20240117T1400Z_52.78.8.187_1jlgx4tq",
        "690116638181_elasticloadbalancing_ap-northeast-2_app.FANCAST-API.f638a8a6bfb2fb6d_20240117T1405Z_3.37.22.240_1fdt3fcu",
        "690116638181_elasticloadbalancing_ap-northeast-2_app.FANCAST-API.f638a8a6bfb2fb6d_20240117T1405Z_43.200.197.221_4nudbb52",
        "690116638181_elasticloadbalancing_ap-northeast-2_app.FANCAST-API.f638a8a6bfb2fb6d_20240117T1405Z_52.78.8.187_1pllff2g",
        "690116638181_elasticloadbalancing_ap-northeast-2_app.FANCAST-API.f638a8a6bfb2fb6d_20240117T1410Z_3.37.22.240_3ec6rh9j",
        "690116638181_elasticloadbalancing_ap-northeast-2_app.FANCAST-API.f638a8a6bfb2fb6d_20240117T1410Z_43.200.197.221_270cq6tw",
        "690116638181_elasticloadbalancing_ap-northeast-2_app.FANCAST-API.f638a8a6bfb2fb6d_20240117T1410Z_52.78.8.187_2qpovtw5"
    ]

    analysis_list = get_save_list(log_list)

    for idx, log in enumerate(log_list):
        extract_https(folder_path + log + ".log", folder_path + analysis_list[idx])


create_log_analysis_file()

