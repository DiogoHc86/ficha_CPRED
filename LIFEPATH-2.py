from MODULOS.DEFS import *

wellcome()
while True:
    linha()
    roll_roles()
    roll_origins()
    roll_personality()
    roll_clothing()
    roll_hairstyle()
    roll_affectation()
    roll_value_most()
    roll_people()
    roll_people_most()
    roll_possession_most()
    roll_back_family()
    roll_description()
    roll_life_goals()
    roll_family_crisis()
    roll_enviroment_child()
    roll_friends(d10f)
    roll_enemy(d10e)
    roll_sr(d10e)
    roll_love(d10l)
    roll_stats()
    nome()
    linha()
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input("Deseja mais uma ficha?[S/N] ")).upper().strip()
    if pergunta in 'Nn':
        bye()
        break
    if pergunta in 'Ss':
        print(f'\n{"#"*40}')



