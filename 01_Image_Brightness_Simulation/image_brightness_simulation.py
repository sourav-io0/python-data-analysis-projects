import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Image Brightness Simulation
# -------------------------------

# Create a 5x5 grayscale image
image = np.array([
    [50, 80, 120, 180, 220],
    [40, 90, 130, 170, 210],
    [30, 100, 140, 160, 200],
    [20, 110, 150, 190, 230],
    [10, 60, 125, 175, 255]
])

# Increase brightness
bright_image = np.clip(image + 30, 0, 255)

# Decrease brightness
dark_image = np.clip(image - 30, 0, 255)

# Flip horizontally
flip_horizontal = np.fliplr(image)

# Flip vertically
flip_vertical = np.flipud(image)

# Rotate 90 degrees
rotated_image = np.rot90(image)

# -------------------------------
# Display Results
# -------------------------------

titles = [
    "Original",
    "Brightened",
    "Darkened",
    "Flip Horizontal",
    "Flip Vertical",
    "Rotated 90°"
]

images = [
    image,
    bright_image,
    dark_image,
    flip_horizontal,
    flip_vertical,
    rotated_image
]

plt.figure(figsize=(10,6))

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i], cmap="gray", vmin=0, vmax=255)
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()

# -------------------------------
# Print Arrays
# -------------------------------

print("Original Image:\n", image)
print("\nBrightened Image:\n", bright_image)
print("\nDarkened Image:\n", dark_image)
print("\nHorizontally Flipped Image:\n", flip_horizontal)
print("\nVertically Flipped Image:\n", flip_vertical)
print("\nRotated Image:\n", rotated_image)
