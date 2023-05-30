
import arcade
from game_state import GameState
from attack_animation import AttaqueType
from attack_animation import AttackAnimation
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "ROCHE, PAPIER, CISEAUX"


class MyGame(arcade.Window):
    """
    La classe principale de l'application

    NOTE: Vous pouvez effacer les méthodes que vous n'avez pas besoin.
    Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.game_state = GameState.NOT_STARTED
        self.pointage_b#Renaud Deschenes 401
#JEu roche papoer siceauxot = 0
        self.pointage_player = 0
        self.face = None
        self.computer = None
        self.attaque_chosen = False
        self.player_attaque = None
        self.bot_attaque = False
        self.player_win = False
        self.player_lose = False
        self.partie_nulle = False
        self.round_won = False
        self.round_lost = False
        self.rock = AttackAnimation(AttaqueType.ROCK)
        self.paper = AttackAnimation(AttaqueType.PAPER)
        self.scissors = AttackAnimation(AttaqueType.SCISSOR)

    def setup(self):
        """
        Configurer les variables de votre jeu ici. Il faut appeler la méthode une nouvelle
        fois si vous recommencer une nouvelle partie.
        """
        # C'est ici que vous allez créer vos listes de sprites et vos sprites.
        # C'est aussi ici que vous charger les sons de votre jeu.
        self.face = arcade.Sprite("assets/faceBeard.png", .24)
        self.computer = arcade.Sprite("assets/compy.png", 1)

    def draw_player_attacks(self):
        """
        draw_player_attacks() est une fonction qui permet d'afficher tous les attaques que le joueur peut utiliser sur
        l'écran. Ces attaques sont: roche, papier et ciseaux.
        """

        self.scissors.center_x = 280
        self.scissors.center_y = 150
        self.scissors.draw()
        self.rock.center_x = 120
        self.rock.center_y = 150
        self.rock.draw()
        self.paper.center_x = 200
        self.paper.center_y = 150
        self.paper.draw()

    def draw_chosen_attack(self):
        """
        draw_chosen_attack() est une fonction qui permet d'afficher l'attaque choisie par le joueur sur l'écran.
        """

        if self.player_attaque == AttaqueType.ROCK:
            self.rock.center_x = 120
            self.rock.center_y = 150
            self.rock.draw()
        elif self.player_attaque == AttaqueType.PAPER:
            self.paper.center_x = 200
            self.paper.center_y = 150
            self.paper.draw()
        elif self.player_attaque == AttaqueType.SCISSOR:
            self.scissors.center_x = 280
            self.scissors.center_y = 150
            self.scissors.draw()

        if self.bot_attaque == AttaqueType.ROCK:
            self.rock.center_x = 599
            self.rock.center_y = 150
            self.rock.draw()
        elif self.bot_attaque == AttaqueType.SCISSOR:
            self.scissors.center_x = 600
            self.scissors.center_y = 150
            self.scissors.draw()
        elif self.bot_attaque == AttaqueType.PAPER:
            self.paper.center_x = 603
            self.paper.center_y = 150
            self.paper.draw()

    def validate_victory(self):
        """
        validate_victory() est une fonction qui permet à l'ordinateur de vérifier si le joueur a gagné la partie.
        """

        if self.player_win:
            arcade.draw_text("Partie gagnée!", 200, 530, arcade.color.RED, 30, font_name="Kenney Future")
        elif self.player_lose:
            arcade.draw_text("Partie perdue!", 200, 530, arcade.color.RED, 30, font_name="Kenney Future")
        elif self.partie_nulle:
            arcade.draw_text("Partie nulle!", 200, 530, arcade.color.RED, 30, font_name="Kenney Future")

    def on_draw(self):
        """
        C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
        de votre jeu à l'écran.
        """
        # Cette commande permet d'effacer l'écran avant de dessiner. Elle va dessiner l'arrière
        # plan selon la couleur spécifié avec la méthode "set_background_color".
        arcade.start_render()
        arcade.draw_text("ROCHE, PAPIER, CISEAU", 220, 570, arcade.color.WHITE, 20, font_name="Kenney Future")
        arcade.draw_text(f"Le pointage du joueur est: {self.pointage_player} ", 50, 90, arcade.color.WHITE, 10, font_name="Kenney Future")
        arcade.draw_text(f"Le pointage du joueur est: {self.pointage_bot}", 480, 90, arcade.color.WHITE, 10, font_name="Kenney Future")
        arcade.draw_rectangle_outline(120, 150, 50, 50, arcade.color.RED)
        arcade.draw_rectangle_outline(200, 150, 50, 50, arcade.color.RED)
        arcade.draw_rectangle_outline(280, 150, 50, 50, arcade.color.RED)
        arcade.draw_rectangle_outline(600, 150, 50, 50, arcade.color.RED)
        self.face.center_x = 200
        self.face.center_y = 220
        self.face.draw()
        self.computer.center_x = 600
        self.computer.center_y = 220
        self.computer.draw()

        if self.game_state == GameState.NOT_STARTED:
            arcade.draw_text("Appuyez 'ESPACE' pour débuter", 100, 530, arcade.color.WHITE, 23, font_name="Kenney Future")
            self.draw_player_attacks()
        elif self.game_state == GameState.ROUND_ACTIVE:
            arcade.draw_text("Choisissez Une Attaque!", 180, 530, arcade.color.RED, 23, font_name="Kenney Future")
            self.draw_player_attacks()
        elif self.game_state == GameState.ROUND_DONE:
            arcade.draw_text("Appuyez sur ESPACE pour continuer", 150, 400, arcade.color.WHITE, 15, font_name="Kenney Future")
            self.draw_chosen_attack()
            self.validate_victory()
        elif self.game_state == GameState.ROUND_OVER:
            self.draw_chosen_attack()
            self.validate_victory()
            if self.round_won is True:
                arcade.draw_text("La partie est terminée, vous avez gagné!", 150, 430, arcade.color.RED, 15, font_name="Kenney Future")
                arcade.draw_text("Appuyez <r> pour recommencer", 180, 300, arcade.color.RED, 15, font_name="Kenney Future")
            else:
                arcade.draw_text("La partie est terminée, vous avez perdu!", 150, 430, arcade.color.RED, 15, font_name="Kenney Future")
                arcade.draw_text("Appuyez <r> pour recommencer", 180, 300, arcade.color.RED, 15, font_name="Kenney Future")

    def on_update(self, delta_time):
        """
        Toute la logique pour déplacer les objets de votre jeu et de
        simuler sa logique vont ici. Normalement, c'est ici que
        vous allez invoquer la méthode "update()" sur vos listes de sprites.
        Paramètre:
            - delta_time : le nombre de milliseconde depuis le dernier update.
        """
        self.rock.on_update()
        self.scissors.on_update()
        self.paper.on_update()
        if self.game_state == GameState.ROUND_ACTIVE:
            if self.attaque_chosen:
                bot_attaque = random.randint(0, 2)
                if bot_attaque == 0:
                    self.bot_attaque = AttaqueType.ROCK
                elif bot_attaque == 1:
                    self.bot_attaque = AttaqueType.PAPER
                else:
                    self.bot_attaque = AttaqueType.SCISSOR

                if self.bot_attaque == AttaqueType.ROCK:
                    if self.player_attaque == AttaqueType.ROCK:
                        self.partie_nulle = True
                    elif self.player_attaque == AttaqueType.PAPER:
                        self.player_win = True
                    else:
                        self.player_lose = True
                elif self.bot_attaque == AttaqueType.PAPER:
                    if self.player_attaque == AttaqueType.ROCK:
                        self.player_lose = True
                    elif self.player_attaque == AttaqueType.PAPER:
                        self.partie_nulle = True
                    else:
                        self.player_win = True
                elif self.bot_attaque == AttaqueType.SCISSOR:
                    if self.player_attaque == AttaqueType.ROCK:
                        self.player_win = True
                    elif self.player_attaque == AttaqueType.PAPER:
                        self.player_lose = True
                    else:
                        self.partie_nulle = True

                if self.player_win:
                    self.pointage_player += 1
                    self.game_state = GameState.ROUND_DONE
                elif self.player_lose:
                    self.pointage_bot += 1
                    self.game_state = GameState.ROUND_DONE
                elif self.partie_nulle:
                    self.pointage_bot += 0
                    self.pointage_player += 0
                    self.game_state = GameState.ROUND_DONE

        elif self.game_state == GameState.ROUND_DONE:
            if self.pointage_player == 3:
                self.round_won = True
                self.game_state = GameState.ROUND_OVER
            elif self.pointage_bot == 3:
                self.round_won = False
                self.game_state = GameState.ROUND_OVER

    def on_key_press(self, key, key_modifiers):
        """
        Cette méthode est invoquée à chaque fois que l'usager tape une touche
        sur le clavier.
        Paramètres:
            - key: la touche enfoncée
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?

        Pour connaître la liste des touches possibles:
        http://arcade.academy/arcade.key.html
        """
        if key == arcade.key.SPACE:
            if self.game_state == GameState.NOT_STARTED:
                self.game_state = GameState.ROUND_ACTIVE
            elif self.game_state == GameState.ROUND_DONE:
                self.game_state = GameState.ROUND_ACTIVE
                self.player_win = self.player_lose = self.partie_nulle = False
                self.attaque_chosen = False
                self.player_attaque = AttaqueType.NOT_STARTED

        elif key == arcade.key.R:
            if self.game_state == GameState.ROUND_OVER:
                self.game_state = GameState.NOT_STARTED
                self.player_win = self.player_lose = self.partie_nulle = False
                self.pointage_player = self.pointage_bot = 0
                self.attaque_chosen = False
                self.player_attaque = AttaqueType.NOT_STARTED

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Méthode invoquée lorsque l'usager clique un bouton de la souris.
        Paramètres:
            - x, y: coordonnées où le bouton a été cliqué
            - button: le bouton de la souris appuyé
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl ?
        """
        if self.game_state == GameState.ROUND_ACTIVE:
            if self.scissors.collides_with_point((x, y)):
                self.player_attaque = AttaqueType.SCISSOR
                self.attaque_chosen = True

            if self.rock.collides_with_point((x, y)):
                self.player_attaque = AttaqueType.ROCK
                self.attaque_chosen = True

            if self.paper.collides_with_point((x, y)):
                self.player_attaque = AttaqueType.PAPER
                self.attaque_chosen = True


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
