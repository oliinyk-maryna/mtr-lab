    
"""
3. Лізингова компанія закуповує обладнання промислового призначення
з метою здачі його в оренду. При цьому можливі значні збитки із-за недостатньо добре дослідженого ринку. Виникають чотири можливі варіанти дій
в залежності від формування попиту на обладнання. Збитки при цьому
складають відповідно 300, 100, 200, та 400 грош.од. Відомі ймовірності цих
подій: р1=0,2, р2=0,3, р3= 0,1 та р4= 0,4. Знайти величину сподіваних збитків
та інші показники ризикованості.
"""
import math

loss1, loss2, loss3, loss4 = 300, 100, 200, 400  # Збитки для кожного варіанту дій
p1, p2, p3, p4 = 0.2, 0.3, 0.1, 0.4  # Відповідні ймовірності

expected_loss = (p1 * loss1) + (p2 * loss2) + (p3 * loss3) + (p4 * loss4)
print(f"Expected loss: {expected_loss:.2f} currency units")

variance = (p1 * (loss1 - expected_loss) ** 2) + \
           (p2 * (loss2 - expected_loss) ** 2) + \
           (p3 * (loss3 - expected_loss) ** 2) + \
           (p4 * (loss4 - expected_loss) ** 2)
print(f"Variance: {variance:.2f} currency units^2")

std_deviation = math.sqrt(variance)
print(f"Standard deviation: {std_deviation:.2f} currency units")