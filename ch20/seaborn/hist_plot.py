# hist_plot.py

import seaborn as sns
import matplotlib.pyplot as plt

# 1. 샘플 데이터 셋 로드
iris = sns.load_dataset('iris')

# 2. 스타일 설정 
sns.set_theme(style='darkgrid',
              palette='muted')

# 3. 그래프 표시
sns.histplot(
        data=iris,
        x='sepal_length',
        hue='species',
        kde=True
        )

plt.title('Histogram Plot Example')
plt.show()