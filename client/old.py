#file contains old code

def commentator_generator_test_old(prompt): 
    battle_logs = []

    with open('replays/cleaned_logs/1/gen1ou/gen1ou-2093289585.txt') as f:
        current_round = "The start of the battle is:\n"
        battle_start = True
        for i,line in enumerate(f): 
            if "Turn" in line:
                battle_logs.append(current_round)
                current_round = ""
                battle_start = False
            else:
                if battle_start and "Switched to" in line:
                    line = line.replace("Switched to", "Started with")
            if "p1" in line: 
                line = line.replace("p1", "Ash")
            if "p2" in line:
                line = line.replace("p2", "Gary")
            current_round += line

        battle_logs.append(current_round)
    with open('hal.txt', 'w') as f:
        battle = BattleHistory("", prompt, URL_BATTLE_CHAT_GENERATOR_TEST, URL_CHECK_HALLUCINATION)
        for i, battle_line in enumerate(battle_logs):
            print("Round:",i)
            print(battle_line)
            expl = battle.generate_next_move_with_checks(battle_line)
            print(expl)
            print("\n\n")
        f.write("\n\n".join(battle.generated_story_history))


def wooper_hallucination_test(prompt):
    battle = BattleHistory("", prompt, URL_BATTLE_CHAT_GENERATOR_TEST, URL_CHECK_HALLUCINATION)
    turn_text = ''' Gary: Wooper used Ice punch on Dragonite for 100 damage it was super effective
Ash: Dragonite Roost and healed for 50
'''
    turn_info = {"pokemon": ["Dragonite", "Tauros", "Wooper"], "moves": ["Ice Punch"], "items": [], "abilities": []}
    expl = battle.generate_next_move_with_checks(turn_text, turn_info)
    print(expl)