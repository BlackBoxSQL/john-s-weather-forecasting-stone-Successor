import display_cnavas
import forecast_result
import random
if __name__ == '__main__':
    random.choice(display_cnavas.display_weather)()
    option=input("What do you see about the stone?\n:::::::>>  Chose One from "
                 "bellow for weather cast report  <<::::::::\n\n"
          "A) Stone is Wet                  E) Can't see stone\n"
          "B) Stone is Dry                  F) Swinging stone\n"
          "C) Shadow on ground              G) Stone jumping Up & Down\n"
          "D) White on top                  H) Stone gone\n")

    if option == 'A':
        forecast_result.result_stone_is_wet()
    if option == 'B':
        forecast_result.result_stone_is_dry()
    if option == 'C':
        forecast_result.result_shadow_on_ground()
    if option == 'D':
        forecast_result.result_white_on_top()
    if option == 'E':
        forecast_result.result_cant_see_stone()
    if option == 'F':
        forecast_result.result_swinging_stone()
    if option == 'G':
        forecast_result.result_stone_jumping_up_and_down()
    if option == 'H':
        forecast_result.result_stone_gone()