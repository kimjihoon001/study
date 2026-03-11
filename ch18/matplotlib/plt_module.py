# plt_module.py
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,25,30]
# plt.plot(x,y)
# plt.title('Line Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()

# 한글 폰트 설정
# plt.rcParams['font.family'] = 'Malgun Gothic'   # windows 사용자
# plt.rcParams['font.family'] = 'AppleGothic'     # Mac 사용자
# plt.rcParams['font.family'] = 'NanumGothic'     # Linux 사용자 (설치 필요)

# # 막대 그래프
# categories = ["A", "B", "C", "D"]
# values = [3, 7, 8, 5]
# plt.bar(categories, values)
# plt.title("막대 그래프")
# plt.show()


# 히스토그램
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(data, bins=4, color="skyblue", edgecolor="black")
plt.title("Histogram")
plt.show()