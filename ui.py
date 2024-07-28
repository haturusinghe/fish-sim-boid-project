import pygame
import pygame_gui
from settings import *

def create_ui(manager):
    ui_panel = pygame_gui.elements.UIPanel(
        relative_rect=pygame.Rect((50, 50), (300, 600)),  # Adjusted height to accommodate new inputs
        manager=manager
    )

    # Add labels for each parameter
    separation_input_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 10), (200, 30)),
        text='Separation Factor:',
        manager=manager,
        container=ui_panel
    )

    alignment_input_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 50), (200, 30)),
        text='Alignment Factor:',
        manager=manager,
        container=ui_panel
    )

    cohesion_input_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 90), (200, 30)),
        text='Cohesion Factor:',
        manager=manager,
        container=ui_panel
    )

    neighbor_radius_input_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 130), (200, 30)),
        text='Neighbor Radius:',
        manager=manager,
        container=ui_panel
    )

    # New input labels
    avoid_obstacle_input_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 170), (200, 30)),
        text='Avoid Obstacle Factor:',
        manager=manager,
        container=ui_panel
    )

    avoid_predator_input_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 210), (200, 30)),
        text='Avoid Predator Factor:',
        manager=manager,
        container=ui_panel
    )

    max_speed_input_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 250), (200, 30)),
        text='Max Speed:',
        manager=manager,
        container=ui_panel
    )

    max_force_input_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 290), (200, 30)),
        text='Max Force:',
        manager=manager,
        container=ui_panel
    )

    # Add text input elements for parameters
    separation_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((200, 10), (50, 30)),  # Adjusted width
        manager=manager,
        container=ui_panel
    )
    separation_input.set_text("1.5")

    alignment_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((200, 50), (50, 30)),  # Adjusted width
        manager=manager,
        container=ui_panel
    )
    alignment_input.set_text("1.0")

    cohesion_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((200, 90), (50, 30)),  # Adjusted width
        manager=manager,
        container=ui_panel
    )
    cohesion_input.set_text("1.0")

    neighbor_radius_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((200, 130), (50, 30)),  # Adjusted width
        manager=manager,
        container=ui_panel
    )
    neighbor_radius_input.set_text("50")

    # New text inputs
    avoid_obstacle_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((200, 170), (50, 30)),  # Adjusted width
        manager=manager,
        container=ui_panel
    )
    avoid_obstacle_input.set_text("2.0")

    avoid_predator_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((200, 210), (50, 30)),  # Adjusted width
        manager=manager,
        container=ui_panel
    )
    avoid_predator_input.set_text("3.0")

    max_speed_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((200, 250), (50, 30)),  # Adjusted width
        manager=manager,
        container=ui_panel
    )
    max_speed_input.set_text("4.0")

    max_force_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((200, 290), (50, 30)),  # Adjusted width
        manager=manager,
        container=ui_panel
    )
    max_force_input.set_text("0.1")

    # Adjust positions of the existing buttons
    update_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((10, 330), (280, 40)),
        text='Update',
        manager=manager,
        container=ui_panel
    )

    separation_toggle_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((10, 380), (280, 30)),
        text="Enable Separation",
        manager=manager,
        container=ui_panel
    )

    alignment_toggle_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((10, 420), (280, 30)),
        text="Enable Alignment",
        manager=manager,
        container=ui_panel
    )

    cohesion_toggle_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((10, 460), (280, 30)),
        text="Enable Cohesion",
        manager=manager,
        container=ui_panel
    )

    remove_boids_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((10, 500), (130, 50)),
        text='Remove Boids',
        manager=manager,
        container=ui_panel
    )

    remove_obstacles_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((160, 500), (130, 50)),
        text='Remove Obstacles',
        manager=manager,
        container=ui_panel
    )

    return ui_panel, separation_input, alignment_input, cohesion_input, neighbor_radius_input, avoid_obstacle_input, avoid_predator_input, max_speed_input, max_force_input, separation_toggle_button, alignment_toggle_button, cohesion_toggle_button, remove_boids_button, remove_obstacles_button, update_button, separation_input_label, alignment_input_label, cohesion_input_label, neighbor_radius_input_label, avoid_obstacle_input_label, avoid_predator_input_label, max_speed_input_label, max_force_input_label
