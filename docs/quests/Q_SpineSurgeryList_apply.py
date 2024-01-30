# - apply() 적용 BMI 컬럼 생성
# - BMI = 체중(kg) / (키(m), 신장)^2 (**2)

import pandas as pd
file_path = 'docs/quests/SpineSurgeryList.csv'      # csv 파일 불러오기
df_SSList = pd.read_csv(file_path)
print(df_SSList)

print(df_SSList.columns)
# Index(['Unnamed: 0', '환자ID', 'Large Lymphocyte', 'Location of herniation',
#        'ODI', '가족력', '간질성폐질환', '고혈압여부', '과거수술횟수', '당뇨여부', '말초동맥질환여부', '빈혈여부',
#        '성별', '스테로이드치료', '신부전여부', '신장', '심혈관질환', '암발병여부', '연령', '우울증여부', '입원기간',
#        '입원일자', '종양진행여부', '직업', '체중', '퇴원일자', '헤모글로빈수치', '혈전합병증여부', '환자통증정도',
#        '흡연여부', '통증기간(월)', '수술기법', '수술시간', '수술실패여부', '수술일자', '재발여부', '혈액형',
#        '전방디스크높이(mm)', '후방디스크높이(mm)', '지방축적도', 'Instability', 'MF + ES',
#        'Modic change', 'PI', 'PT', 'Seg Angle(raw)', 'Vaccum disc', '골밀도',
#        '디스크단면적', '디스크위치', '척추이동척도', '척추전방위증'],
#       dtype='object')


print(df_SSList[['환자ID','체중','신장']])


# 풀이 1
def receive_params(params):          # BMI 계산 함수
    BMI = params.loc['체중']/((params.loc['신장']*0.1)**2)       # 신장과 체중 내용으로 BMI를 계산
    return params
df_SSList[['신장','체중']].apply(receive_params, axis=1)
pass

# 풀이 2
def receive_params(params):
    BMI = params['체중'] / (params['신장'] * 0.1 ** 2)
    return params

df_SSList[['신장','체중']].apply(receive_params, axis=1)
pass