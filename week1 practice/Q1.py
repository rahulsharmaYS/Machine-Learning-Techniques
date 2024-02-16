import matplotlib.pyplot as plt

#Using example datapoints to practice representation learning ~
height = [150, 160, 170, 180, 190, 160]
weight = [50, 60, 70, 80, 90]
age = [25, 30, 35, 40, 45]

plt.scatter(height, weight, c=age, cmap='cool', s=100)

plt.xlabel('height (cm)')
plt.ylabel('weight (kg)')
plt.title('height vs weight vs age')
plt.colorbar(label='Age')
plt.grid(True)

plt.show()
