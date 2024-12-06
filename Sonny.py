import pygame
import random
from animations import play_hint_animation
from songs import get_random_song
import webbrowser  # Import for opening the GitHub link

# Initialize Pygame
pygame.init()

# Initialize global variables
current_song = get_random_song()  # Load the first random song
player_answer = ""                # Initialize the player's answer as an empty string
feedback_text = ""                # Initialize feedback as an empty string


# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sonny - Singleplayer")

# Colors
BACKGROUND_COLOR = (10, 10, 30)
BUTTON_COLOR = (100, 100, 255)
TEXT_COLOR = (255, 255, 255)

# Clock for FPS control
clock = pygame.time.Clock()
FPS = 60

# Font
font = pygame.font.Font("fonts/PixelifySans-Regular.ttf", 36)

# Button position and size
button_rect = pygame.Rect(WIDTH - 150, HEIGHT - 130, 120, 50)

# Game states
START_MENU = "start_menu"
GAME = "game"
PAUSE_MENU = "pause_menu"
current_state = START_MENU
game_mode = None  # Tracks the selected game mode ("speed_run" or "regular")


# Load a random song
current_song = get_random_song()

# Player input and feedback
player_answer = ""
feedback_text = ""

# Particle system for cursor
particles = []

# Hint animation control
hint_active = False
hint_text = ""
hint_start_time = 0  # Track the start time of the hint animation
hint_display_active = False  # To show the hint text after the animation

def end_screen():
    global current_state

    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)

        # Display the final score
        end_text = font.render("Game Over! (QAQ)", True, TEXT_COLOR)
        score_text = font.render(f"Your Final Score: {total_score}", True, TEXT_COLOR)

        screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, HEIGHT // 3))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))

        # Add a button to return to the main menu
        main_menu_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 50)
        draw_button(main_menu_button, "Main Menu")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_menu_button.collidepoint(event.pos):
                    current_state = START_MENU
                    running = False

        pygame.display.flip()
        clock.tick(FPS)


# Draw buttons side by side with proper spacing
def draw_button(rect, label_text):
    # Draw button background with Miku colors and Christmas style
    pygame.draw.rect(screen, (57, 197, 187), rect, border_radius=5)  # Miku teal base
    pygame.draw.rect(screen, (0, 209, 206), rect, 3, border_radius=5)  # Teal border

    # Add the label text
    label = font.render(label_text, True, TEXT_COLOR)
    label_rect = label.get_rect(center=rect.center)
    screen.blit(label, label_rect)


# Render wrapped text
def render_wrapped_text(text, x, y, font, color, max_width):
    words = text.split(' ')
    lines = []
    current_line = ''

    for word in words:
        test_line = f"{current_line} {word}".strip()
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)

    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        screen.blit(text_surface, (x, y + i * font.get_linesize()))

# Add particle for cursor animation
def add_particle(position):
    particles.append({
        "pos": position,
        "radius": 5,
        "growth": random.uniform(0.2, 0.5),
        "color": random.choice([(255, 0, 0), (0, 255, 0), (255, 255, 255)]),
        "life": 30
    })

# Update particles for cursor
def update_particles():
    for particle in particles[:]:
        particle["life"] -= 1
        if particle["life"] <= 0:
            particles.remove(particle)
        else:
            particle["radius"] += particle["growth"]
            alpha = int(255 * (particle["life"] / 30))
            color = (*particle["color"], alpha)
            pygame.draw.circle(screen, color, particle["pos"], int(particle["radius"]))

def main_menu():
    global current_state, game_mode  # Declare game_mode as global

    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)

        # Title (larger font size)
        title_font = pygame.font.Font("fonts/PixelifySans-Regular.ttf", 48)  # Larger font size
        title_text = title_font.render("Welcome to Sonny!", True, TEXT_COLOR)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))

        # Description (smaller font, yellow text)
        description_font = pygame.font.Font("fonts/PixelifySans-Regular.ttf", 18)  # Smaller font size
        description_text = description_font.render("Guess the songs and beat your best score!", True, (255, 223, 0))  # Yellow color
        screen.blit(description_text, (WIDTH // 2 - description_text.get_width() // 2, HEIGHT // 4 + 45))  # Position below the title

        # Define buttons for modes
        button_width = 250
        button_height = 50
        speed_run_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - 70, button_width, button_height)
        regular_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 10, button_width, button_height)
        github_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 90, button_width, button_height)  # GitHub button

        # Draw buttons
        draw_button(speed_run_button, "Speed Run")
        draw_button(regular_button, "Regular Mode")
        draw_button(github_button, "GitHub")  # GitHub button

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if speed_run_button.collidepoint(event.pos):
                    game_mode = "speed_run"  # Set game_mode to "speed_run"
                    current_state = GAME
                    running = False
                if regular_button.collidepoint(event.pos):
                    game_mode = "regular"  # Set game_mode to "regular"
                    current_state = GAME
                    running = False
                if github_button.collidepoint(event.pos):  # GitHub button logic
                    webbrowser.open("https://github.com/M0bula")  # Open GitHub link

        pygame.display.flip()
        clock.tick(FPS)


# Pause menu
def pause_menu():
    global current_state
    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
        pause_text = font.render("Game Paused", True, TEXT_COLOR)
        screen.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 4))

        resume_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50)
        quit_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
        draw_button(resume_button, "Resume")
        draw_button(quit_button, "Quit")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if resume_button.collidepoint(event.pos):
                    current_state = GAME
                    running = False
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    exit()

        pygame.display.flip()
        clock.tick(FPS)

def game():
    global current_state, total_score, game_mode, hint_count, hint_text  # Declare necessary global variables

    # Initialize variables
    total_score = 0
    question_count = 0
    attempts = 0
    hint_count = 0
    player_answer = ""
    current_song = get_random_song()
    feedback_text = ""
    hint_text = ""  # Ensure hint_text starts empty
    if game_mode == "speed_run":
        start_time = pygame.time.get_ticks()
        time_limit = 2 * 60 * 1000  # 2 minutes in milliseconds

    running = True
    while running:
        # **Render static background**
        screen.fill(BACKGROUND_COLOR)

        # Display lyrics
        render_wrapped_text(
            f"Lyrics: {current_song['lyrics']}",
            x=50,
            y=50,
            font=font,
            color=TEXT_COLOR,
            max_width=700
        )

        # Input box
        input_rect = pygame.Rect(50, HEIGHT - 100, 500, 40)
        draw_input_box_with_snow(input_rect, player_answer)

        # Display hint text above the input box
        if hint_text:
            hint_surface = font.render(hint_text, True, TEXT_COLOR)
            # screen.blit(hint_surface, (50, HEIG   HT - 230))  # Position just above the input box
            render_wrapped_text(hint_text, 50, HEIGHT - 230, font, TEXT_COLOR , 700)
        # Draw the hint button
        draw_pixelated_button(button_rect, "Hint")

        # Display timer for Speed Run mode
        if game_mode == "speed_run":
            elapsed_time = pygame.time.get_ticks() - start_time
            remaining_time = max(0, time_limit - elapsed_time)
            timer_surface = font.render(f"Time Left: {remaining_time // 1000}s", True, TEXT_COLOR)
            screen.blit(timer_surface, (50, HEIGHT - 270))
            if remaining_time == 0:
                feedback_text = f"Time's up! Final Score: {total_score}"
                current_state = "end_screen"
                running = False
        elif game_mode == "regular":
            question_surface = font.render(f"Question {question_count + 1}/10", True, TEXT_COLOR)
            screen.blit(question_surface, (WIDTH - 500, 13))  # Adjust position as needed
                # End the game after 10 questions
            if question_count >= 10:
                feedback_text = f"Game Over! Final Score: {total_score}"
                current_state = "end_screen"
                running = False
        # Display feedback below the hint text
        feedback_surface = font.render(feedback_text, True, TEXT_COLOR)
        # screen.blit(feedback_surface, (50, HEIGHT - 240))
        render_wrapped_text(feedback_text, 50, HEIGHT - 350, font, TEXT_COLOR , 700)
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    current_state = PAUSE_MENU
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    player_answer = player_answer[:-1]
                elif event.key == pygame.K_RETURN:
                    if player_answer.strip().lower() == current_song["name"].lower():
                        if attempts == 0:
                            total_score += 100 - (15 * hint_count)
                        elif attempts == 1:
                            total_score += 60 - (15 * hint_count)

                        feedback_text = "Correct! Moving to next song."
                        current_song = get_random_song()
                        question_count += 1
                        player_answer = ""
                        attempts = 0
                        hint_count = 0
                        hint_text = ""  # Reset hint text
                    else:
                        attempts += 1
                        if attempts == 2:
                            feedback_text = f"Wrong! The correct answer was: {current_song['name']}."

                            current_song = get_random_song()
                            question_count += 1
                            player_answer = ""
                            attempts = 0
                            hint_count = 0
                            hint_text = ""  # Reset hint text
                        else:
                            feedback_text = "Wrong! Try again."
                else:
                    player_answer += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):  # Hint button logic
                    if hint_count == 0:
                        play_hint_animation(screen, f"Artist: {current_song['artist']}", BACKGROUND_COLOR)
                        hint_text = f"Artist: {current_song['artist']}"  # Update hint text
                        hint_count += 1
                    elif hint_count == 1:
                        play_hint_animation(screen, f"Famous Line: {current_song['famous_line']}", BACKGROUND_COLOR)
                        hint_text = f"Famous Line: {current_song['famous_line']}"  # Update hint text
                        hint_count += 1


        # Update particles (if any)
        update_particles()

        # Refresh screen
        pygame.display.flip()
        clock.tick(FPS)

def draw_pixelated_button(rect, label_text):
    # Draw button background with Miku colors and Christmas style
    pygame.draw.rect(screen, (57, 197, 187), rect, border_radius=5)  # Base color
    pygame.draw.rect(screen, (0, 209, 206), rect, 3, border_radius=5)  # Border

    # Add a holiday-themed gift box in the center
    box_center_x = rect.centerx
    box_center_y = rect.centery
    gift_width, gift_height = 40, 40

    # Draw the gift box
    pygame.draw.rect(screen, (255, 0, 0), (box_center_x - gift_width // 2, box_center_y - gift_height // 2, gift_width, gift_height))  # Red box
    pygame.draw.rect(screen, (255, 255, 255), (box_center_x - gift_width // 2, box_center_y - 5, gift_width, 10))  # Horizontal ribbon
    pygame.draw.rect(screen, (255, 255, 255), (box_center_x - 5, box_center_y - gift_height // 2, 10, gift_height))  # Vertical ribbon

    # Add a bow
    pygame.draw.circle(screen, (255, 0, 0), (box_center_x - 10, box_center_y - gift_height // 2 - 5), 8)  # Left bow
    pygame.draw.circle(screen, (255, 0, 0), (box_center_x + 10, box_center_y - gift_height // 2 - 5), 8)  # Right bow

    # Add label below the button
    label = font.render(label_text, True, TEXT_COLOR)
    label_rect = label.get_rect(center=(box_center_x, rect.bottom + 20))
    screen.blit(label, label_rect)
    
# Snow particle system
snow_particles = []  # List to hold snow particles

def add_snow_particles(rect, num_particles=50):
    """Add snow particles on top of the input box."""
    for _ in range(num_particles):
        snow_particles.append({
            "x": rect.left + random.randint(0, rect.width),  # Random x position within the box
            "y": rect.top - 10,  # Start slightly above the box
            "speed": random.uniform(0.5, 1.5),  # Slower falling speed
            "size": random.randint(2, 5),  # Random particle size
            "lifetime": 100,  # Lifetime before fully disappearing
            "opacity": 255  # Initial opacity (fully visible)
        })

def update_snow_particles():
    """Update and draw snow particles with slow drop and melting effect."""
    for particle in snow_particles[:]:
        particle["y"] += particle["speed"]  # Move particle downward

        # Stop halfway down the input box and start fading (melting)
        if particle["y"] >= HEIGHT - 100 + 40:  # Halfway down the box
            particle["speed"] = 0  # Stop falling
            particle["opacity"] -= 5  # Gradually decrease opacity

        # Draw the particle with current opacity
        alpha_surface = pygame.Surface((particle["size"] * 2, particle["size"] * 2), pygame.SRCALPHA)
        pygame.draw.circle(alpha_surface, (255, 255, 255, particle["opacity"]), (particle["size"], particle["size"]), particle["size"])
        screen.blit(alpha_surface, (particle["x"] - particle["size"], particle["y"] - particle["size"]))

        # Remove particle if completely melted
        if particle["opacity"] <= 0:
            snow_particles.remove(particle)


def draw_input_box_with_snow(input_rect, player_answer):
    """Draw input box with collapsing snow effect."""
    # Draw the input box
    pygame.draw.rect(screen, (200, 200, 200), input_rect, border_radius=5)  # Grey box
    pygame.draw.rect(screen, (50, 50, 50), input_rect, 2, border_radius=5)  # Border

    # Render the text
    input_text_surface = font.render(player_answer, True, TEXT_COLOR)

    # Correct vertical alignment
    text_height = input_text_surface.get_height()
    vertical_offset = (input_rect.height - text_height) // 2
    screen.blit(input_text_surface, (input_rect.left + 10, input_rect.top + vertical_offset))

    # Add initial snow particles (only once)
    if not snow_particles:
        add_snow_particles(input_rect, num_particles=50)

    # Update and draw collapsing snow particles
    update_snow_particles()

# Main loop
while True:
    if current_state == START_MENU:
        main_menu()
    elif current_state == GAME:
        game()
    elif current_state == PAUSE_MENU:
        pause_menu()
    elif current_state == "end_screen":
        end_screen()