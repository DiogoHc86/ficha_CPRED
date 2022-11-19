from random import choices, choice, randrange

und = "\033[4m"
norm = "\033[m"
yell = "\033[33m"
red = "\033[31m"
ppr = "\033[35m"
red_ = "\033[4;31m"
yell_ = "\033[4;33m"

d10f = (randrange(1, 11)-7)
d10e = (randrange(1, 11) - 7)
d10l = (randrange(1, 11) - 7)

def criararq(arq):
    a = open(arq, 'wt')
    a.close()
    print(f'Arquivo de {arq} criado com sucesso')


def wellcome():
    print(f'"Bem vindo a Nigth City choomba" diz o guarda na fronteira.')
    print()


def nome():
    n = str(input("Qual seu nome? ")).capitalize()
    salvararq('catalogo.txt','Nome\n', n)


def salvararq(arq,titulo, txt):
    a = open(arq, 'at')
    a.write(f'{titulo} - {txt}\n')
    a.close()


def roll_roles():
    roles = ["Rockerboy", "Solo", "Netrunner", "Tech", "Medtech", "Media", "Exec", "Lawman", "Fixer", "Nomad" ]
    role = choice(roles)
    print(f'{und}Qual seu Papel{norm}? {role}')
    salvararq('catalogo.txt', 'Papel', role)


def roll_origins():
    origins = ['North American', 'South/Central American', 'Western European', 'Eastern European',
               'Middle Eastern/North African', 'Sub-Saharan African', 'South Asian', 'South East Asian',
               'East Asian', 'Oceania/Pacific Islander']
    select_or = choice(origins)
    print("{}Onde vc nasceu{}? {}.\n" \
        "{}Qual desses idiomas vc fala?{}".format(und, norm, select_or, und, norm))
    salvararq('catalogo.txt', 'Local de nascimento', select_or)

    if (select_or == origins[0]):
        n = "Chinese, Cree, Creole, English,French, Navajo, Spanish"
    elif (select_or == origins[1]):
        n = "Creole, English, German, Guarani,Mayan, Portuguese, Quechua, Spanish"
    elif (select_or == origins[2]):
        n = "Dutch, English, French, German, Italian, Norwegian, Portuguese, Spanish"
    elif (select_or == origins[3]):
        n = "English, Finnish, Polish, Romanian, Russian, Ukrainian"
    elif (select_or == origins[4]):
        n = "Arabic, Berber, English, Farsi, French, Hebrew, Turkish"
    elif (select_or == origins[5]):
        n = "Arabic, English, French, Hausa, Lingala,\nOromo, Portuguese, Swahili, Twi, Yoruba"
    elif (select_or == origins[6]):
        n = "Bengali, Dari, English, Hindi, Nepali,\nSinhalese, Tamil, Urdu"
    elif (select_or == origins[7]):
        n = "Arabic, Burmese, English, Filipino, Hindi,\nIndonesian, Khmer, Malayan, Vietnamese"
    elif (select_or == origins[8]):
        n = "Cantonese Chinese, English, Japanese, Korean,\nMandarin Chinese, Mongolian"
    else:
        n = "English, French, Hawaiian, Maori,\nPama-Nyungan, Tahitian"

    print(n)
    salvararq('catalogo.txt', 'Idiomas', n)


def roll_personality():
    personality = ["Shy", "Secretive", "Rebellious", "Antisocial", "Violent", "Arrogant",
                   "Proud", "Aloof", "Moody", "Rash", "Frivolous", "Headstrong", "Fussy", "Nervous",
                   "Stable", "Serious", "Silly", "Fluff – Hearted", "Deceptive", "Intellectual",
                   "Detached", "Friendly", "Outgoing", "Mysteriuos", "Blabbermouth", "Nosy",
                   "Compassionate", "Idealistc", "Perfectionist", "Apathetic", "Fatalistc", "Subtle", "Cunning",
                   "Hedonistic", "Gracious", "Self-critical", "Tidy", "Adaptable", "Blunt", "Complacent"]

    list = []
    nova_list = []

    num = randrange(2, 4)
    for count in range(num):
        list.append(choice(personality))
        for element in list:
            if element not in nova_list:
                nova_list.append(element)
    if len(nova_list) < num:
        nova_list.append(choice(personality))

    if num == 2:
        print("\033[4mPersonlidade?\033[m '{}' e '{}'".format(nova_list[0], nova_list[1]))
    else:
        print("\033[4mPersonalidade?\033[m '{}', '{}' e '{}'".format(nova_list[0], nova_list[1], nova_list[2]))

    salvararq('catalogo.txt', 'Personalidade', nova_list)


def roll_clothing():
    clothing = ['Generic Chic (Standard, Colorful, Modular)', 'Leisurewear (Comfort, Agility, Athleticism)',
                'Urban Flash (Flashy, Technological, Streetwear)', 'Businesswear (Leadership, Presence, Authority)',
                'High Fashion (Exclusive, Designer, Couture)', 'Bohemian (Folksy, Retro, Free-spirited)',
                'Bag Lady Chic (Homeless, Ragged, Vagrant)', 'Gang Colors (Dangerous, Violent, Rebellious)',
                'Nomad Leathers (Western, Rugged, Tribal)', 'Asia Pop (Bright, Costume-like, Youthful)',
                'Cyber Grunge (Neon, Individualist, Defiant)', 'Crypto Core (Weird, Practical, Academic)',
                'VSCO (Relaxed, Soft, Pastel)', 'Y2K (Eccentric, Playful, 00s)',
                'Retro Chic (Old-school Cool, Traditional, Distinguished )',
                'Glam Witch (Dark, Occult, Spiritual )', 'Corpo Punk (Understated, Enticing, Edgy)',
                'Dolly Key (Antique, Distressed, Layered)',
                'Mall Goth (Spiky, Provocative, Accessorised)', 'Military Chic (Tactical, Camo, Intimidating)']
    c = choice(clothing)
    print("{}Seu estilo de roupa{}? {}".format(und, norm,c))
    salvararq('catalogo.txt','Estilo de roupa', c)


def roll_hairstyle():
    hairstyle = ['Mohawk', 'Long and ratty', 'Short and spiked', 'Wild and all over', 'Bald', 'Striped', 'Wild colors',
                 'Neat and short', 'Short and curly', 'Long and straight', 'Short sides long top',
                 'Chin Length & Thick',
                 'Slicked Back', 'Mullet', 'Messy Coils', 'Tightly Braided', 'Military Cut', 'Side Parted',
                 'Multicoloured', 'Asymmetrical']
    h = choice(hairstyle)
    print("{}Como é seu cabelo{}? {}".format(und, norm,h))
    salvararq('catalogo.txt', 'Corte de cabelo', h)


def roll_affectation():
    affectation = ['Tattoos', 'Mirrorshades', 'Ritual scars', 'Spiked gloves', 'Nose rings',
                   'Tongue or other piercings',
                   'Strange fingernail implants', 'Spiked boots or heels', 'Fingerless gloves', 'Strange contacts',
                   'Jacket coverd in sewn on patches ', 'Personalised Lighter', 'Particular shade of lipstick',
                   'A favourite hat', 'Large, retro headphones', 'Excessive jewellery', 'Stylish bag/backpack',
                   'Particularly funky socks/stockings', 'Decorated/Personalised airhypo', 'Cool retro hip flash',
                   'Distinct belt buckle']
    aff = choice(affectation)
    print("{}Sua maior afetação{}? {}".format(und,norm, aff))
    salvararq('catalogo.txt', 'Afetação', aff)


def roll_value_most():
    value_most = ['Money', 'Honor', 'Your word', 'Honesty', 'Knowledge', 'Vengeance', 'Love', 'Power', 'Family',
                  'Friendship', 'Faith', 'Loyalty', 'Image', 'Life', 'Stability', 'Compassion', 'Independence',
                  'Courage',
                  'Justice', 'Pleasure']
    vm = choice(value_most)
    print("{}O que vc mais valoriza{}? {}".format(und, norm, vm))
    salvararq('catalogo.txt', 'O que vc mais valoriza?', vm)


def roll_people():
    people = ['I stay neutral', 'I stay neutral', 'I like almost everyone', 'I hate almost everyone',
              'People are tools. Use them for your own goals then discard them',
              'Every person is a valuable individual',
              'People are obstacles to be destroyed if they cross me',
              'People are untrustworthy. Do not depend on anyone',
              'Wipe ‘em all out and let the cockroaches take over', 'People are wonderful!',
              'I either love or hate them. It changes by the hour.',
              'People are like stickers. Collect as many as you can.', 'I like them better than I like myself.',
              'You need the right one for the right job.', 'They are fascinating to watch. From afar.',
              'I stop thinking about them the moment they are out of my bed.', 'I avoid them like the plague.',
              'They aways find new ways to disappoint me.', 'I crave and fear their presence at the same time.',
              'People are like little puzzles for me to crack.', 'I find them hard to understand.']
    pp = choice(people)
    print("{}Como  vc se sente sobre as pessoas{}? {}".format(und, norm, pp))
    salvararq('catalogo.txt', 'Sobre as pessoas?', pp)


def roll_people_most():
    people_most = ['A parent', 'A brother or sister', 'A lover', 'A friend', 'Yourself', 'A pet', 'A teacher or mentor',
                   'A public figure', 'A personal hero', 'No one', "A religious figure",
                   "A person who doesn't know you exist.",
                   "Your boss.", "Your therapist.", "A child.", "Someone you’ve only met on the net.",
                   "Someone who is dead.",
                   "A rival.", "A fictional character."]
    pm = choice(people_most)
    print("{}Quem é a pessoa mais importante da sua vida{}? {}".format(und,norm,pm))
    salvararq('catalogo.txt', 'Pessoa(s) de mais valor?', pm)


def roll_possession_most():
    possession_most = ['A weapon', 'A tool', 'A piece of clothing', 'A photograph', 'A book or diary', 'A recording',
                       'A musical instrument', 'A piece of jewelry', 'A toy', 'A letter', "A data chip", "A recipe",
                       "And old console",
                       "A figurine", "A piece of art", "A bottle of vintage alcohol", "A family collection",
                       "A piece of military memorabilia",
                       "A set of dice", "A deed", "A seed"]
    po = choice(possession_most)
    print("{}Um objeto que vc mais valoriza{}? {}".format(und, norm,po))
    salvararq('catalogo.txt', 'Objeto de maior valor? ', po)


def roll_back_family():
    background_family = ['Corporate Execs', 'Corporate Managers', 'Corporate Technicians', 'Nomad Pack',
                         'Ganger "Family"',
                         'Combat Zoners',
                         'Urban Homeless', 'Megastructure Warren Rats', 'Reclaimers', 'Edgerunners']
    bf = choice(background_family)
    print("{}E sua família(Original Back){}? {}".format(und, norm, bf))
    salvararq('catalogo.txt', 'Background familiar?', bf)


def roll_life_goals():
    life_goals = ["Get rid of a bad reputation.", "Gain power and control.",
                  "Get off The Street no matter what it takes.",
                  "Cause pain and suffering to anyone who crosses you.",
                  "Live down your past life and try to forget it.",
                  "Hunt down those responsible for your miserable life and make them pay.",
                  "Get what's rightfully yours.",
                  "Save, if possible, anyone else involved in your background, like a lover, or family member.",
                  "Gain fame and recognition.", "Become feared and respected."]
    lg = choice(life_goals)
    print("{}Qual seu objetivo na vida{}? {}".format(und, norm, lg))
    salvararq('catalogo.txt', 'Seu objetivo na vida? ',lg)


def roll_family_crisis():
    family_crisis = ['Your family lost everything through betrayal.',
                     'Your family lost everything through badmanagement.',
                     'Your family was exiled or otherwise driven from their original home/nation/Corporation.',
                     'Your family is imprisoned, and you alone escaped.',
                     'Your family vanished. You are the only remaining member.',
                     'Your family was killed, and you were the only survivor.',
                     'Your family is involved in a long-term conspiracy, organization, or association, such as a crime family or revolutionary group.',
                     'Your family was scattered to the winds due to misfortune.',
                     'Your family is cursed with a hereditary feud that has lasted for generations.',
                     'You are the inheritor of a family debt; you must honor this debt before moving on with your life.']
    fc = choice(family_crisis)
    print("{}Sua crise familiar{}? {}".format(und, norm,fc))
    salvararq('catalogo.txt', 'Crise familiar? ',fc)


def roll_description():
    arquivo = open("descricao.txt", "r")
    bloco = []

    for linha in arquivo:
        linha = linha.split("**")
        bloco.append(choice(linha))

    arquivo.close()
    #return bloco
    #description = roll_description()
    de = choice(bloco)
    print("{}de que tipo (Description){}? {}".format(und, norm, de))
    salvararq('catalogo.txt', 'Qual descriçao? ', de)


def roll_enviroment_child():
    enviroment_child = ["Ran on The Street, with no adult supervision.",
                        'Spent in a safe Corp Zone walled off from the rest of the City.',
                        'In a Nomad pack moving from place to place.',
                        'In a Nomad pack with roots in transport (ships, planes, caravans).',
                        'In a decaying, once upscale neighborhood,now holding off the boosters to survive.',
                        'In the heart of the Combat Zone, living in a wrecked building or other squat.',
                        'In a huge "megastructure" building controlled by a Corp or the City.',
                        'In the ruins of a deserted town or city taken over by Reclaimers.',
                        'In a Drift Nation (a floating offshore city) that is a meeting place for all kinds of people.',
                        'In a Corporate luxury "starscraper," high above the rest of the teeming rabble.']
    ec = choice(enviroment_child)
    print("{}Como foi seu ambiente na infância{}? {}".format(und, norm, ec))
    salvararq('catalogo.txt', 'Ambiente familiar? ', ec)


def roll_friends(d10f):
    friends = ['Like an older sibling to you.', 'Like a younger sibling to you.', 'A teacher or mentor.',
               'A partner or coworker.', 'A former lover.', 'An old enemy.', 'Like a parent to you.',
               'An old childhood friend.', 'Someone you know from The Street.',
               'Someone with a common interest or goal.']

    if d10f   <=  0:
        print("{}Possui amigos?{} Não. Ninguém.".format(und,norm))
        salvararq('catalogo.txt', 'Amigos', 'Não. Ninguém.')
    elif d10f ==  1:
        amigo = choice(friends)
        print( f'{und}Possui amigos?{norm} Sim, {d10f} amigo.\n'
               f'{yell_}Quem?{norm} {d10f}º {amigo}')
        salvararq('catalogo.txt', 'Amigos? Sim, um(a)', amigo)
    elif d10f == 2:
        amigo = choice(friends)
        amigo2 = choice(friends)
        print(f'{und}Possui amigos?{norm} Sim,{d10f} amigos.\n'
                f'{yell_}Quem?{norm} {d10f-1}º {amigo}\n{yell_}Quem?{norm} {d10f}º {amigo2}')
        salvararq('catalogo.txt', 'Amigos? Sim, primeiro(a)', amigo)
        salvararq('catalogo.txt', 'Segundo(a)', amigo2)
    else:
        amigo = choice(friends)
        amigo2 = choice(friends)
        amigo3 = choice(friends)
        print(f'{und}Possui amigos?{norm} Sim,{d10f} amigos.\n'
               f'{yell_}Quem?{norm} {d10f-2}º {amigo}\n{yell_}Quem?{norm} {d10f-1}º {amigo2}\n{yell_}Quem?{norm} {d10f}º {amigo3}')
        salvararq('catalogo.txt', 'Amigos? Sim, primeiro(a)', amigo)
        salvararq('catalogo.txt', 'Segundo(a)', amigo2)
        salvararq('catalogo.txt', 'Terceiro(a)', amigo3)


def roll_enemy(d10e):
    enemys = ["Ex-friend", 'Ex-lover', 'Estranged relative', 'Childhood enemy', 'Person working for you',
              'Person you work for',
              'Partner or coworker', 'Corporate exec', 'Government official', 'Boosterganger']
    cause = ['Caused the other to lose face or status.', 'Caused the loss of lover, friend, or relative',
             'Caused a major public humiliation', 'Accused the other of cowardice or some othermajor personal flaw.',
             'Deserted or betrayed the other.', "Turned down the other's offer of a job or romantic involvement.",
             "You just don't like each other.", "One of you was a romantic rival.", "One of you was a business rival.",
             "One of you set the other up for a crime they didn't commit."]
    throw_in_u = ["Just themselves and even they won't go out of their way.", "Just themselves.",
                  "Just themselves and a close friend.",
                  "Themselves and a few (1d6/2) friends.", "Themselves and a few (1d10/2) friends.",
                  "An entire gang (at least 1d10 + 5 people).",
                  "The local cops or other Lawmen.", "A powerful gang lord or small Corporation.",
                  "A powerful Corporation.", "An entire city or government or agency."]
    if d10e <= 0:
        print(f'{red_}Inimigos?{norm} Não, nenhum.')
        salvararq('catalogo.txt', 'Inimigos?', 'Não, nenhum.')
    elif d10e == 1:
        print(f'{red_}Possui inimigos?{norm}')
        roll_tabel(f'Inimigos? Sim, 1 inimigo - ', enemys)
        roll_tabel(f'E por que? ', cause)
        roll_tabel(f'Com o que te ataca? ',throw_in_u)
    elif d10e == 2:
        print(f'{red_}Possui inimigos?{norm}')
        roll_tabel(f'Inimigos? Sim, dois \nPrimeiro - ', enemys)
        roll_tabel(f'E por que? ', cause)
        roll_tabel(f'Com o que te ataca? ', throw_in_u)

        roll_tabel(f'\nSegundo - ', enemys)
        roll_tabel(f'E por que? ', cause)
        roll_tabel(f'Com o que te ataca? ', throw_in_u)
    else:
        print(f'{red_}Possui inimigos?{norm}')
        roll_tabel(f'Inimigos? Sim, três \nPrimeiro - ', enemys)
        roll_tabel(f'E por que? ', cause)
        roll_tabel(f'Com o que te ataca? ', throw_in_u)

        roll_tabel(f'\nSegundo - ', enemys)
        roll_tabel(f'E por que? ', cause)
        roll_tabel(f'Com o que te ataca? ', throw_in_u)

        roll_tabel(f'\nTerceiro - ', enemys)
        roll_tabel(f'E por que? ', cause)
        roll_tabel(f'Com o que te ataca? ', throw_in_u)


def roll_sr(d10e):
    sw = ["Avoid the scum.", "Go into a murderous rage and try to physically rip their face off.",
          "Backstab them indirectly.", "Verbally attack them.",
          "Set them up for a crime or other transgression they didn't commit.",
          "Set out to murder or maim them."]
    weights = [20, 20, 20, 20, 10, 10]
    if d10e <= 0:
        print("Sem vingança")
        salvararq('catalogo.txt', 'Sweet Revenge!', 'Sem vingança')
    else:
        sr = choices(sw, weights)
        sr2 = choices(sw,weights)
        sr3 = choices(sw, weights)
        if d10e == 1:
            print(f'{red}Sweet Revenge!\nO que o 1 fara a respeito:{norm}\n{sr}')
            salvararq('catalogo.txt', '\nSweet Revenge!', sr)
        elif d10e == 2:
            print(f'{red}Sweet Revenge!\nO que o 1 fara a respeito:{norm}\n{sr}\n{red}O que o 2 fara a respeito:{norm}\n{sr2}')
            salvararq('catalogo.txt', '\nSweet Revenge! O que o 1 fara a respeito:\n', sr)
            salvararq('catalogo.txt', 'O que o 2 fara a respeito:\n', sr2)
        else:
            print("Sweet Revenge!\n{}O que o 1 fara a respeito:{}\n{}\n{}O que o 2 fara a respeito:{}\n{}\n{}O que o 3 fara a respeito:{}\n{}".format(red_,norm,sr,red_,norm,sr2,red_,norm,sr3))
            salvararq('catalogo.txt', '\nSweet Revenge! O que o 1 fara a respeito:\n', sr)
            salvararq('catalogo.txt', 'O que o 2 fara a respeito:\n', sr2)
            salvararq('catalogo.txt', 'O que o 3 fara a respeito:\n', sr3)



def roll_love(d10l):
    t_love = ["Your lover died in an accident.", "Your lover mysteriously vanished.", "It just didn't work out.",
              "A personal goal or vendetta came between you and your lover.",
              "Your lover was kidnapped", "Your lover went insane or cyberpsycho.", "Your lover committed suicide.",
              "Your lover was killed in a fight", "A rival cut you out of the action",
              "Your lover is imprisoned or exiled."]
    tl = choice(t_love)
    tl2 = choice(t_love)
    tl3 = choice(t_love)

    if d10l <= 0:
        print(f'{und}Amores perdidos?{norm} Não, nenhum.')
        salvararq('catalogo.txt', 'Amores perdidos? ', 'Não, nenhum.')
    elif d10l == 1:
        print(f'{und}Amores perdidos?{norm} Sim, {d10l} amor perdido.\n{ppr}Como?{norm} {d10l}º {tl}')
        salvararq('catalogo.txt', 'Amores perdidos? Sim, um: ', tl)
    elif d10l == 2:
        print( f'{und}Amores perdidos?{norm} Sim, {d10l} amores perdidos.\n'
               f'{ppr}Como?{norm} {d10l - 1}º {tl}\n'
               f'{ppr}Como?{norm} {d10l}º {tl2}')
        salvararq('catalogo.txt', 'Amores perdidos? Sim, dois. Primeiro(a): ', tl)
        salvararq('catalogo.txt', 'Amores perdidos? Segundo(a): ', tl2)
    else:
        print( f'{und}Amores perdidos?{norm} Sim, {d10l} amores perdidos.'
               f'{ppr}Como?{norm} {d10l - 2}º {tl}\n'
               f'{ppr}Como?{norm} {d10l - 1}º {tl2}\n'
               f'{ppr}Como?{norm} {d10l}º {tl3}')
        salvararq('catalogo.txt', 'Amores perdidos? Sim, dois. Primeiro(a): ', tl)
        salvararq('catalogo.txt', 'Segundo(a): ', tl2)
        salvararq('catalogo.txt', 'Terceiro(a): ', tl3)


def linha():
    salvararq('catalogo.txt', '#'*20,"#"*20)


def bye():
    print(f'"PRÓXIMO"\ndiz o guarda com um sorriso predatório no rosto')


def roll_stats():
    # METHOD 2 - EDGERUNERS
    from random import randint
    stt = ' '
    int = ref = dex = tech = cool = will = luck = move = body = emp = 0
    #print("Seus status são:")
    for c in range(1, 11):
        d10 = randint(1, 10)
        if c == 1:
            stt = 'INT'
            if d10 == 1:
                int = 6
            elif d10 == 2:
                int = 7
            elif d10 == 3:
                int = 5
            elif d10 == 4:
                int = 5
            elif d10 == 5:
                int = 6
            elif d10 == 6:
                int = 7
            elif d10 == 7:
                int = 7
            elif d10 == 8:
                int = 7
            elif d10 == 9:
                int = 7
            else:
                int = 6
            #print(f'Vc rolou {d10} e tem {int} em {stt}.')
        elif c == 2:
            stt = 'REF'
            if d10 == 1:
                ref = 7
            elif d10 == 2:
                ref = 8
            elif d10 == 3:
                ref = 8
            elif d10 == 4:
                ref = 8
            elif d10 == 5:
                ref = 6
            elif d10 == 6:
                ref = 7
            elif d10 == 7:
                ref = 7
            elif d10 == 8:
                ref = 8
            elif d10 == 9:
                ref = 7
            else:
                ref = 6
            #print(f'Vc rolou {d10} e tem {ref} em {stt}.')
        elif c == 3:
            stt = 'DEX'
            if d10 == 1:
                dex = 7
            elif d10 == 2:
                dex = 6
            elif d10 == 3:
                dex = 7
            elif d10 == 4:
                dex = 6
            elif d10 == 5:
                dex = 7
            elif d10 == 6:
                dex = 6
            elif d10 == 7:
                dex = 6
            elif d10 == 8:
                dex = 7
            elif d10 == 9:
                dex = 6
            else:
                dex = 8
            #print(f'Vc rolou {d10} e tem {dex} em {stt}.')
        elif c == 4:
            stt = 'TECH'
            if d10 == 1:
                tech = 3
            elif d10 == 2:
                tech = 3
            elif d10 == 3:
                tech = 4
            elif d10 == 4:
                tech = 4
            elif d10 == 5:
                tech = 5
            elif d10 == 6:
                tech = 5
            elif d10 == 7:
                tech = 5
            elif d10 == 8:
                tech = 5
            elif d10 == 9:
                tech = 4
            else:
                tech = 5
            #print(f'Vc rolou {d10} e tem {tech} em {stt}.')
        elif c == 5:
            stt = 'COOL'
            if d10 == 1:
                cool = 8
            elif d10 == 2:
                cool = 6
            elif d10 == 3:
                cool = 7
            elif d10 == 4:
                cool = 6
            elif d10 == 5:
                cool = 7
            elif d10 == 6:
                cool = 7
            elif d10 == 7:
                cool = 6
            elif d10 == 8:
                cool = 6
            elif d10 == 9:
                cool = 6
            else:
                cool = 6
            #print(f'Vc rolou {d10} e tem {cool} em {stt}.')
        elif c == 6:
            stt = 'WILL'
            if d10 == 1:
                will = 6
            elif d10 == 2:
                will = 6
            elif d10 == 3:
                will = 7
            elif d10 == 4:
                will = 7
            elif d10 == 5:
                will = 6
            elif d10 == 6:
                will = 6
            elif d10 == 7:
                will = 7
            elif d10 == 8:
                will = 6
            elif d10 == 9:
                will = 6
            else:
                will = 6
            #print(f'Vc rolou {d10} e tem {will} em {stt}.')
        elif c == 7:
            stt = 'LUCK'
            if d10 == 1:
                luck = 5
            elif d10 == 2:
                luck = 7
            elif d10 == 3:
                luck = 6
            elif d10 == 4:
                luck = 6
            elif d10 == 5:
                luck = 7
            elif d10 == 6:
                luck = 6
            elif d10 == 7:
                luck = 7
            elif d10 == 8:
                luck = 5
            elif d10 == 9:
                luck = 6
            else:
                luck = 5
            #print(f'vc rolou {d10} e tem {luck} em {stt}')
        elif c == 8:
            stt = 'MOVE'
            if d10 == 1:
                move = 5
            elif d10 == 2:
                move = 5
            elif d10 == 3:
                move = 7
            elif d10 == 4:
                move = 5
            elif d10 == 5:
                move = 6
            elif d10 == 6:
                move = 7
            elif d10 == 7:
                move = 6
            elif d10 == 8:
                move = 6
            elif d10 == 9:
                move = 5
            else:
                move = 6
            #print(f'vc rolou {d10} e tem {move} em {stt}')
        elif c == 9:
            stt = 'BODY'
            if d10 == 1:
                body = 5
            elif d10 == 2:
                body = 7
            elif d10 == 3:
                body = 6
            elif d10 == 4:
                body = 6
            elif d10 == 5:
                body = 7
            elif d10 == 6:
                body = 6
            elif d10 == 7:
                body = 7
            elif d10 == 8:
                body = 5
            elif d10 == 9:
                body = 6
            else:
                body = 5
            #print(f'vc rolou {d10} e tem {body} em {stt}')
        else:
            stt = 'EMP'
            if d10 == 1:
                emp = 5
            elif d10 == 2:
                emp = 6
            elif d10 == 3:
                emp = 5
            elif d10 == 4:
                emp = 6
            elif d10 == 5:
                emp = 4
            elif d10 == 6:
                emp = 5
            elif d10 == 7:
                emp = 6
            elif d10 == 8:
                emp = 4
            elif d10 == 9:
                emp = 5
            else:
                emp = 5
            #print(f'vc rolou {d10} e tem {emp} em {stt}')

    print("_" * 40)
    print(f'Seus Stats são:\nINT({int}), REF({ref}), DEX({dex}), TECH({tech}), COLL({cool})\nWILL({will}), LUCK({luck}), MOVE({move}), BODY({body}), EMP({emp})')
    print("_" * 40)
    salvararq('catalogo.txt', 'Seus Stats', '\n')
    salvararq('catalogo.txt', 'INT', int)
    salvararq('catalogo.txt', 'REF', ref)
    salvararq('catalogo.txt', 'DEX', dex)
    salvararq('catalogo.txt', 'TECH', tech)
    salvararq('catalogo.txt', 'COOL', cool)
    salvararq('catalogo.txt', 'WILL', will)
    salvararq('catalogo.txt', 'LUCK', luck)
    salvararq('catalogo.txt', 'MOVE', move)
    salvararq('catalogo.txt', 'BODY', body)
    salvararq('catalogo.txt', 'EMP', emp)
    #salvararq('catalogo.txt', '-'*40,'\n')


def roll_tabel(txt, lista):
    a = choice(lista)
    print(txt,a)
    salvararq('catalogo.txt', txt, a)

