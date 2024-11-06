import pygame
import random
import sys
import math

# Initialize pygame
pygame.init()

# Set up the display
width, height = 600, 600
window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Abstract Surreal Image Generator")

# Font settings
font = pygame.font.SysFont(None, 24)
large_font = pygame.font.SysFont(None, 32)


def draw_gradient(surface, width, height, direction='horizontal', start_color=(0, 0, 0), end_color=(255, 255, 255)):
    """
    Draws a gradient on the surface.
    """
    if direction == 'horizontal':
        for x in range(width):
            ratio = x / width
            r = int(start_color[0] * (1 - ratio) + end_color[0] * ratio)
            g = int(start_color[1] * (1 - ratio) + end_color[1] * ratio)
            b = int(start_color[2] * (1 - ratio) + end_color[2] * ratio)
            pygame.draw.line(surface, (r, g, b), (x, 0), (x, height))
    elif direction == 'vertical':
        for y in range(height):
            ratio = y / height
            r = int(start_color[0] * (1 - ratio) + end_color[0] * ratio)
            g = int(start_color[1] * (1 - ratio) + end_color[1] * ratio)
            b = int(start_color[2] * (1 - ratio) + end_color[2] * ratio)
            pygame.draw.line(surface, (r, g, b), (0, y), (width, y))


def draw_random_shape(surface, width, height):
    """
    Draws a random shape with random color, position, and transparency.
    """
    shape_type = random.choice(['rectangle', 'ellipse', 'line', 'polygon', 'arc'])
    color = tuple(random.randint(0, 255) for _ in range(3))
    x0 = random.randint(0, width)
    y0 = random.randint(0, height)
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)

    if shape_type == 'rectangle':
        rect = pygame.Rect(min(x0, x1), min(y0, y1), abs(x1 - x0), abs(y1 - y0))
        pygame.draw.rect(surface, color, rect)
    elif shape_type == 'ellipse':
        rect = pygame.Rect(min(x0, x1), min(y0, y1), abs(x1 - x0), abs(y1 - y0))
        pygame.draw.ellipse(surface, color, rect)
    elif shape_type == 'line':
        pygame.draw.line(surface, color, (x0, y0), (x1, y1), random.randint(1, 5))
    elif shape_type == 'polygon':
        num_points = random.randint(3, 6)
        points = [(random.randint(0, width), random.randint(0, height)) for _ in range(num_points)]
        pygame.draw.polygon(surface, color, points)
    elif shape_type == 'arc':
        rect = pygame.Rect(min(x0, x1), min(y0, y1), abs(x1 - x0), abs(y1 - y0))
        start_angle = random.uniform(0, math.pi * 2)
        end_angle = start_angle + random.uniform(math.pi / 2, math.pi * 2)
        pygame.draw.arc(surface, color, rect, start_angle, end_angle, random.randint(1, 5))


def generate_image(width, height):
    """
    Generates an abstract image by randomly selecting drawing functions.
    """
    image_surface = pygame.Surface((width, height))
    image_surface = image_surface.convert_alpha()

    # Draw a background gradient
    start_color = tuple(random.randint(0, 255) for _ in range(3))
    end_color = tuple(random.randint(0, 255) for _ in range(3))
    direction = random.choice(['horizontal', 'vertical'])
    draw_gradient(image_surface, width, height, direction=direction, start_color=start_color, end_color=end_color)

    # Randomly select drawing functions to execute
    num_drawings = random.randint(3, 5)  # Adjust the range as needed
    selected_functions = random.sample(list(keyword_draw_functions.values()), num_drawings)

    for draw_function in selected_functions:
        draw_function(image_surface, width, height)

    # Optionally, add some random shapes
    for _ in range(random.randint(5, 10)):
        draw_random_shape(image_surface, width, height)

    return image_surface


def draw_cat(surface, width, height):
    """
    Draws an abstract representation of a cat.
    """
    x = random.randint(50, width - 50)
    y = random.randint(50, height - 50)
    r = random.randint(30, 50)  # Radius of the face
    color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    # Draw face
    pygame.draw.circle(surface, color, (x, y), r)
    # Draw ears as triangles
    ear_points_left = [(x - r // 2, y - r // 2), (x - r, y - r), (x - r // 4, y - r // 2)]
    ear_points_right = [(x + r // 2, y - r // 2), (x + r, y - r), (x + r // 4, y - r // 2)]
    pygame.draw.polygon(surface, color, ear_points_left)
    pygame.draw.polygon(surface, color, ear_points_right)
    # Draw eyes
    eye_radius = r // 5
    pygame.draw.circle(surface, (0, 0, 0), (x - r // 3, y - r // 5), eye_radius)
    pygame.draw.circle(surface, (0, 0, 0), (x + r // 3, y - r // 5), eye_radius)
    # Draw nose
    nose_points = [(x, y), (x - r // 10, y + r // 5), (x + r // 10, y + r // 5)]
    pygame.draw.polygon(surface, (255, 182, 193), nose_points)  # Light pink nose


def draw_dog(surface, width, height):
    """
    Draws an abstract representation of a dog.
    """
    x = random.randint(50, width - 50)
    y = random.randint(50, height - 50)
    w = random.randint(60, 80)
    h = random.randint(80, 100)
    color = (random.randint(150, 200), random.randint(100, 150), random.randint(50, 100))
    # Draw face
    face_rect = pygame.Rect(x - w // 2, y - h // 2, w, h)
    pygame.draw.ellipse(surface, color, face_rect)
    # Draw ears
    ear_left = [(x - w // 2, y - h // 2), (x - w // 2 - 30, y - h // 2 - 40), (x - w // 2 + 10, y - h // 2)]
    ear_right = [(x + w // 2, y - h // 2), (x + w // 2 + 30, y - h // 2 - 40), (x + w // 2 - 10, y - h // 2)]
    pygame.draw.polygon(surface, color, ear_left)
    pygame.draw.polygon(surface, color, ear_right)
    # Draw eyes
    eye_radius = w // 10
    pygame.draw.circle(surface, (0, 0, 0), (x - w // 4, y - h // 6), eye_radius)
    pygame.draw.circle(surface, (0, 0, 0), (x + w // 4, y - h // 6), eye_radius)
    # Draw nose
    nose_rect = pygame.Rect(x - w // 20, y + h // 10, w // 10, h // 10)
    pygame.draw.ellipse(surface, (0, 0, 0), nose_rect)
    # Draw mouth
    pygame.draw.arc(surface, (0, 0, 0), (x - w // 4, y + h // 5, w // 2, h // 5), math.pi / 6, 5 * math.pi / 6, 2)


def draw_clouds(surface, width, height):
    """
    Draws abstract clouds.
    """
    for _ in range(random.randint(3, 5)):
        x = random.randint(0, width)
        y = random.randint(0, height // 2)
        for _ in range(random.randint(5, 7)):
            r = random.randint(20, 40)
            offset_x = random.randint(-50, 50)
            offset_y = random.randint(-20, 20)
            pygame.draw.circle(surface, (255, 255, 255), (x + offset_x, y + offset_y), r)


def draw_moon(surface, width, height):
    """
    Draws a more realistic moon.
    """
    x = random.randint(width // 4, 3 * width // 4)
    y = random.randint(height // 4, 3 * height // 4)
    r = random.randint(60, 100)
    pygame.draw.circle(surface, (220, 220, 220), (x, y), r)
    # Add craters
    for _ in range(random.randint(5, 15)):
        cr_r = random.randint(5, 15)
        cr_x = x + random.randint(-r + cr_r, r - cr_r)
        cr_y = y + random.randint(-r + cr_r, r - cr_r)
        pygame.draw.circle(surface, (180, 180, 180), (cr_x, cr_y), cr_r)
    # Add shading
    for i in range(r * 2):
        shade = int(50 * (i / (r * 2)))
        pygame.draw.line(surface, (0, 0, 0, shade), (x - r + i, y - r), (x - r + i, y + r))


def draw_chessboard(surface, width, height):
    """
    Draws a detailed chessboard.
    """
    board_size = min(width, height) - 200
    square_size = board_size // 8
    x0 = (width - board_size) // 2
    y0 = (height - board_size) // 2
    colors = [(240, 217, 181), (181, 136, 99)]
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            rect = pygame.Rect(x0 + col * square_size, y0 + row * square_size, square_size, square_size)
            pygame.draw.rect(surface, color, rect)
    # Optionally add pieces
    for _ in range(random.randint(2, 5)):
        piece_color = random.choice([(0, 0, 0), (255, 255, 255)])
        piece_row = random.randint(0, 7)
        piece_col = random.randint(0, 7)
        piece_x = x0 + piece_col * square_size + square_size // 2
        piece_y = y0 + piece_row * square_size + square_size // 2
        pygame.draw.circle(surface, piece_color, (piece_x, piece_y), square_size // 3)


def draw_robot(surface, width, height):
    """
    Draws an abstract robot.
    """
    x = random.randint(100, width - 100)
    y = random.randint(100, height - 100)
    w = random.randint(60, 80)
    h = random.randint(80, 120)
    color = (random.randint(100, 200), random.randint(100, 200), random.randint(100, 200))
    # Draw body
    body_rect = pygame.Rect(x - w // 2, y, w, h)
    pygame.draw.rect(surface, color, body_rect)
    # Draw head
    head_rect = pygame.Rect(x - w // 2, y - h // 2, w, h // 2)
    pygame.draw.rect(surface, color, head_rect)
    # Draw eyes
    eye_radius = w // 10
    pygame.draw.circle(surface, (0, 0, 0), (x - w // 4, y - h // 3), eye_radius)
    pygame.draw.circle(surface, (0, 0, 0), (x + w // 4, y - h // 3), eye_radius)
    # Draw mouth
    mouth_rect = pygame.Rect(x - w // 4, y - h // 4, w // 2, h // 20)
    pygame.draw.rect(surface, (0, 0, 0), mouth_rect)
    # Draw arms
    pygame.draw.line(surface, color, (x - w // 2, y + h // 4), (x - w, y + h // 2), 5)
    pygame.draw.line(surface, color, (x + w // 2, y + h // 4), (x + w, y + h // 2), 5)
    # Draw antenna
    pygame.draw.line(surface, (0, 0, 0), (x, y - h // 2), (x, y - h // 2 - 30), 2)
    pygame.draw.circle(surface, (255, 0, 0), (x, y - h // 2 - 30), 5)


def draw_fish(surface, width, height):
    """
    Draws an abstract fish.
    """
    x = random.randint(50, width - 150)
    y = random.randint(50, height - 50)
    fish_length = random.randint(80, 120)
    fish_height = fish_length // 2
    body_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # Draw body
    body_points = [
        (x, y),
        (x + fish_length // 2, y - fish_height // 2),
        (x + fish_length, y),
        (x + fish_length // 2, y + fish_height // 2)
    ]
    pygame.draw.polygon(surface, body_color, body_points)
    # Draw tail
    tail_points = [
        (x + fish_length, y),
        (x + fish_length + fish_length // 4, y - fish_height // 2),
        (x + fish_length + fish_length // 4, y + fish_height // 2)
    ]
    pygame.draw.polygon(surface, body_color, tail_points)
    # Draw eye
    pygame.draw.circle(surface, (0, 0, 0), (x + 20, y), 5)


def draw_bicycle(surface, width, height):
    """
    Draws an abstract bicycle.
    """
    x = random.randint(50, width - 150)
    y = random.randint(height // 2, height - 50)
    wheel_radius = 30
    frame_color = (0, 0, 0)
    # Draw wheels
    pygame.draw.circle(surface, frame_color, (x, y), wheel_radius, 4)
    pygame.draw.circle(surface, frame_color, (x + 100, y), wheel_radius, 4)
    # Draw frame
    pygame.draw.line(surface, frame_color, (x, y), (x + 50, y - 50), 4)
    pygame.draw.line(surface, frame_color, (x + 50, y - 50), (x + 100, y), 4)
    pygame.draw.line(surface, frame_color, (x + 50, y - 50), (x + 50, y - 80), 4)
    pygame.draw.line(surface, frame_color, (x + 50, y - 80), (x + 30, y - 90), 4)
    pygame.draw.line(surface, frame_color, (x + 50, y - 50), (x + 20, y), 4)
    # Draw handlebars
    pygame.draw.line(surface, frame_color, (x + 50, y - 80), (x + 80, y - 100), 4)
    pygame.draw.line(surface, frame_color, (x + 80, y - 100), (x + 90, y - 90), 4)


# Mapping of keywords to drawing functions
keyword_draw_functions = {
    'cat': draw_cat,
    'dog': draw_dog,
    'clouds': draw_clouds,
    'moon': draw_moon,
    'chess': draw_chessboard,
    'robot': draw_robot,
    'fish': draw_fish,
    'bicycle': draw_bicycle,
    # Add more mappings as needed
}


def draw_text(surface, text, position, font, color=(0, 0, 0)):
    """
    Renders text onto the surface.
    """
    text_lines = []
    words = text.split(' ')
    line = ''
    for word in words:
        if font.size(line + word)[0] < surface.get_width() - 100:
            line += word + ' '
        else:
            text_lines.append(line)
            line = word + ' '
    text_lines.append(line)
    y_offset = position[1]
    for line in text_lines:
        text_obj = font.render(line, True, color)
        surface.blit(text_obj, (position[0], y_offset))
        y_offset += text_obj.get_height()


def recalculate_layout(window_width, window_height):
    """
    Recalculates the positions and sizes of GUI elements based on the window size.
    """
    # Input box dimensions
    input_rect = pygame.Rect(50, 50, window_width - 100, 32)
    # Positions for text and buttons
    prompt_message_pos = (50, 20)
    error_message_pos = (50, 90)
    image_surface_pos = (0, 130)
    generate_button_rect = pygame.Rect(50, window_height - 70, 250, 50)
    return input_rect, prompt_message_pos, error_message_pos, image_surface_pos, generate_button_rect


def main():
    global width, height, window  # Declare 'window' as global
    # Variables for the prompt input
    prompt = ''
    input_active = True
    prompt_message = 'tell me your secrets:'
    error_message = ''
    image_surface = None

    # Cursor variables
    cursor_visible = True  # Cursor is visible when the input box is active
    cursor_timer = 0  # Timer to manage blinking
    cursor_blink_rate = 500  # Cursor blink rate in milliseconds

    # Initialize clock
    clock = pygame.time.Clock()

    # Initial GUI layout calculations
    input_rect, prompt_message_pos, error_message_pos, image_surface_pos, generate_button = recalculate_layout(width,
                                                                                                               height)

    # Main loop
    running = True
    while running:
        dt = clock.tick()
        window.fill((255, 255, 255))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                # Update the window size
                width, height = event.w, event.h
                window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                # Recalculate GUI layout
                input_rect, prompt_message_pos, error_message_pos, image_surface_pos, generate_button = recalculate_layout(
                    width, height)
                # Resize image surface if needed
                if image_surface:
                    image_surface = pygame.transform.scale(image_surface, (width, height - 200))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    input_active = True
                else:
                    input_active = False
                # Check if the Generate button is clicked
                if generate_button.collidepoint(event.pos):
                    if prompt.strip():
                        # Process the prompt
                        error_message = ''
                        image_surface = generate_image(width, height - 200)
                    else:
                        error_message = 'Please enter a prompt.'
                        image_surface = None
            elif event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        if prompt.strip():
                            # Process the prompt
                            error_message = ''
                            image_surface = generate_image(width, height - 200)
                        else:
                            error_message = 'Please enter a prompt.'
                            image_surface = None
                        prompt = ''
                    elif event.key == pygame.K_BACKSPACE:
                        prompt = prompt[:-1]
                    else:
                        prompt += event.unicode

        # Update cursor blinking
        if input_active:
            cursor_timer += dt
            if cursor_timer >= cursor_blink_rate:
                cursor_timer = 1
                cursor_visible = not cursor_visible
        else:
            cursor_visible = True

        # Draw the input box
        color_active = pygame.Color('lightskyblue3')
        color_inactive = pygame.Color('gray15')
        color = color_active if input_active else color_inactive
        pygame.draw.rect(window, color, input_rect, 2)

        # Render the current prompt text
        txt_surface = font.render(prompt, True, (0, 0, 0))
        window.blit(txt_surface, (input_rect.x + 5, input_rect.y + 5))

        # Draw the cursor
        if cursor_visible and input_active:
            cursor_x = input_rect.x + 5 + txt_surface.get_width()
            cursor_y = input_rect.y + 5
            cursor_height = txt_surface.get_height()
            pygame.draw.line(window, (0, 0, 0), (cursor_x, cursor_y), (cursor_x, cursor_y + cursor_height))

        # Draw the prompt message
        draw_text(window, prompt_message, prompt_message_pos, large_font)

        # Draw error message if any
        if error_message:
            draw_text(window, error_message, error_message_pos, font, color=(255, 0, 0))

        # Draw the generated image
        if image_surface:
            window.blit(image_surface, image_surface_pos)

        # Draw the Generate button
        pygame.draw.rect(window, (70, 130, 180), generate_button)
        draw_text(window, 'do your worst', (generate_button.x + 10, generate_button.y + 15), font,
                  color=(255, 255, 255))

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
