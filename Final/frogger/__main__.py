from os import times
import random
import arcade
import sys

sys.path.append('cse210-project-main/frogger/Pictures')

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"

PLAYER_MOVEMENT_SPEED = 2

class MyGame(arcade.Window):
    """
    Main application class.
    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)


        # If you have sprite lists, you should create them here,
        # and set them to None
        self.car_list = None
        self.truck_list = None
        self.frog_list = None
        self.physics_engine = None

    def setup(self):
        # Create your sprites and sprite lists here
        self.car_list = arcade.SpriteList()
        self.truck_list = arcade.SpriteList()

        self.frog = arcade.SpriteList()

        self.frog = arcade.Sprite("frogger/Pictures/frog.jpg", 0.3)

        self.frog.center_x = 400
        self.frog.center_y = 0


        for y in range(100, 700, 200):
            for i in range(5):
                car = arcade.Sprite("frogger/Pictures/convertible-car.png",0.05)
                car.center_x = random.randrange(100, 700, 100)
                car.center_y = y
                car.change_x = -3 #random.randrange(1,5)
                self.car_list.append(car)

        for y in range(200, 600, 200):
            for i in range(3):
                truck = arcade.Sprite("frogger/Pictures/truck.png",0.20)
                truck.center_x = random.randrange(100, 700, 150)
                truck.center_y = y

                truck.change_x = 1#random.randrange(1,5)
                self.truck_list.append(truck)

        arcade.set_background_color(arcade.color.BATTLESHIP_GREY)

        self.physics_engine = arcade.PhysicsEngineSimple(
            self.frog, self.car_list
        )

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()

        self.car_list.draw()

        self.frog.draw()
        
        self.truck_list.draw()



    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        for car in self.car_list:
            car.center_x += car.change_x
            if car.center_x <= 0:
                car.center_x = 800
        for truck in self.truck_list:
            truck.center_x += truck.change_x
            if truck.center_x >= 800:
                truck.center_x = 0

        self.physics_engine.update()
        self.car_list.update()
        self.frog.update()

        player_collision_car = arcade.check_for_collision_with_list(self.frog, self.car_list)
        player_collision_truck = arcade.check_for_collision_with_list(self.frog, self.truck_list)

        for collision in player_collision_car:
            if self.car_list in collision.sprite_lists:
                self.setup()
                return

        for collision in player_collision_truck:
            if self.truck_list in collision.sprite_lists:
                self.setup()
                return

        if self.frog.center_y >= 599:
            arcade.draw_text("test", 138, 492, (250, 250, 250), 58, font_name='comic')
            arcade.exit()
            for i in range(20):
                print('\n')
            print('******************************')
            print('Congratulations!')
            print('You have won!')
            print('******************************')
            return


    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        """
        if key == arcade.key.UP or key == arcade.key.W:
            self.frog.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.frog.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.frog.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.frog.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.UP or key == arcade.key.W:
            self.frog.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.frog.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.frog.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.frog.change_x = 0

def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()



if __name__ == "__main__":
    main()
