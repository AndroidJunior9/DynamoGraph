import matplotlib.pyplot as plt
import numpy as np

# Initialize your time and distance lists
time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # time in seconds
distance = [0,1,4,8,22,39,60,77,90,97,100]  # distance in meters

# Calculate velocity (v = d/t)
velocity = np.diff(distance) / np.diff(time)

# Create time points for velocity by removing the last time point
time_velocity = time[:-1]

# Plot distance over time
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(time, distance, marker='o')
plt.title('Distance over Time')
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')

# Plot velocity over time
plt.subplot(1, 2, 2)
plt.plot(time_velocity, velocity, marker='o')
plt.title('Velocity over Time')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')

plt.tight_layout()
plt.show()
