import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Home Page"

SPRITE_SCALING_PLAYER = 0.07

hour_time_input = 23
minutes_time_input = 10

set_time = f"{hour_time_input}:{minutes_time_input}"

points = 0

days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]


class HomePage(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.button_list = None

        self.text_angle = 0
        self.time_elapsed = 0.0

        # If you have sprite lists, you should create them here,
        # and set them to None

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        for button in self.button_list:
            button.draw()

        self.day(0, 400)

        start_y = 525
        start_x = 100
        arcade.draw_text("GOAL",
                         start_x, start_y, arcade.color.BLUEBERRY, 40, width=200, align="center", font_name='Ariel')

        start_y = 480
        start_x = 100

        arcade.draw_text(f"{set_time}",
                         start_x, start_y, arcade.color.BLUEBERRY, 30, width=200, align="center", font_name='Ariel')

        start_y = 50
        start_x = 175

        arcade.draw_text("POINTS",
                         start_x, start_y, arcade.color.BLUEBERRY, 18, width=200, align="center", font_name='Ariel')

        start_y = 20
        start_x = 175

        arcade.draw_text(f"{points}",
                         start_x, start_y, arcade.color.BLUEBERRY, 18, width=200, align="center", font_name='Ariel')

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
        check_mouse_press_for_buttons(x, y, self.button_list)

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """

        check_mouse_release_for_buttons(x, y, self.button_list, )

    def setup(self):
        # Create your sprites and sprite lists here
        self.button_list = []

        sticker_store_button = self.StickerStoreButton(100, 60)
        self.button_list.append(sticker_store_button)

        start_y = 410
        for row in range(6):
            yes_button = self.YesButton(375, start_y, check())
            self.button_list.append(yes_button)

            no_button = self.NoButton(500, start_y, x_mark())
            self.button_list.append(no_button)

            start_y -= 50

        # Override arcade window methods
        window = arcade.get_window()
        window.on_draw = self.on_draw
        window.on_key_press = self.on_key_press
        window.on_key_release = self.on_key_release
        window.on_mouse_press = self.on_mouse_press
        window.on_mouse_release = self.on_mouse_release

        arcade.run()

    def day(self, num, start_y):
        if num == 6:
            return 1

        arcade.draw_text(f"{days[num]}", 40, start_y, arcade.color.BLUEBERRY, 20, width=200, align="center",
                         font_name='Ariel')

        arcade.draw_circle_outline(260, start_y + 12, 14, arcade.color.WHITE, 2)

        return self.day(num + 1, start_y - 50)



    class TextButton:
        """ Text-based button """

        def __init__(self,
                     center_x, center_y,
                     width, height,
                     text,
                     font_size=18,
                     font_face="Arial",
                     face_color=arcade.color.LIGHT_GRAY,
                     highlight_color=arcade.color.WHITE,
                     shadow_color=arcade.color.GRAY,
                     button_height=2):
            self.center_x = center_x
            self.center_y = center_y
            self.width = width
            self.height = height
            self.text = text
            self.font_size = font_size
            self.font_face = font_face
            self.pressed = False
            self.face_color = face_color
            self.highlight_color = highlight_color
            self.shadow_color = shadow_color
            self.button_height = button_height

            self.check_sprite = None
            self.x_sprite = None

        def draw(self):
            """ Draw the button """
            arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,
                                         self.height, self.face_color)

            if not self.pressed:
                color = self.shadow_color
            else:
                color = self.highlight_color

            # Bottom horizontal
            arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                             self.center_x + self.width / 2, self.center_y - self.height / 2,
                             color, self.button_height)

            # Right vertical
            arcade.draw_line(self.center_x + self.width / 2, self.center_y - self.height / 2,
                             self.center_x + self.width / 2, self.center_y + self.height / 2,
                             color, self.button_height)

            if not self.pressed:
                color = self.highlight_color
            else:
                color = self.shadow_color

            # Top horizontal
            arcade.draw_line(self.center_x - self.width / 2, self.center_y + self.height / 2,
                             self.center_x + self.width / 2, self.center_y + self.height / 2,
                             color, self.button_height)

            # Left vertical
            arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                             self.center_x - self.width / 2, self.center_y + self.height / 2,
                             color, self.button_height)

            x = self.center_x
            y = self.center_y
            if not self.pressed:
                x -= self.button_height
                y += self.button_height

            arcade.draw_text(self.text, x, y,
                             arcade.color.BLACK, font_size=self.font_size,
                             width=self.width, align="center",
                             anchor_x="center", anchor_y="center")


        def on_press(self):
            self.pressed = True

        def on_release(self):
            self.pressed = False

    class StickerStoreButton(TextButton):
        def __init__(self, center_x, center_y):
            super().__init__(center_x, center_y, 150, 75, "Sticker Store!", 18, "Ariel")

        def on_release(self):
            super().on_release()

    class YesButton(TextButton):
        def __init__(self, center_x, center_y, action):
            super().__init__(center_x, center_y, 100, 30, "Yes", 18, "Ariel")
            self.action = action

        def on_release(self):
            super().on_release()
            if self.pressed:
                check()

    class NoButton(TextButton):
        def __init__(self, center_x, center_y, action):
            super().__init__(center_x, center_y, 100, 30, "No", 18, "Ariel")
            self.action = action

        def on_release(self):
            super().on_release()
            if self.pressed:
                x_mark()


def check_mouse_press_for_buttons(x, y, button_list):
    """ Given an x, y, see if we need to register any button clicks. """
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()


def check_mouse_release_for_buttons(_x, _y, button_list):
    """ If a mouse button has been released, see if we need to process
        any release events. """
    for button in button_list:
        if button.pressed:
            button.on_release()


def check():
    check_sprite = arcade.Sprite("images/check.png", SPRITE_SCALING_PLAYER)
    check_sprite.center_x = 260
    check_sprite.center_y = 400
    check_sprite.draw()


def x_mark():
    x_sprite = arcade.Sprite("images/x.png", SPRITE_SCALING_PLAYER)
    x_sprite.center_x = 260
    x_sprite.center_y = 400
    x_sprite.draw()


def main():
    """ Main method """
    game = HomePage(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()


if __name__ == "__main__":
    main()
