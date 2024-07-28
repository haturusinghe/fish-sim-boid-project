import pygame
import sys
import pygame_gui
from settings import *
from boid import Boid
from predator import Predator
from obstacle import Obstacle
from ui import create_ui

# Initialize Pygame
pygame.init()

# Create Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fish Schooling Simulation")

# Initialize pygame_gui
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

# Create UI elements
ui_panel, separation_input, alignment_input, cohesion_input, neighbor_radius_input, avoid_obstacle_input, avoid_predator_input, max_speed_input, max_force_input, separation_toggle_button, alignment_toggle_button, cohesion_toggle_button, remove_boids_button, remove_obstacles_button, update_button, separation_input_label, alignment_input_label, cohesion_input_label, neighbor_radius_input_label, avoid_obstacle_input_label, avoid_predator_input_label, max_speed_input_label, max_force_input_label = create_ui(manager)

# Initialize boids and obstacles
boids = []
obstacles = []
predators = []

# Toggle UI visibility
ui_visible = True

# Manage toggle states
separation_enabled = True
alignment_enabled = True
cohesion_enabled = True

def show_instructions(screen):
    font = pygame.font.SysFont(None, 36)
    instructions = [
        "Welcome to the Fish Schooling Simulation by CS/2018/015",
        "",
        "",
        "Left Click: Add a new Fish",
        "Right Click: Add an obstacle",
        "Middle Click: Add a Predator",
        "Press Tab to toggle Settings Overlay",
        "",
        "",
        "Press any key to start the simulation"
    ]
    screen.fill(BACKGROUND_COLOR)

    y = HEIGHT // 2 - len(instructions) * 20
    for line in instructions:
        text = font.render(line, True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, y))
        screen.blit(text, text_rect)
        y += 40

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

def main():
    show_instructions(screen)

    global ui_visible, separation_enabled, alignment_enabled, cohesion_enabled
    clock = pygame.time.Clock()

    running = True
    while running:
        time_delta = clock.tick(30) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    ui_visible = not ui_visible
                    ui_panel.visible = ui_visible
                    separation_input.visible = ui_visible
                    alignment_input.visible = ui_visible
                    cohesion_input.visible = ui_visible
                    neighbor_radius_input.visible = ui_visible
                    separation_toggle_button.visible = ui_visible
                    alignment_toggle_button.visible = ui_visible
                    cohesion_toggle_button.visible = ui_visible
                    remove_boids_button.visible = ui_visible
                    remove_obstacles_button.visible = ui_visible
                    update_button.visible = ui_visible
                    separation_input_label.visible = ui_visible
                    alignment_input_label.visible = ui_visible
                    cohesion_input_label.visible = ui_visible
                    # New
                    neighbor_radius_input_label.visible = ui_visible
                    neighbor_radius_input.visible = ui_visible
                    avoid_obstacle_input_label.visible = ui_visible
                    avoid_obstacle_input.visible = ui_visible
                    avoid_predator_input_label.visible = ui_visible
                    avoid_predator_input.visible = ui_visible
                    max_speed_input_label.visible = ui_visible
                    max_speed_input.visible = ui_visible
                    max_force_input_label.visible = ui_visible
                    max_force_input.visible = ui_visible


            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    x, y = event.pos
                    boids.append(Boid(x, y))
                elif event.button == 3:  # Right click
                    x, y = event.pos
                    obstacles.append(Obstacle(x, y))
                elif event.button == 2:  # Middle click to add a predator
                    x, y = pygame.mouse.get_pos()
                    predators.append(Predator(x, y))
                
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == remove_boids_button:
                    boids.clear()
                    predators.clear()
                elif event.ui_element == remove_obstacles_button:
                    obstacles.clear()
                elif event.ui_element == update_button:
                    try:
                        sep_factor = float(separation_input.get_text())
                        align_factor = float(alignment_input.get_text())
                        coh_factor = float(cohesion_input.get_text())
                        neighbor_radius = float(neighbor_radius_input.get_text())

                        Boid.SEPARATION_FACTOR = sep_factor
                        Boid.ALIGNMENT_FACTOR = align_factor
                        Boid.COHESION_FACTOR = coh_factor
                        Boid.NEIGHBOR_RADIUS = neighbor_radius
                    except ValueError:
                        pass
                elif event.ui_element == separation_toggle_button:
                    separation_enabled = not separation_enabled
                    Boid.separation_enabled = separation_enabled
                    separation_toggle_button.set_text(f"Enable Separation: {'On' if separation_enabled else 'Off'}")
                elif event.ui_element == alignment_toggle_button:
                    alignment_enabled = not alignment_enabled
                    Boid.alignment_enabled = alignment_enabled
                    alignment_toggle_button.set_text(f"Enable Alignment: {'On' if alignment_enabled else 'Off'}")
                elif event.ui_element == cohesion_toggle_button:
                    cohesion_enabled = not cohesion_enabled
                    Boid.cohesion_enabled = cohesion_enabled
                    cohesion_toggle_button.set_text(f"Enable Cohesion: {'On' if cohesion_enabled else 'Off'}")

            manager.process_events(event)

        manager.update(time_delta)

        screen.fill(BACKGROUND_COLOR)

        for boid in boids:
            boid.update(boids, obstacles, predators)
            boid.draw(screen)

        for obstacle in obstacles:
            obstacle.draw(screen)
        
        for predator in predators:
            predator.update(boids, obstacles)
            predator.draw(screen)

        manager.draw_ui(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
