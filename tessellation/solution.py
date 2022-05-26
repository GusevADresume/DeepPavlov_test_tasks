# %%
def main(desk_size: list[int, int]) -> list[list[int, int]]:
    desk = [[0 for x in range(desk_size[0])] for y in range(desk_size[1])]
    return find_way(desk)


def сheck_border(step, desk) -> bool:
    return (0 <= step[0] < len(desk[-1])) and (0 <= step[1] < len(desk))


def check_step(current_position, desk) -> list[list]:
    possible_steps = [[1, 2], [-1, 2], [2, 1], [-2, 1], [2, -1], [-2, -1], [1, -2], [-1, -2]]
    new_pos_list = []
    for step in possible_steps:
        if сheck_border([current_position[0] + step[0], current_position[1] + step[1]], desk):
            new_pos_list.append([current_position[0] + step[0], current_position[1] + step[1]])
    return new_pos_list


def step_selection(new_pos_list, desc) -> list[bool, list]:
    for step in new_pos_list:
        if check_replays(step, desc):
            return [True, step]
    return [False]


def check_replays(step, desc) -> bool:
    return desc[step[1]][step[0]] == 0


def desk_filling(desk) -> bool:
    for y in range(len(desk)):
        for x in desk[y]:
            if x == 0:
                return False
    return True


def find_way(desk) -> list[list]:
    desk = desk
    horse_way = []
    current_position = [[0, 0], ]
    while not desk_filling(desk):
        new_step = step_selection(check_step(current_position[-1], desk), desk)
        if new_step[0]:
            horse_way.append(new_step[1])
            desk[new_step[1][1]][new_step[1][0]] = 1
            current_position.append(new_step[1])
        if not new_step[0]:
            current_position.pop()
            horse_way.append(current_position[-1])
    return horse_way


if __name__ == '__main__':
    main()
