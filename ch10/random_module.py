import random

# 시드 : 같은 결과를 보장
# random.seed(4)

animals = ['체셔고양이', '오리', '도도새']

print(random.choice(animals))


nums = [i for i in range(1,46)]
print(nums)
print(random.sample(nums,6))
print(random.randint(1,45))