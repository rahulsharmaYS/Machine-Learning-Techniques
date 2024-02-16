import matplotlib.pyplot as plt

<<<<<<< HEAD
#Using example datapoints to practice representation learning ~
=======
#Using example data points to practice representation learning ~
>>>>>>> 4cb9f43ab1b42dfa53446d4eba1454e2f78e1870
height = [150, 160, 170, 180, 190, 160, 160]
weight = [50, 60, 70, 80, 90, 45, 80]
age = [25, 30, 35, 40, 45, 42, 40]

plt.scatter(height, weight, c=age, cmap='cool', s=100)

plt.xlabel('height (cm)')
plt.ylabel('weight (kg)')
plt.title('height vs weight vs age')
plt.colorbar(label='Age')
plt.grid(True)

plt.show()
