import numpy as np
import matplotlib.pyplot as plt
import math


# create random values for the face features
features = np.random.randint(100,700, size=10)
features = [f/1000 for f in features]
#print(features)

# Create canvas
fig, ax = plt.subplots()

# Set axis limits
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')

# Draw face outline
face_outline = plt.Circle(xy=(0, 0), radius=1, color='lightgray', fill=True)
ax.add_patch(face_outline)

# Draw eyes
eye_size = features[0]
eye_spacing = features[1]*2
eye_height = features[2]
eye_color = tuple(features[3:6])  # Use a tuple for RGB color
eye1_x = -eye_spacing / 2
eye2_x = eye_spacing / 2
eye1_y = eye2_y = 0.25

eye_size_inside = eye_size/5
eye_displacement = eye_size_inside*2
eye_color_inside = (0,0,0)
angle = np.random.random()*1000
eye1_x_inside = eye1_x - (eye_displacement*math.cos(angle))
eye2_x_inside = eye2_x - (eye_displacement*math.cos(angle))
eye1_y_inside = eye1_y - (eye_displacement*math.sin(angle))
eye2_y_inside = eye2_y - (eye_displacement*math.sin(angle))

eye1 = plt.Circle((eye1_x, eye1_y), eye_size, color=eye_color, fill=True)
eye2 = plt.Circle((eye2_x, eye2_y), eye_size, color=eye_color, fill=True)
eye1_inside = plt.Circle((eye1_x_inside, eye1_y_inside), eye_size/5, color=eye_color_inside, fill=True)
eye2_inside = plt.Circle((eye2_x_inside, eye2_y_inside), eye_size/5, color=eye_color_inside, fill=True)

# Draw mouth
mouth_width = features[7]*1.5
mouth_height = 0.05
mouth_angle = 0
mouth = plt.Rectangle((-mouth_width / 2, -0.55), mouth_width, mouth_height, angle=mouth_angle, color='red', fill=True)

# Add face items to the plot
ax.add_patch(eye1)
ax.add_patch(eye2)
ax.add_patch(eye1_inside)
ax.add_patch(eye2_inside)
ax.add_patch(mouth)

# Remove axis labels
ax.set_xticks([])
ax.set_yticks([])

plt.show()