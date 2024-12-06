import pygame
import random

def play_hint_animation(screen, hint, background_color):
    for _ in range(30):  # Short animation loop
        screen.fill(background_color)
        for _ in range(10):
            x = random.randint(0, screen.get_width())
            y = random.randint(0, screen.get_height())
            size = random.randint(10, 50)
            color = random.choice([(0, 255, 255), (255, 255, 255), (0, 0, 0)])  # Miku's colors
            pygame.draw.circle(screen, color, (x, y), size)
        pygame.display.flip()
        pygame.time.delay(50)  # Slower animation

    # Return the hint text to be displayed after the animation
    return hint
