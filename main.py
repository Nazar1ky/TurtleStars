from turtle import *
import random

used_coordinates = []
errors = 0

size = 15

bgcolor("black")
speed(10)

def draw_star(x, y, color = "white"):
  """Draw Star"""
  up()
  goto(x, y)
  down()
  for i in range(5):
    forward(size)
    right(144)

def check_star_near(x, y):
    """Check if Star Near. If Yes > False."""
    radius = size + 3
    for coordinates in used_coordinates:
        if abs(coordinates[0] - x) < radius and abs(coordinates[1] - y) < radius:
            return False
    return True

def main():
    while True:
        if errors > 100:
            break

        x = random.randint(-190, 140)
        y = random.randint(-140, 170)

        if check_star_near(x,y):
            errors = 0 # Reset Errors
            draw_star(x,y)
            used_coordinates.append([x, y])
        else:
            errors += 1

    print("Random ended. Using alghoritm for now.")

    for x in range(-190, 140):
        for y in range(-140, 170):
            if check_star_near(x,y):
              draw_star(x, y)
              used_coordinates.append([x, y]) 

if __name__ == "__main__":
    main()
