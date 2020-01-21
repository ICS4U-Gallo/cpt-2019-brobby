import arcade, time, os
from typing import List
from datetime import datetime

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sticker Store"

SPRITE_SCALING_PLAYER = 0.07
SPRITE_SCALING_COIN = 0.2

points = 0

owned_stickers = []


class StickerStore(arcade.Window):
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
        self.button_list = None
        self.sticker_button_list = None

        self.stickers_list = None

        self.heart_sprite = None

        self.smiley_sprite = None

        self.sleeping_sprite = None

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        start_y = 500
        start_x = 55
        arcade.draw_text("STICKER STORE",
                         start_x, start_y, arcade.color.BLUEBERRY, 30, width=300, align="center", font_name='Ariel')

        self.stickers_list.draw()

        for button in self.sticker_button_list:
            button.draw()

        for button in self.button_list:
            button.draw()

        start_y = 50
        start_x = 240

        arcade.draw_text("POINTS",
                         start_x, start_y, arcade.color.BLUEBERRY, 18, width=200, align="center", font_name='Ariel')

        start_y = 20
        start_x = 240

        arcade.draw_text(f"{points}",
                         start_x, start_y, arcade.color.BLUEBERRY, 18, width=200, align="center", font_name='Ariel')

    def on_update(self, delta_time):

        pass

        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        check_mouse_press_for_buttons(x, y, self.button_list, self.sticker_button_list)

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """

        check_mouse_release_for_buttons(x, y, self.button_list, self.sticker_button_list)

    def setup(self):
        # Create your sprites and sprite lists here

        self.button_list = []
        self.sticker_button_list = []

        home_button = self.HomeButton(50, 550)
        self.button_list.append(home_button)

        sort_button = self.SortButton(100, 450)
        self.button_list.append(sort_button)

        heart_button = self.HeartButton(300, 390)
        self.sticker_button_list.append(heart_button)

        smiley_button = self.SmileyButton(300, 250)
        self.sticker_button_list.append(smiley_button)

        sleepy_button = self.SleepyButton(300, 120)
        self.sticker_button_list.append(sleepy_button)

        self.stickers_list = arcade.SpriteList()

        self.heart_sprite = arcade.Sprite("images/heart.png", SPRITE_SCALING_PLAYER)
        self.heart_sprite.center_x = 100
        self.heart_sprite.center_y = 370
        self.stickers_list.append(self.heart_sprite)

        self.smiley_sprite = arcade.Sprite("images/smiley.png", SPRITE_SCALING_PLAYER)
        self.smiley_sprite.center_x = 100
        self.smiley_sprite.center_y = 250
        self.stickers_list.append(self.smiley_sprite)

        self.sleeping_sprite = arcade.Sprite("images/sleeping.png", SPRITE_SCALING_PLAYER)
        self.sleeping_sprite.center_x = 100
        self.sleeping_sprite.center_y = 130
        self.stickers_list.append(self.sleeping_sprite)

        # Override arcade window methods
        window = arcade.get_window()
        window.on_draw = self.on_draw
        window.on_key_press = self.on_key_press
        window.on_key_release = self.on_key_release
        window.on_mouse_press = self.on_mouse_press
        window.on_mouse_release = self.on_mouse_release

        arcade.run()

    def collect_sticker_heart(self):
        self.owned_stickers.append(self.heart_sprite)

    class TextButton:
        """
        class that creates buttons

        Attrs:
            center_x: int
            center_y: int
            width: int
            height: int
            text: str
            font_size; int
            font_face: str
            face_color: str
            highlight_color: str
            shadow_color: str
            button_height: int

        """

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

        def draw(self):
            """ Draws the button """
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

    class HomeButton(TextButton):
        """
        Button that returns you home
        """
        def __init__(self, center_x, center_y):
            super().__init__(center_x, center_y + 20, 70, 30, "Home", 18, "Arial")

        def on_release(self):
            super().on_release()

    class SortButton(TextButton):
        """
        Button that returns you home
        """
        def __init__(self, center_x, center_y):
            super().__init__(center_x, center_y + 20, 70, 30, "Sort", 18, "Arial")

        def on_release(self):
            super().on_release()
            self.merge_sort(StickerStore.sticker_button_list)

        def merge_sort(self, sticker_button_list: List) -> List:
            """
            Sorts the stickers from lowest to highest points
            Args: 
                sticker_button_list: List [int]
            Returns:
                List[int]
            """
            # base case
            if len(sticker_button_list) == 0:
                return sticker_button_list

            midpoint = len(sticker_button_list) // 2

            # two recursive steps
            # mergesort left
            left_side = self.merge_sort(sticker_button_list[:midpoint])
            # mergesort right
            right_side = self.merge_sort(sticker_button_list[midpoint:])
            # merge the two together
            sorted_list = []

            # loop through both lists with two markers
            left_marker = 0
            right_marker = 0
            while left_marker < len(left_side) and right_marker < len(right_side):
                # if right value less than left value, add right value to sorted, increase right marker
                if left_side[left_marker] < right_side[right_marker]:
                    sorted_list.append(left_side[left_marker])
                    left_marker += 1
                # if left value less than right value, add left value to sorted, increase left marker
                else:
                    sorted_list.append(right_side[right_marker])
                    right_marker += 1

            # create a while loop to gather the rest of the values from either list
            while right_marker < len(right_side):
                sorted_list.append(right_side[right_marker])
                right_marker += 1

            while left_marker < len(left_side):
                sorted_list.append(left_side[left_marker])
                left_marker += 1

            # return the sorted list
            return sorted_list

    class HeartButton(TextButton):
        """
        Draws button for heart sticker
        """
        def __init__(self, center_x, center_y):
            super().__init__(center_x, center_y, 100, 40, "7 Points", 18, "Arial")

        def on_release(self):
            super().on_release()

    class SmileyButton(TextButton):
        def __init__(self, center_x, center_y):
            super().__init__(center_x, center_y, 100, 40, "4 Points", 18, "Arial")

        def on_release(self):
            super().on_release()

    class SleepyButton(TextButton):
        def __init__(self, center_x, center_y):
            super().__init__(center_x, center_y, 100, 40, "5 Points", 18, "Arial")

        def on_release(self):
            super().on_release()


def check_mouse_press_for_buttons(x, y, button_list, sticker_button_list):
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

    for button in sticker_button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()


def check_mouse_release_for_buttons(_x, _y, button_list, sticker_button_list):
    """ If a mouse button has been released, see if we need to process
        any release events. """
    for button in button_list:
        if button.pressed:
            button.on_release()

    for button in sticker_button_list:
        if button.pressed:
            button.on_release()


def main():
    """ Main method """
    game = StickerStore(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()


if __name__ == "__main__":
    main()
