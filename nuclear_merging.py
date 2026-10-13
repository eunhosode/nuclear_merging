import pygame
import sys
import random
import math
import time

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("nuclear_merging")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
GRAY = (220, 220, 220)
DARK_GRAY = (80, 80, 80)
FOG_GRAY = (180, 180, 180)

element_names = {
    1: "H",
    2: "He",
    3: "Li",
    4: "Be",
    5: "B",
    6: "C",
    7: "N",
    8: "O",
    9: "F",
    10: "Ne",
    11: "Na",
    12: "Mg",
    13: "Al",
    14: "Si",
    15: "P",
    16: "S",
    17: "Cl",
    18: "Ar",
    19: "K",
    20: "Ca",
    21: "Sc",
    22: "Ti",
    23: "V",
    24: "Cr",
    25: "Mn",
    26: "Fe",
    27: "Co",
    28: "Ni",
    29: "Cu",
    30: "Zn",
    31: "Ga",
    32: "Ge",
    33: "As",
    34: "Se",
    35: "Br",
    36: "Kr",
    37: "Rb",
    38: "Sr",
    39: "Y",
    40: "Zr",
    41: "Nb",
    42: "Mo",
    43: "Tc",
    44: "Ru",
    45: "Rh",
    46: "Pd",
    47: "Ag",
    48: "Cd",
    49: "In",
    50: "Sn",
    51: "Sb",
    52: "Te",
    53: "I",
    54: "Xe",
    55: "Cs",
    56: "Ba",
    57: "La",
    58: "Ce",
    59: "Pr",
    60: "Nd",
    61: "Pm",
    62: "Sm",
    63: "Eu",
    64: "Gd",
    65: "Tb",
    66: "Dy",
    67: "Ho",
    68: "Er",
    69: "Tm",
    70: "Yb",
    71: "Lu",
    72: "Hf",
    73: "Ta",
    74: "W",
    75: "Re",
    76: "Os",
    77: "Ir",
    78: "Pt",
    79: "Au",
    80: "Hg",
    81: "Tl",
    82: "Pb",
    83: "Bi",
    84: "Po",
    85: "At",
    86: "Rn",
    87: "Fr",
    88: "Ra",
    89: "Ac",
    90: "Th",
    91: "Pa",
    92: "U",
    93: "Np",
    94: "Pu",
    95: "Am",
    96: "Cm",
    97: "Bk",
    98: "Cf",
    99: "Es",
    100: "Fm",
    101: "Md",
    102: "No",
    103: "Lr",
    104: "Rf",
    105: "Db",
    106: "Sg",
    107: "Bh",
    108: "Hs",
    109: "Mt",
    110: "Ds",
    111: "Rg",
    112: "Cn",
    113: "Nh",
    114: "Fl",
    115: "Mc",
    116: "Lv",
    117: "Ts",
    118: "Og",
}

baseline_isotopes = {
    (1, 1), (1, 2),
    (2, 3), (2, 4),
    (3, 6), (3, 7),
    (4, 9),
    (5, 10), (5, 11),
    (6, 12), (6, 13),
    (7, 14), (7, 15),
    (8, 16), (8, 17), (8, 18),
    (9, 19),
    (10, 20), (10, 21), (10, 22),
    (11, 23),
    (12, 24), (12, 25), (12, 26),
    (13, 27),
    (14, 28), (14, 29), (14, 30),
    (15, 31),
    (16, 32), (16, 33), (16, 34), (16, 36),
    (17, 35), (17, 37),
    (18, 36), (18, 38), (18, 40),
    (19, 39), (19, 41),
    (20, 40), (20, 42), (20, 43), (20, 44), (20, 46),
    (21, 45),
    (22, 46), (22, 47), (22, 48), (22, 49), (22, 50),
    (23, 51),
    (24, 50), (24, 52), (24, 53), (24, 54),
    (25, 55),
    (26, 54), (26, 56), (26, 57), (26, 58),
    (27, 59),
    (28, 58), (28, 60), (28, 61), (28, 62), (28, 64),
    (29, 63), (29, 65),
    (30, 64), (30, 66), (30, 67), (30, 68), (30, 70),
    (31, 69), (31, 71),
    (32, 70), (32, 72), (32, 73), (32, 74), (32, 76),
    (33, 75),
    (34, 74), (34, 76), (34, 77), (34, 78), (34, 80), (34, 82),
    (35, 79), (35, 81),
    (36, 78), (36, 80), (36, 82), (36, 83), (36, 84), (36, 86),
    (37, 85),
    (38, 84), (38, 86), (38, 87), (38, 88),
    (39, 89),
    (40, 90), (40, 91), (40, 92), (40, 94), (40, 96),
    (41, 93),
    (42, 92), (42, 94), (42, 95), (42, 96), (42, 97), (42, 98), (42, 100),
    (44, 96), (44, 98), (44, 99), (44, 100), (44, 101), (44, 102), (44, 104),
    (45, 103),
    (46, 102), (46, 104), (46, 105), (46, 106), (46, 107), (46, 108), (46, 110),
    (47, 107), (47, 109),
    (48, 106), (48, 108), (48, 110), (48, 111), (48, 112), (48, 114), (48, 116),
    (49, 113),
    (50, 112), (50, 114), (50, 115), (50, 116), (50, 117), (50, 118), (50, 120), (50, 122), (50, 124),
    (51, 121), (51, 123),
    (52, 120), (52, 122), (52, 124), (52, 125), (52, 126), (52, 128), (52, 130),
    (53, 127),
    (54, 124), (54, 126), (54, 128), (54, 129), (54, 130), (54, 131), (54, 132), (54, 134), (54, 136),
    (55, 133),
    (56, 130), (56, 132), (56, 134), (56, 135), (56, 136), (56, 137), (56, 138),
    (57, 139),
    (58, 136), (58, 138), (58, 140),
    (59, 141),
    (60, 142), (60, 143), (60, 145), (60, 146), (60, 148), (60, 150),
    (62, 144), (62, 150), (62, 152), (62, 154),
    (63, 151), (63, 153),
    (64, 154), (64, 155), (64, 156), (64, 157), (64, 158), (64, 160),
    (65, 159),
    (66, 158), (66, 160), (66, 161), (66, 162), (66, 163), (66, 164),
    (67, 165),
    (68, 162), (68, 164), (68, 166), (68, 167), (68, 168), (68, 170),
    (69, 169),
    (70, 168), (70, 170), (70, 171), (70, 172), (70, 173), (70, 174), (70, 176),
    (71, 175),
    (72, 176), (72, 177), (72, 178), (72, 179), (72, 180),
    (73, 181),
    (74, 180), (74, 182), (74, 183), (74, 184), (74, 186),
    (75, 185),
    (76, 184), (76, 187), (76, 188), (76, 189), (76, 190), (76, 192),
    (77, 191), (77, 193),
    (78, 192), (78, 194), (78, 195), (78, 196), (78, 198),
    (79, 197),
    (80, 196), (80, 198), (80, 199), (80, 200), (80, 201), (80, 202), (80, 204),
    (81, 203), (81, 205),
    (82, 206), (82, 207), (82, 208),
    
}

isotope_decay_levels = {
    **{isotope: 0 for isotope in baseline_isotopes},

    (1, 3): 1,
    (4, 10): 1,
    (6, 14): 1,
    (19, 40): 1,
    (20, 48): 1,
    (22, 50): 1,
    (37, 87): 1,
    (52, 123): 1,
    (57, 138): 1,
    (58, 142): 1,
    (60, 144): 1,
    (62, 147): 1,
    (62, 148): 1,
    (62, 149): 1,
    (64, 152): 1,
    (66, 156): 1,
    (71, 176): 1,
    (72, 174): 1,
    (73, 180): 1,
    (75, 187): 1,
    (76, 186): 1,
    (78, 190): 1,
    (82, 204): 1,
    (83, 209): 1,
    (85, 215): 1,
    (90, 232): 1,
    (91, 231): 1,
    (91, 234): 1,
    (92, 234): 1,
    (92, 235): 1,
    (92, 238): 1,

    (13, 26): 2,
    (17, 36): 2,
    (18, 39): 2,
    (18, 42): 2,
    (20, 41): 2,
    (25, 53): 2,
    (26, 60): 2,
    (28, 59): 2,
    (34, 79): 2,
    (36, 81): 2,
    (40, 93): 2,
    (41, 91): 2,
    (41, 92): 2,
    (41, 94): 2,
    (43, 97): 2,
    (43, 98): 2,
    (43, 99): 2,
    (46, 107): 2,
    (48, 113): 2,
    (49, 115): 2,
    (50, 126): 2,
    (53, 129): 2,
    (55, 135): 2,
    (57, 137): 2,
    (62, 146): 2,
    (64, 150): 2,
    (66, 154): 2,
    (72, 182): 2,
    (82, 202): 2,
    (82, 205): 2,
    (90, 230): 2,
    (92, 233): 2,
    (92, 236): 2,
    (93, 236): 2,
    (93, 237): 2,
    (94, 239): 2,
    (94, 242): 2,
    (94, 244): 2,
    (96, 247): 2,
    (96, 248): 2,

    (14, 32): 3,
    (18, 39): 3,
    (18, 42): 3,
    (22, 44): 3,
    (28, 63): 3,
    (36, 85): 3,
    (38, 90): 3,
    (42, 93): 3,
    (55, 137): 3,
    (56, 133): 3,
    (61, 145): 3,
    (62, 151): 3,
    (63, 152): 3,
    (64, 148): 3,
    (65, 157): 3,
    (66, 158): 3,
    (67, 163): 3,
    (78, 193): 3,
    (80, 194): 3,
    (82, 210): 3,
    (83, 207): 3,
    (84, 209): 3,
    (88, 226): 3,
    (89, 227): 3,
    (90, 229): 3,
    (92, 232): 3,
    (94, 238): 3,
    (94, 240): 3,
    (94, 241): 3,
    (95, 241): 3,
    (95, 243): 3,
    (96, 243): 3,
    (96, 244): 3,
    (96, 245): 3,
    (96, 246): 3,
    (96, 250): 3,
    (97, 247): 3,
    (98, 249): 3,
    (98, 250): 3,
    (98, 251): 3,

    (11, 22): 4,
    (20, 45): 4,
    (23, 49): 4,
    (25, 54): 4,
    (26, 55): 4,
    (27, 57): 4,
    (30, 65): 4,
    (32, 68): 4,
    (34, 75): 4,
    (39, 88): 4,
    (44, 106): 4,
    (45, 101): 4,
    (45, 102): 4,
    (48, 109): 4,
    (50, 113): 4,
    (50, 123): 4,
    (51, 125): 4,
    (55, 134): 4,
    (58, 139): 4,
    (58, 144): 4,
    (61, 143): 4,
    (61, 144): 4,
    (61, 146): 4,
    (61, 147): 4,
    (62, 145): 4,
    (63, 154): 4,
    (63, 155): 4,
    (64, 151): 4,
    (64, 153): 4,
    (66, 159): 4,
    (69, 170): 4,
    (69, 171): 4,
    (71, 173): 4,
    (71, 174): 4,
    (72, 172): 4,
    (73, 179): 4,
    (73, 182): 4,
    (74, 181): 4,
    (76, 194): 4,
    (79, 195): 4,
    (81, 204): 4,
    (84, 208): 4,
    (84, 210): 4,
    (88, 228): 4,
    (90, 228): 4,
    (93, 235): 4,
    (94, 236): 4,
    (96, 242): 4,
    (97, 248): 4,
    (97, 249): 4,
    (98, 248): 4,
    (98, 252): 4,
    (99, 252): 4,
    (99, 254): 4,
    (100, 257): 4,

}

decay_chances = {
    0: 0.00,
    1: 0.05,
    2: 0.10,
    3: 0.15,
    4: 0.20,
    5: 0.40,
}

atomic_radius_rules = [
    (1, 2, 20, 4),
    (3, 10, 30, 1.5),
    (11, 18, 36, 1.7),
    (19, 36 , 42, 1.2),
]


def get_atomic_radius(protons):
    for period_start, period_end, largest_radius, shrink_per_element in atomic_radius_rules:
        if period_start <= protons <= period_end:
            position = protons - period_start
            return round(largest_radius - position * shrink_per_element)
    return 18


def get_photon_count(protons):
    if protons <= 2:
        return 3
    if protons <= 10:
        return 4
    if protons <= 18:
        return 5
    return 6


def create_player():
    return {
        'x': width // 2,
        'y': height - 60,
        'radius': get_atomic_radius(1),
        'protons': 1,
        'neutrons': 0
    }


def get_isotope_label(protons, neutrons):
    mass_number = protons + neutrons
    name = element_names.get(protons, f"Element-{protons}")
    return f"{name}-{mass_number}"


def get_time_label(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes}min {remaining_seconds}sec"


levels = {
    'Easy': {
        'weights': [30, 60, 0],
        'particle_speed': 3,
        'neutron_decay': 'vanish',
    },
    'Normal': {
        'weights': [30, 60, 10],
        'particle_speed': 3,
        'photon_speed': 6,
        'neutron_decay': 'vanish',
    },
    'Hard': {
        'weights': [30, 60, 10],
        'particle_speed': 3,
        'photon_speed': 9,
        'neutron_decay': 'vanish',
    },
    'Speedy': {
        'weights': [30, 60, 5],
        'particle_speed': 6,
        'photon_speed': 12,
        'neutron_decay': 'vanish',
    },
    'Is it snail?': {
        'weights': [30, 60, 10],
        'particle_speed': 1,
        'photon_speed': 18,
        'neutron_decay': 'vanish',
    },
    'Choking': {
        'weights': [30, 60, 90],
        'particle_speed': 3,
        'photon_speed': 1,
        'neutron_decay': 'vanish',
    },
    'Miserable': {
        'weights': [30, 60, 90],
        'particle_speed': 3,
        'photon_speed': 9,
        'neutron_decay': 'vanish',
    },
    'Schrödinger\'s particle': {
        'weights': [50, 50, 0],
        'particle_speed': 3,
        'photon_speed': 12,
        'neutron_decay': 'photon',
        'neutron_decay_chance': 0.75,
        'proton_decay': 'photon',
        'proton_decay_chance': 0.75,
    },
    'Midgley\'s Gas': {
        'weights': [30, 60, 90],
        'particle_speed': 3,
        'photon_speed': 18,
        'neutron_decay': 'photon',
        'neutron_decay_chance': 0.75,
        'proton_decay': 'photon',
        'proton_decay_chance': 0.75,
    },
    'Permian': {
        'weights': [1, 1, 1],
        'particle_speed': 18,
        'photon_speed': 18,
        'neutron_decay': 'photon',
        'neutron_decay_chance': 0.9,
        'proton_decay': 'photon',
        'proton_decay_chance': 0.9,
    },
    'Fog': {
        'weights': [30, 60, 10],
        'particle_speed': 3,
        'photon_speed': 6,
        'neutron_decay': 'vanish',
        'fog': True,
    },
    'Paralysis': {
        'weights': [30, 60, 10],
        'particle_speed': 3,
        'photon_speed': 6,
        'neutron_decay': 'vanish',
        'paralysis': True,
        'paralysis_interval': 10000,
        'paralysis_duration': 3000,
        'paralysis_chance': 0.5,
    }
}


player = create_player()

particles = []

font = pygame.font.SysFont(None, 30)
title_font = pygame.font.SysFont(None, 56)

level_buttons = []
button_width = 180
button_height = 54
button_gap = 12
button_columns = 3
button_start_x = width // 2 - (button_columns * button_width + (button_columns - 1) * button_gap) // 2
button_rows = math.ceil(len(levels) / button_columns)
button_start_y = height // 2 - (button_rows * button_height + (button_rows - 1) * button_gap) // 2
for index, level_name in enumerate(levels):
    button_x = button_start_x + (index % button_columns) * (button_width + button_gap)
    button_y = button_start_y + (index // button_columns) * (button_height + button_gap)
    level_buttons.append((level_name, pygame.Rect(button_x, button_y, button_width, button_height)))

restart_button = pygame.Rect(width // 2 - button_width - button_gap // 2, height // 2 + 120, button_width, button_height)
other_mode_button = pygame.Rect(width // 2 + button_gap // 2, height // 2 + 120, button_width, button_height)

clock = pygame.time.Clock()
running = True
game_over = False
game_state = 'menu'
selected_level = None
selected_level_name = ""
game_over_started_at = 0
game_over_menu_started_at = 0
game_over_isotope = ""
game_started_at = 0
game_over_elapsed_seconds = 0
next_paralysis_check_at = 0
paralysis_until = 0

PARTICLE_INTERVAL = 25
frame_count = 0

while running:
    clock.tick(60)
    frame_count += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif game_state == 'menu' and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for level_name, button_rect in level_buttons:
                if button_rect.collidepoint(event.pos):
                    selected_level = levels[level_name]
                    selected_level_name = level_name
                    player = create_player()
                    particles = []
                    frame_count = 0
                    game_over = False
                    game_over_isotope = ""
                    game_started_at = time.time()
                    game_over_elapsed_seconds = 0
                    next_paralysis_check_at = pygame.time.get_ticks() + selected_level.get('paralysis_interval', 10000)
                    paralysis_until = 0
                    game_state = 'playing'
        elif game_state == 'game_over_menu' and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if restart_button.collidepoint(event.pos):
                selected_level = levels[selected_level_name]
                player = create_player()
                particles = []
                frame_count = 0
                game_over = False
                game_over_isotope = ""
                game_started_at = time.time()
                game_over_elapsed_seconds = 0
                next_paralysis_check_at = pygame.time.get_ticks() + selected_level.get('paralysis_interval', 10000)
                paralysis_until = 0
                game_state = 'playing'
            elif other_mode_button.collidepoint(event.pos):
                game_state = 'menu'
                selected_level = None
                selected_level_name = ""
                particles = []
                game_over = False
                game_over_isotope = ""
                game_over_elapsed_seconds = 0
                next_paralysis_check_at = 0
                paralysis_until = 0

    if game_state == 'menu':
        screen.fill(WHITE)

        title_text = title_font.render("Select Level", True, BLACK)
        title_rect = title_text.get_rect(center=(width // 2, height // 4))
        screen.blit(title_text, title_rect)

        for level_name, button_rect in level_buttons:
            pygame.draw.rect(screen, GRAY, button_rect)
            pygame.draw.rect(screen, DARK_GRAY, button_rect, 2)
            level_text = font.render(level_name, True, BLACK)
            level_rect = level_text.get_rect(center=button_rect.center)
            screen.blit(level_text, level_rect)

        pygame.display.flip()
        continue

    if game_state == 'game_over':
        screen.fill(WHITE)

        game_over_text = title_font.render("GAME OVER!", True, BLACK)
        text_rect = game_over_text.get_rect(center=(width // 2, height // 2 - 60))
        screen.blit(game_over_text, text_rect)

        mode_text = title_font.render(selected_level_name, True, BLACK)
        mode_rect = mode_text.get_rect(center=(width // 2, height // 2))
        screen.blit(mode_text, mode_rect)

        isotope_text = title_font.render(game_over_isotope, True, BLACK)
        isotope_rect = isotope_text.get_rect(center=(width // 2, height // 2 + 60))
        screen.blit(isotope_text, isotope_rect)

        time_text = title_font.render(get_time_label(game_over_elapsed_seconds), True, BLACK)
        time_rect = time_text.get_rect(center=(width // 2, height // 2 + 120))
        screen.blit(time_text, time_rect)

        if pygame.time.get_ticks() - game_over_started_at >= 3000:
            game_state = 'game_over_menu'
            game_over_menu_started_at = pygame.time.get_ticks()

        pygame.display.flip()
        continue

    if game_state == 'game_over_menu':
        if pygame.time.get_ticks() - game_over_menu_started_at >= 10000:
            running = False
            continue

        screen.fill(WHITE)

        title_text = title_font.render("GAME OVER!", True, BLACK)
        title_rect = title_text.get_rect(center=(width // 2, height // 3 - 65))
        screen.blit(title_text, title_rect)

        mode_text = title_font.render(selected_level_name, True, BLACK)
        mode_rect = mode_text.get_rect(center=(width // 2, height // 3 - 5))
        screen.blit(mode_text, mode_rect)

        isotope_text = title_font.render(game_over_isotope, True, BLACK)
        isotope_rect = isotope_text.get_rect(center=(width // 2, height // 3 + 55))
        screen.blit(isotope_text, isotope_rect)

        time_text = title_font.render(get_time_label(game_over_elapsed_seconds), True, BLACK)
        time_rect = time_text.get_rect(center=(width // 2, height // 3 + 115))
        screen.blit(time_text, time_rect)

        pygame.draw.rect(screen, GRAY, restart_button)
        pygame.draw.rect(screen, DARK_GRAY, restart_button, 2)
        restart_text = font.render("Restart", True, BLACK)
        restart_rect = restart_text.get_rect(center=restart_button.center)
        screen.blit(restart_text, restart_rect)

        pygame.draw.rect(screen, GRAY, other_mode_button)
        pygame.draw.rect(screen, DARK_GRAY, other_mode_button, 2)
        other_mode_text = font.render("Other Mode", True, BLACK)
        other_mode_rect = other_mode_text.get_rect(center=other_mode_button.center)
        screen.blit(other_mode_text, other_mode_rect)

        pygame.display.flip()
        continue

    now_ticks = pygame.time.get_ticks()
    if selected_level.get('paralysis') and now_ticks >= next_paralysis_check_at:
        next_paralysis_check_at = now_ticks + selected_level.get('paralysis_interval', 10000)
        if random.random() < selected_level.get('paralysis_chance', 0.5):
            paralysis_until = now_ticks + selected_level.get('paralysis_duration', 3000)

    is_paralyzed = selected_level.get('paralysis') and now_ticks < paralysis_until
    keys = pygame.key.get_pressed()
    if not is_paralyzed:
        if keys[pygame.K_LEFT] and player['x'] - player['radius'] > 0:
            player['x'] -= 5
        if keys[pygame.K_RIGHT] and player['x'] + player['radius'] < width:
            player['x'] += 5

    if frame_count % PARTICLE_INTERVAL == 0:
        px = random.randint(20, width - 20)
        ptype = random.choices(['proton', 'neutron', 'photon'], weights=selected_level['weights'], k=1)[0]
        if ptype == 'photon':
            for _ in range(get_photon_count(player['protons'])):
                if selected_level_name in ('Choking', 'Miserable', 'Midgley\'s Gas', 'Permian'):
                    px = random.randint(20, width - 20)
                else:
                    px = max(20, min(width - 20, player['x'] + random.randint(-60, 60)))
                particles.append({'x': px, 'y': 0, 'type': ptype})
        else:
            particle = {'x': px, 'y': 0, 'type': ptype}
            if ptype == 'neutron' and random.random() < selected_level.get('neutron_decay_chance', 0):
                particle['vanish_y'] = random.randint(height // 4, height // 2)
            elif ptype == 'proton' and random.random() < selected_level.get('proton_decay_chance', 0):
                particle['vanish_y'] = random.randint(height // 4, height // 2)
            particles.append(particle)

    for p in particles:
        default_speed = selected_level['photon_speed'] if p['type'] == 'photon' else selected_level['particle_speed']
        p['y'] += p.get('speed', default_speed)

    new_particles = []
    for p in particles:
        if p['y'] - 10 > height:
            continue
        if p.get('vanish_y') is not None and p['y'] >= p['vanish_y']:
            decay_action = selected_level.get(f"{p['type']}_decay")
            if decay_action == 'photon':
                p['type'] = 'photon'
                p['speed'] = selected_level['photon_speed']
                p.pop('vanish_y', None)
            elif decay_action in ('proton', 'neutron'):
                p['type'] = decay_action
                p.pop('speed', None)
                p.pop('vanish_y', None)
            else:
                continue

        dist = math.hypot(p['x'] - player['x'], p['y'] - player['y'])
        if dist < player['radius'] + 10:
            if p['type'] == 'photon':
                game_over = True
                game_over_isotope = get_isotope_label(player['protons'], player['neutrons'])
                game_over_elapsed_seconds = int(time.time() - game_started_at)
                game_state = 'game_over'
                game_over_started_at = pygame.time.get_ticks()
                break
            elif p['type'] == 'proton':
                player['protons'] += 1
                player['radius'] = get_atomic_radius(player['protons'])
            else:
                player['neutrons'] += 1

            Z = player['protons']
            A = player['protons'] + player['neutrons']
            decay_level = isotope_decay_levels.get((Z, A), 5)
            if random.random() < decay_chances[decay_level]:
                game_over = True
                game_over_isotope = get_isotope_label(player['protons'], player['neutrons'])
                game_over_elapsed_seconds = int(time.time() - game_started_at)
                game_state = 'game_over'
                game_over_started_at = pygame.time.get_ticks()
                break
        else:
            new_particles.append(p)
    particles = new_particles

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (player['x'], player['y']), player['radius'])

    for p in particles:
        color = RED if p['type'] == 'proton' else BLUE if p['type'] == 'neutron' else GREEN
        pygame.draw.circle(screen, color, (p['x'], p['y']), 10)

    if selected_level.get('fog'):
        fog_surface = pygame.Surface((width, height // 2), pygame.SRCALPHA)
        fog_surface.fill((*FOG_GRAY, 245))
        screen.blit(fog_surface, (0, height // 4))

    Z = player['protons']
    A = player['protons'] + player['neutrons']
    element_text = font.render(get_isotope_label(player['protons'], player['neutrons']), True, BLACK)
    screen.blit(element_text, (10, 10))

    size_text = font.render(f"Mass Number: {A}", True, BLACK)
    screen.blit(size_text, (10, 40))

    mode_text = font.render(f"Mode: {selected_level_name}", True, BLACK)
    screen.blit(mode_text, (10, 70))

    if is_paralyzed:
        paralysis_text = font.render("Paralyzed", True, BLACK)
        screen.blit(paralysis_text, (10, 100))

    if game_over:
        game_over_text = font.render("GAME OVER!", True, BLACK)
        text_rect = game_over_text.get_rect(center=(width // 2, height // 2))
        screen.blit(game_over_text, text_rect)
        pygame.display.flip()
        continue

    pygame.display.flip()

pygame.quit()
sys.exit()
