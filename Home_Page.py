import arcade

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Home Page"

set_time = "11:00"

class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        self.text_angle = 0
        self.time_elapsed = 0.0

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        start_y = 525
        start_x = 100

        arcade.draw_text("GOAL",
                         start_x, start_y, arcade.color.BLUEBERRY, 40, width=200, align="center", font_name='Ariel')

        start_y = 465
        start_x = 100
        width = 200
        height = 40

        arcade.draw_lrtb_rectangle_outline(start_x, start_x + width,
                                           start_y + height, start_y,
                                           arcade.color.BLUEBERRY, 1)
        arcade.draw_text(f"{set_time}",
                         start_x, start_y, arcade.color.BLUEBERRY, 30, width=200, align="center", font_name='Ariel')

        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):

        self.time_elapsed += delta_time

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
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
