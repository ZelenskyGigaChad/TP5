import random
import arcade
from attack_animation import AttackType
from game_state import GameState

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Roche, papier, ciseaux"
DEFAULT_LINE_HEIGHT = 45


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.DARK_ELECTRIC_BLUE)
        self.joueur = None
        self.computer = None
        self.rock = None
        self.paper = None
        self.scissors = None
        self.rock_computer = None
        self.paper_computer = None
        self.scissors_computer = None
        self.player_score = 0
        self.computer_score = 0
        self.player_attack_type = {}
        self.game_state = None
        self.computer_attack_type = None

    def setup(self):
        self.joueur = arcade.Sprite("assets/faceBeard.png", 0.85, center_x= 450, center_y= 650)
        self.computer = arcade.Sprite("assets/compy.png", 4,center_x= 1470,center_y= 650)
        self.player_attack_type = None
        self.computer_attack_type = random.choice([AttackType.ROCK, AttackType.PAPER, AttackType.SCISSORS])
        self.rock = arcade.Sprite("assets/srock.png", 0.5, center_x=395, center_y=437)
        self.paper = arcade.Sprite("assets/spaper.png", 0.5, center_x=505, center_y=430)
        self.scissors = arcade.Sprite("assets/scissors.png", 0.5, center_x=445, center_y=325)
        self.rock_computer = arcade.Sprite("assets/srock.png", 0.5, center_x=1480, center_y=437)
        self.paper_computer = arcade.Sprite("assets/spaper.png", 0.5, center_x=1480, center_y=437)
        self.scissors_computer = arcade.Sprite("assets/scissors.png", 0.5, center_x=1480, center_y=437)
        self.player_attack_chosen = False
        self.game_state = GameState.NOT_STARTED

    def validate_victory(self):
        if self.game_state == GameState.ROUND_ACTIVE:
            if self.computer_attack_type == self.player_attack_type:
                self.game_state = GameState.ROUND_DONE
            if self.player_attack_type == AttackType.ROCK and self.computer_attack_type == AttackType.SCISSORS:
                self.player_score += 1
                self.game_state = GameState.ROUND_DONE
            if self.player_attack_type == AttackType.SCISSORS and self.computer_attack_type == AttackType.PAPER:
                self.player_score += 1
                self.game_state = GameState.ROUND_DONE
            if self.player_attack_type == AttackType.PAPER and self.computer_attack_type == AttackType.ROCK:
                self.player_score += 1
                self.game_state = GameState.ROUND_DONE
            if self.player_attack_type == AttackType.SCISSORS and self.computer_attack_type == AttackType.ROCK:
                self.computer_score += 1
                self.game_state = GameState.ROUND_DONE
            if self.player_attack_type == AttackType.PAPER and self.computer_attack_type == AttackType.SCISSORS:
                self.computer_score += 1
                self.game_state = GameState.ROUND_DONE
            if self.player_attack_type == AttackType.ROCK and self.computer_attack_type == AttackType.PAPER:
                self.computer_score += 1
                self.game_state = GameState.ROUND_DONE
            if self.player_score == 3:
                self.game_state = GameState.GAME_OVER
            if self.computer_score == 3:
                self.game_state = GameState.GAME_OVER

    def draw_possible_attack(self):
        if self.game_state == GameState.ROUND_ACTIVE:
            self.rock.draw()
            self.paper.draw()
            self.scissors.draw()
        elif self.game_state == GameState.ROUND_DONE or self.game_state == GameState.GAME_OVER:
            if self.player_attack_type == AttackType.ROCK:
                self.rock.draw()
            elif self.player_attack_type == AttackType.PAPER:
                self.paper.draw()
            elif self.player_attack_type == AttackType.SCISSORS:
                self.scissors.draw()

    def draw_computer_attack(self):
        if self.game_state == GameState.ROUND_ACTIVE:
            self.rock_computer.draw()
            self.paper_computer.draw()
            self.scissors_computer.draw()
        elif self.game_state == GameState.ROUND_DONE or self.game_state == GameState.GAME_OVER:
            if self.computer_attack_type == AttackType.ROCK:
                self.rock_computer.draw()
            elif self.computer_attack_type == AttackType.PAPER:
                self.paper_computer.draw()
            elif self.computer_attack_type == AttackType.SCISSORS:
                self.scissors_computer.draw()

    def draw_instructions(self):
        arcade.draw_text(f"Le pointage du joueur est: {self.player_score} ", 315, 490, arcade.color.WHITE, 10, font_name="Kenney Future")
        arcade.draw_text(f"Le pointage du robot est: {self.computer_score} ", 1350, 490, arcade.color.WHITE, 10,font_name="Kenney Future")
        if self.game_state == GameState.NOT_STARTED:
            arcade.draw_text("Appuyez 'ESPACE' pour débuter", 680, 600, arcade.color.WHITE, 20, font_name="Kenney Future")
        elif self.game_state == GameState.ROUND_ACTIVE:
            arcade.draw_text("Choisissez Une Attaque!", 700, 600, arcade.color.RED, 23, font_name="Kenney Future")
        elif self.game_state == GameState.ROUND_DONE:
            arcade.draw_text("Appuyez sur ESPACE pour continuer", 690, 600, arcade.color.WHITE, 15,
                             font_name="Kenney Future")
        elif self.game_state == GameState.GAME_OVER:
            arcade.draw_text("Finito! Appuyez sur espace pour recommencer", 0, 200,
                             arcade.color.BLIZZARD_BLUE, 20,
                             width=SCREEN_WIDTH, align="center", font_name="Kenney Future")
            if self.player_score == 3:
                arcade.draw_text("Vous avez gagné !", 0, 450,
                                 arcade.color.BLIZZARD_BLUE, 20,
                                 width=SCREEN_WIDTH, align="center", font_name="Kenney Future")

            elif self.computer_score == 3:
                arcade.draw_text("Vous avez perdu !", 0, 450,
                                 arcade.color.BLIZZARD_BLUE, 20,
                                 width=SCREEN_WIDTH, align="center", font_name="Kenney Future")


    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(SCREEN_TITLE,
                         0,
                         SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 2,
                         arcade.color.BLACK_BEAN,
                         60,
                         width=SCREEN_WIDTH,
                         align="center", font_name="Kenney Future")

        self.draw_instructions()
        self.joueur.draw()
        self.computer.draw()
        arcade.draw_rectangle_outline(1480, 430, 75,
                                      75, arcade.color.RED, 5)
        arcade.draw_rectangle_outline(390, 430, 75,
                                      75, arcade.color.RED, 5)
        arcade.draw_rectangle_outline(500, 430, 75,
                                      75, arcade.color.RED, 5)
        arcade.draw_rectangle_outline(445, 320, 75,
                                      75, arcade.color.RED, 5)
        if self.game_state == GameState.ROUND_ACTIVE:
            self.draw_possible_attack()
        elif self.game_state == GameState.ROUND_DONE or self.game_state == GameState.GAME_OVER:
            self.draw_possible_attack()
            self.draw_computer_attack()

    def on_update(self, delta_time):
        pass

    def on_key_press(self, key, key_modifiers):
        if self.game_state == GameState.NOT_STARTED and key == arcade.key.SPACE:
            self.game_state = GameState.ROUND_ACTIVE
        elif self.game_state == GameState.ROUND_DONE and key == arcade.key.SPACE:
            self.game_state = GameState.ROUND_ACTIVE
            self.reset_round()
        elif self.game_state == GameState.GAME_OVER and key == arcade.key.SPACE:
            self.game_state = GameState.ROUND_ACTIVE
            self.player_score = 0
            self.computer_score = 0

    def reset_round(self):
        self.computer_attack_type = False

    def on_mouse_press(self, x, y, button, key_modifiers):
        if self.game_state == GameState.ROUND_ACTIVE:
            if self.rock.collides_with_point((x, y)):
                self.player_attack_type = AttackType.ROCK
            elif self.paper.collides_with_point((x, y)):
                self.player_attack_type = AttackType.PAPER
            elif self.scissors.collides_with_point((x, y)):
                self.player_attack_type = AttackType.SCISSORS
            self.computer_attack_type = random.choice([AttackType.ROCK, AttackType.PAPER, AttackType.SCISSORS])
            self.validate_victory()


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
