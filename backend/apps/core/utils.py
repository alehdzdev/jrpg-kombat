# -*- coding: utf-8 -*-


class Player:
    def __init__(
        self, name: str, last_name: str, combinations: dict, player_dict: dict
    ) -> None:
        self.name = name
        self.last_name = (last_name,)
        self.combinations = combinations
        self.dict = player_dict

    def combine_moves(self) -> list:
        combined_moves = []
        for move, hit in zip(self.dict.get('movimientos'), self.dict.get('golpes')):
            combined_moves.append(move + hit)
        return combined_moves

    def find_combinations(self) -> list:
        moves = []

        for move in self.combine_moves():
            found_combinations = []
            i = 0

            while i < len(move):
                found_combination = False

                for combination in self.combinations:
                    if move[i:].startswith(combination):
                        found_combinations.append(combination)
                        i += len(combination)
                        found_combination = True
                        break

                if not found_combination:
                    i += 1

            moves.append(found_combinations)

        return moves

    def get_moves(self, player: str) -> list:
        turns = self.find_combinations()
        moves = []
        for turn in turns:
            turn_str = f'{self.name}'
            turn_value = 0
            for move in turn:
                combination = self.combinations.get(move)
                turn_str += f' {combination.get("name")}'
                turn_value += combination.get('value')
            moves.append({'text': turn_str, 'value': turn_value, 'player': player})
        return moves


def get_first_turn(player1: dict, player2: dict) -> str:
    player1_movements = player1.get('movimientos')
    player2_movements = player2.get('movimientos')
    player1_hits = player1.get('golpes')
    player2_hits = player2.get('golpes')

    if (len(player2_movements) + len(player2_hits)) < (
        len(player1_movements) + len(player1_hits)
    ):
        return 'player2'
    elif (len(player2_movements) + len(player2_hits)) == (
        len(player1_movements) + len(player1_hits)
    ):
        if len(player2_movements) < len(player1_movements):
            return 'player2'
        elif len(player2_movements) == len(player1_movements):
            if len(player2_hits) < len(player1_hits):
                return 'player2'
            else:
                return 'player1'
    return 'player1'


def combine_players_moves(first_turn_list, first_turn_player_name, second_turn_list, second_turn_player_name) -> list:
    while len(first_turn_list) < len(second_turn_list):
        first_turn_list.append({
            'text': f'{first_turn_player_name} está confundido y se quedó estático',
            'value': 0,
            'player': first_turn_list[0].get('player')
        })
    while len(second_turn_list) < len(first_turn_list):
        second_turn_list.append({
            'text': f'{second_turn_player_name} está confundido y se quedó estático',
            'value': 0,
            'player': second_turn_list[0].get('player')
        })

    return [item for pair in zip(first_turn_list, second_turn_list) for item in pair]


def kombat(data: dict):
    player1 = Player(
        name='Tonyn',
        last_name='Stallone',
        combinations={
            'DSDP': {'name': 'conecta un Taladoken', 'value': 3},
            'SDK': {'name': 'usa un Remuyuken', 'value': 2},
            'P': {'name': 'le da un puñetazo', 'value': 1},
            'K': {'name': 'da una patada', 'value': 1},
            'W': {'name': 'salta', 'value': 0},
            'S': {'name': 'baja', 'value': 0},
            'A': {'name': 'retrocede', 'value': 0},
            'D': {'name': 'avanza', 'value': 0},
        },
        player_dict=data.get('player1')
    )
    player2 = Player(
        name='Arnaldor',
        last_name='Shuatseneguer',
        combinations={
            'SAK': {'name': 'conecta un Remuyuken', 'value': 3},
            'ASAP': {'name': 'usa un Taladoken', 'value': 2},
            'P': {'name': 'le da un puñetazo', 'value': 1},
            'K': {'name': 'da una patada', 'value': 1},
            'W': {'name': 'salta', 'value': 0},
            'S': {'name': 'baja', 'value': 0},
            'A': {'name': 'avanza', 'value': 0},
            'D': {'name': 'retrocede', 'value': 0},
        },
        player_dict=data.get('player2')
    )
    player1_life = 6
    player2_life = 6
    first_turn = get_first_turn(player1.dict, player2.dict)
    player1_moves = player1.get_moves('player1')
    player2_moves = player2.get_moves('player2')
    kombat = combine_players_moves(player1_moves, player1.name, player2_moves, player2.name) if first_turn == 'player1' else combine_players_moves(player2_moves, player2.name, player1_moves, player1.name) # noqa
    finish = False
    loser = ''
    index = 0
    kombat_story = []
    while not finish:
        move = kombat[index]
        turn = move.get('player')
        turn_action = move.get('text')
        turn_value = move.get('value')
        kombat_story.append(turn_action)
        print(turn_action)
        if turn == 'player1':
            player2_life -= turn_value
            finish = True if player2_life <= 0 else False
            loser = 'player2'
        else:
            player1_life -= turn_value
            finish = True if player1_life <= 0 else False
            loser = 'player1'
        index += 1

    result = f"El ganador del TalanaKombatJRPG es {player1.name if loser == 'player2' else player2.name}"
    print(result)
    kombat_story.append(result)
    return kombat_story
