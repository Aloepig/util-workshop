# https://xn--3e0bx5euxnjje69i70af08bea817g.xn--3e0b707e/jsp/statboard/IPAS/ovrse/natal/IPaddrBandCurrent.jsp?nationCode1=JP
# 국가별 ip 대역은 KISA 에서 확인 가능
with open('ip_block_auonenet.txt', 'r') as file:
    for line in file:
        if '103.246.66' in line:
            print(line)
        elif '103.246.67' in line:
            print(line)
        elif '103.246.72' in line:
            print(line)
        elif '103.246.73' in line:
            print(line)
        elif '103.232.22' in line:
            print(line)
        elif '103.232.23' in line:
            print(line)
        elif '103.235.180' in line: # 2023년 추가된 ip 여기까지
            print(line)
        elif '106.128' in line: # 차단된 ip
            print(line)
