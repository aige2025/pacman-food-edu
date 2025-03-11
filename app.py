import os
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template, send_file

app = Flask(__name__)

# Create static/images directory if not exists
os.makedirs("static/images", exist_ok=True)

# Food data with fun facts
foods = [
    {"name": "Apple", "color": "red", "fact": "Apples keep your heart healthy!"},
    {"name": "Carrot", "color": "orange", "fact": "Carrots improve vision!"},
    {"name": "Banana", "color": "yellow", "fact": "Bananas give you energy!"},
    {"name": "Broccoli", "color": "green", "fact": "Broccoli boosts immunity!"},
    {"name": "Strawberry", "color": "pink", "fact": "Strawberries are full of vitamin C!"},
]

def generate_pacman():
    """Generates a Pac-Man image"""
    fig, ax = plt.subplots(figsize=(2, 2))
    ax.set_facecolor("black")

    # Draw Pac-Man
    pacman = plt.Circle((0, 0), 1, color="yellow", clip_on=False)
    ax.add_patch(pacman)

    # Draw the mouth (triangle)
    mouth = plt.Polygon([[0, 0], [1, 0.5], [1, -0.5]], color="black")
    ax.add_patch(mouth)

    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)

    # Save the figure
    plt.savefig("static/images/pacman.png", bbox_inches="tight", facecolor="black")
    plt.close()

def generate_food_image(food_name, color):
    """Generates food images"""
    fig, ax = plt.subplots(figsize=(2, 2))
    ax.set_facecolor("black")

    # Draw food (circle)
    food = plt.Circle((0, 0), 1, color=color, clip_on=False)
    ax.add_patch(food)

    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)

    # Save the image
    filename = f"static/images/{food_name.lower()}.png"
    plt.savefig(filename, bbox_inches="tight", facecolor="black")
    plt.close()

# Generate images for Pac-Man and food items
generate_pacman()
for food in foods:
    generate_food_image(food["name"], food["color"])

@app.route("/")
def index():
    return render_template("index.html", foods=foods)

@app.route("/static/images/<filename>")
def get_image(filename):
    return send_file(f"static/images/{filename}")

if __name__ == "__main__":
    app.run(debug=True)
