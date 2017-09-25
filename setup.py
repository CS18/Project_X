import cx_Freeze

executables = [cx_Freeze.Executable("project_x.py")]

cx_Freeze.setup(
    name="Project X",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["boss.png", "enemy_ship1.png","enemy_ship2.png","LCD_Solid.ttf", "player_ship.png"]}},
    executables = executables

    )