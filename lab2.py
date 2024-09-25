
"""
3. Лізингова компанія закуповує обладнання промислового призначення
з метою здачі його в оренду. При цьому можливі значні збитки із-за недостатньо добре дослідженого ринку. Виникають чотири можливі варіанти дій
в залежності від формування попиту на обладнання. Збитки при цьому
складають відповідно 300, 100, 200, та 400 грош.од. Відомі ймовірності цих
подій: р1=0,2, р2=0,3, р3= 0,1 та р4= 0,4. Знайти величину сподіваних збитків
та інші показники ризикованості.
"""
import math

loss1, loss2, loss3, loss4 = 300, 100, 200, 400
p1, p2, p3, p4 = 0.2, 0.3, 0.1, 0.4

# 1. Очікувані збитки (Expected Loss)
expected_loss = (p1 * loss1) + (p2 * loss2) + (p3 * loss3) + (p4 * loss4)
print(f"Expected loss: {expected_loss:.2f} currency units")

# 2. Дисперсія (Variance)
variance = (p1 * (loss1 - expected_loss) ** 2) + \
           (p2 * (loss2 - expected_loss) ** 2) + \
           (p3 * (loss3 - expected_loss) ** 2) + \
           (p4 * (loss4 - expected_loss) ** 2)
print(f"Variance: {variance:.2f} currency units^2")

# 3. Стандартне відхилення (Standard Deviation)
std_deviation = math.sqrt(variance)
print(f"Standard deviation: {std_deviation:.2f} currency units")

# 4. Семіваріація (Semivariance)
semi_variance = (p1 * max(0, (loss1 - expected_loss)) ** 2) + \
                (p2 * max(0, (loss2 - expected_loss)) ** 2) + \
                (p3 * max(0, (loss3 - expected_loss)) ** 2) + \
                (p4 * max(0, (loss4 - expected_loss)) ** 2)
print(f"Semivariance: {semi_variance:.2f} currency units^2")

# 5. Семіквадратичне відхилення (Semideviation)
semi_deviation = math.sqrt(semi_variance)
print(f"Semideviation: {semi_deviation:.2f} currency units")

# 6. Негативна семіваріація (Negative Semivariance) - враховує лише збитки нижче очікуваних
negative_semi_variance = (p1 * min(0, (loss1 - expected_loss)) ** 2) + \
                         (p2 * min(0, (loss2 - expected_loss)) ** 2) + \
                         (p3 * min(0, (loss3 - expected_loss)) ** 2) + \
                         (p4 * min(0, (loss4 - expected_loss)) ** 2)
negative_semi_variance = abs(negative_semi_variance)
print(f"Negative Semivariance: {negative_semi_variance:.2f} currency units^2")

# 7. Негативне семіквадратичне відхилення (Negative Semideviation)
negative_semi_deviation = math.sqrt(negative_semi_variance)
print(f"Negative Semideviation: {negative_semi_deviation:.2f} currency units")
