import arcade, time
from typing import List
from datetime import datetime

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sticker Store"

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2


# buttons
BTN_X = 0
BTN_Y = 1
BTN_WIDTH = 2
BTN_HEIGHT = 3
BTN_IS_CLICKED = 4
BTN_COLOR = 5
BTN_CLICKED_COLOR = 6

sticker_button = [280, 550, 120, 30, False, arcade.color.WHITE, arcade.color.ASH_GREY]


class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.text_angle = 0
        self.time_elapsed = 0.0

        # If you have sprite lists, you should create them here,
        # and set them to None

        self.stickers_list = None

        self.heart_sprite = None
        self.cost = 7

        self.smiley_sprite = None
        self.cost = 4
        
        self.sleeping_sprite = None
        self.cost = 5

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        start_y = 525
        start_x = 60
        arcade.draw_text("STICKER STORE",
                         start_x, start_y, arcade.color.BLUEBERRY, 30, width=300, align="center", font_name='Ariel')

    def on_update(self, delta_time):

        pass

        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        if (x > friends_button[BTN_X] and x < friends_button[BTN_X] + friends_button[BTN_WIDTH] and
                y > friends_button[BTN_Y] and y < friends_button[BTN_Y] + friends_button[BTN_HEIGHT]):
            friends_button[BTN_IS_CLICKED] = True

        if (x > sticker_store_button[BTN_X] and x < sticker_store_button[BTN_X] + sticker_store_button[BTN_WIDTH] and
                y > sticker_store_button[BTN_Y] and y < sticker_store_button[BTN_Y] + sticker_store_button[BTN_HEIGHT]):
            sticker_store_button[BTN_IS_CLICKED] = True

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """

        heart_button[BTN_IS_CLICKED] = False

        smiley_store_button[BTN_IS_CLICKED] = False

    def setup(self):
        # Create your sprites and sprite lists here
        self.heart_sprite = arcade.Sprite(":resources:images/heart.png", SPRITE_SCALING_PLAYER)
        self.heart_sprite.center_x = 50
        self.heart_sprite.center_y = 50
        self.sticker_list.append(self.heart_sprite)

        # Override arcade window methods
        window = arcade.get_window()
        window.on_draw = self.on_draw
        window.on_key_press = self.on_key_press
        window.on_key_release = self.on_key_release
        window.on_mouse_press = self.on_mouse_press
        window.on_mouse_release = self.on_mouse_release

        arcade.run()

def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()


if __name__ == "__main__":
    main()