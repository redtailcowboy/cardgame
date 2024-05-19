import pygame
import random
import os

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CARD_WIDTH = 100
CARD_HEIGHT = 145
CARD_BACK = 'cards/cardBack_red3.png'
CARD_SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
CARD_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
DECK = [f'card{suit}{value}' for suit in CARD_SUITS for value in CARD_VALUES]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load card images
card_images = {card: pygame.transform.scale(pygame.image.load(os.path.join('cards', f'{card}.png')), (CARD_WIDTH, CARD_HEIGHT)) for card in DECK}
card_back_image = pygame.transform.scale(pygame.image.load(CARD_BACK), (CARD_WIDTH, CARD_HEIGHT))

# Game variables
dealer_hand = []
player_hand = []
deck = DECK.copy()
player_turn = True
game_over = False

# ... (rest of the code remains the same)

# Function to draw text
def draw_text(text, font_size, x, y, color=(255, 255, 255)):
    font = pygame.font.SysFont('Arial', font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Function to draw cards
def draw_cards(hand, x, y, is_dealer=False):
    for i, card in enumerate(hand):
        if is_dealer and i == 0 and player_turn:
            screen.blit(card_back_image, (x + i * (CARD_WIDTH + 5), y))
        else:
            screen.blit(card_images[card], (x + i * (CARD_WIDTH + 5), y))

# Main game loop
running = True
while running:
    # ... (event handling code remains the same)

    # Game logic
    if not player_hand:
        deal_card(player_hand)
        deal_card(dealer_hand)
        deal_card(player_hand)
        dealer_strategy()

    if not player_turn and not game_over:
        dealer_strategy()
        game_over = True  # End the game after the dealer's turn

    # Render game
    screen.fill((50, 150, 50))  # Green background for the table
    hit_button.draw(screen)
    stand_button.draw(screen)
    draw_cards(player_hand, 50, SCREEN_HEIGHT - CARD_HEIGHT - 100)
    draw_cards(dealer_hand, 50, 50, is_dealer=True)

    # Draw text
    draw_text(f'Player: {calculate_hand_value(player_hand)}', 30, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
    draw_text(f'Dealer: {calculate_hand_value(dealer_hand)}', 30, SCREEN_WIDTH // 2, 20)

    if game_over:
        player_score = calculate_hand_value(player_hand)
        dealer_score = calculate_hand_value(dealer_hand)
        if player_score > 21:
            draw_text('Player busts! Dealer wins!', 40, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        elif dealer_score > 21 or player_score > dealer_score:
            draw_text('Player wins!', 40, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        elif player_score < dealer_score:
            draw_text('Dealer wins!', 40, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        else:
            draw_text('Push!', 40, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
