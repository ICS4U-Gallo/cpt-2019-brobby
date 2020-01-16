import arcade, time
from typing import List
from datetime import datetime

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Home Page"

hour_time_input = 23
minutes_time_input = 10

set_time = f"{hour_time_input}:{minutes_time_input}"

points = 0

#buttons
BTN_X = 0
BTN_Y = 1
BTN_WIDTH = 2
BTN_HEIGHT = 3
BTN_IS_CLICKED = 4
BTN_COLOR = 5
BTN_CLICKED_COLOR = 6

friends_button = [280, 550, 120, 30, False, arcade.color.WHITE, arcade.color.ASH_GREY]
sticker_store_button = [0, 0, 200, 100, False, arcade.color.WHITE, arcade.color.ASH_GREY]


class Home_Page(arcade.Window):
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

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        start_y = 400
        start_x = 40
        days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

        for i in range(6):
            arcade.draw_text(f"{days[i]}",
                             start_x, start_y, arcade.color.BLUEBERRY, 20, width=200, align="center", font_name='Ariel')

            arcade.draw_circle_outline(start_x + 220, start_y + 12, 14, arcade.color.WHITE, 2)

            start_y -= 50

        # def day_list(days: List[int], x: int) -> int:
        #     if x == len(days):
        #         return 0
        #     return days[x] + day_list(days, x + 1)

        start_y = 525
        start_x = 100
        arcade.draw_text("GOAL",
                         start_x, start_y, arcade.color.BLUEBERRY, 40, width=200, align="center", font_name='Ariel')

        start_y = 480
        start_x = 100

        # arcade.draw_lrtb_rectangle_outline(start_x, start_x + width,
        #                                    start_y + height, start_y,
        #                                    arcade.color.BLUEBERRY, 1)
        arcade.draw_text(f"{set_time}",
                         start_x, start_y, arcade.color.BLUEBERRY, 30, width=200, align="center", font_name='Ariel')

        start_y = 50
        start_x = 240

        arcade.draw_text("POINTS",
                         start_x, start_y, arcade.color.BLUEBERRY, 18, width=200, align="center", font_name='Ariel')

        start_y = 20
        start_x = 240

        arcade.draw_text(f"{points}",
                         start_x, start_y, arcade.color.BLUEBERRY, 18, width=200, align="center", font_name='Ariel')

        if friends_button[BTN_IS_CLICKED]:
            color = friends_button[BTN_CLICKED_COLOR]
        else:
            color = friends_button[BTN_COLOR]

            # Draw friend_button
        arcade.draw_xywh_rectangle_filled(friends_button[BTN_X],
                                          friends_button[BTN_Y],
                                          friends_button[BTN_WIDTH],
                                          friends_button[BTN_HEIGHT],
                                          color)
        start_y = 555
        start_x = 265

        arcade.draw_text("FRIENDS",
                         start_x, start_y, arcade.color.BLUEBERRY, 16, width=150, align="center", font_name='Ariel')

        if sticker_store_button[BTN_IS_CLICKED]:
            color = sticker_store_button[BTN_CLICKED_COLOR]
        else:
            color = sticker_store_button[BTN_COLOR]

            # Draw friend_button
        arcade.draw_xywh_rectangle_filled(sticker_store_button[BTN_X],
                                          sticker_store_button[BTN_Y],
                                          sticker_store_button[BTN_WIDTH],
                                          sticker_store_button[BTN_HEIGHT],
                                          color)

        start_y = 60
        start_x = 0

        arcade.draw_text("STICKER STORE",
                         start_x, start_y, arcade.color.BLUEBERRY, 16, width=200, align="center", font_name='Ariel')


        # start_y = 425
        # start_x = 100
        #
        # # hours
        # total_seconds = hour_time_input * 60 * 60 + minutes_time_input * 60
        # current = dattime.now()
        # difference_seconds = total_seconds - current
        #
        # # hours_left = difference_seconds // 3600
        # # minutes_left = hours_left // 60
        #
        # arcade.draw_text(f"{int(difference_seconds)}",
        #                  start_x, start_y, arcade.color.BLUEBERRY, 30, width=200, align="center", font_name='Ariel')

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

        friends_button[BTN_IS_CLICKED] = False

        sticker_store_button[BTN_IS_CLICKED] = False

    def setup(self):
        # Create your sprites and sprite lists here

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
    game = Home_Page(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()


if __name__ == "__main__":
    main()
