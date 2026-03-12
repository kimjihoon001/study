# plt_module.py
import matplotlib.pyplot as plt

# x = [1,2,3,4]
# y = [10,20,25,30]
# plt.plot(x,y)
# plt.title('Line Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'   # windows 사용자
# plt.rcParams['font.family'] = 'AppleGothic'     # Mac 사용자
# plt.rcParams['font.family'] = 'NanumGothic'     # Linux 사용자 (설치 필요)
# print('----------------------')
# # 막대 그래프
# categories = ["A", "B", "C", "D"]
# values = [3, 7, 8, 5]
# plt.bar(categories, values)
# plt.title("막대 그래프")
# plt.show()


# print('----------------------')
# # 히스토그램
# data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# plt.hist(data, bins=4, color="skyblue", edgecolor="black")
# plt.title("Histogram")
# plt.show()

# 구간 크기 계산
# (최댓값-최솟값) / bins

# print('----------------------')
# x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
# y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]
# plt.scatter(x, y, color="green")
# plt.title("Scatter Plot")
# plt.show()

# print('----------------------')
# sizes = [15, 30, 45, 10]
# labels = ["Group A", "Group B", "Group C", "Group D"]
# plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90,counterclock= False)
# plt.title("Pie Chart")
# plt.show()

# print('----------------------')

# data = [7, 8, 5, 6, 8, 9, 6, 7, 5, 8]
# plt.boxplot(data)
# plt.title("Box Plot")
# plt.show()

# 이상치(outlier) : 대부분의 데이터 패턴에서 크게 벗어난 값
# 이상치 생성 이유: 측정오류, 데이터 처리 오류, 실제 특이한 사건
# 이상치 발생시 처리 방법
# 1. 제거(삭제)
# 입력/측정/데이터 수집 오류
# 2. 값 수정(대처)
# 평균값, 중앙값,최빈값 등으로 바꾸는 방법
# 3. 윈저라이징
# 극단값을 최대/최소 범위 값으로 바꾸는 방법
# 4. 로그 변환(데이터 변환)
# 데이터 분포를 줄이는 방법
# 5. 그대로 사용


# IQR 기준 계산
# IQR = Q3 -Q1
# lower = Q1 - 1.5 * IQR
# upper = Q3 - 1.5 * IQR


# print('----------------------')
# x = [1,2,3,4]
# y = [10,20,25,30]
# # plt.plot(x, y, color="red", linestyle="--", marker="*")
# # plt.plot(x, y, color="blue", linestyle="-", marker="^")
# plt.plot(x,y,"k^:")
# plt.title("Customized Line Plot")
# plt.show()

# linestyle : '-' '--' ':' '-.' ...
# marker : '.' ',' 'o' '^' 'v'  ...


# print('----------------------')
# x = [1,2,3,4]
# y = [10,20,25,30]
# plt.plot(x,y,"k^:")
# plt.plot(x, y)
# plt.xlim(0, 5)
# plt.ylim(0, 40)
# plt.xticks(range(1, 5))
# plt.yticks(range(0, 41, 10))
# plt.show() 


# print('----------------------')
# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]
# x1 = [1, 2, 3, 4]
# y2 = [3, 5, 9, 7]
# plt.plot(x, y, label="Data 1")
# plt.plot(x1, y2, label="Data 2")
# plt.legend(loc="upper left")
# plt.savefig(r'ch18\matplotlib\my_plot.png')
# plt.show()


print('----------------------')

x = [1,2,3,4]
y = [10,20,25,30]
categories = ["A", "B", "C", "D"]
values = [3, 7, 8, 5]
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# fig : 전체 그래프창
# axs : subplot(그래프 영역)

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 1].bar(categories, values)
axs[1, 0].scatter(x, y)
axs[1, 1].hist(data)
fig.suptitle('전체 그래프 제목')
plt.tight_layout()
plt.show()
