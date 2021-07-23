import random
print("This is a Pokemon Guesser\n")
starting=int(input("Please select your prefered level.\n1.Easy(10lives)\n2.Novice(7Lives)\n3.Hard(5lives)\n4.Hell(2lives)\nPlease select your prefered option as (1),(2),(3)or(4)\n"))
lives=0
if starting==1:
    lives=10
elif starting==2:
    lives=7
elif starting==3:
    lives=5
elif starting==4:
    lives=2
else:
    print("Please Restart\n")
game=False
while not game:
 pokemon=("Bulbasaur,Ivysaur,Venusaur,Charmander,Charmeleon,Charizard,Squirtle,Wartortle,Blastoise,Caterpie,Metapod,Butterfree,Weedle,Kakuna,Beedrill,Pidgey,Pidgeotto,Pidgeot,Rattata,Raticate,Spearow,Fearow,Ekans,Arbok,Pikachu,Raichu,Sandshrew,Sandslash,Nidoran,Nidorina,Nidoqueen,Nidorino,Nidoking,Clefairy,Clefable,Vulpix,Ninetales,Jigglypuff,Wigglytuff,Zubat,Golbat,Oddish,Gloom,Vileplume,Paras,Parasect,Venonat,Venomoth,Diglett,Dugtrio,Meowth,Persian,Psyduck,Golduck,Mankey,Primeape,Growlithe,Arcanine,Poliwag,Poliwhirl,Poliwrath,Abra,Kadabra,Alakazam,Machop,Machoke,Machamp,Bellsprout,Weepinbell,Victreebel,Tentacool,Tentacruel,Geodude,Graveler,Golem,Ponyta,Rapidash,Slowpoke,Slowbro,Magnemite,Magneton,Farfetchd,Doduo,Dodrio,Seel,Dewgong,Grimer,Muk,Shellder,Cloyster,Gastly,Haunter,Gengar,Onix,Drowzee,Hypno,Krabby,Kingler,Voltorb,Electrode,Exeggcute,Exeggutor,Cubone,Marowak,Hitmonlee,Hitmonchan,Lickitung,Koffing,Weezing,Rhyhorn,Rhydon,Chansey,Tangela,Kangaskhan,Horsea,Seadra,Goldeen,Seaking,Staryu,Starmie,Mr.Mime,Scyther,Jynx,Electabuzz,Magmar,Pinsir,Tauros,Magikarp,Gyarados,Lapras,Ditto,Eevee,Vaporeon,Jolteon,Flareon,Porygon,Omanyte,Omastar,Kabuto,Kabutops,Aerodactyl,Snorlax,Articuno,Zapdos,Moltres,Dratini,Dragonair,Dragonite,Mewtwo,Mew").lower()
 pokemon_list=pokemon.split(",")
 word=random.choice(pokemon_list)
 no_of_word=int(len(word))
 word_list=list(word)
 display=[]
 for char in word :
     display+='_'
 end=False
 Input_list=[]
 while not end:
      print(display)
      Input = input("\nPlease give a word.\n").lower()
      for position in range(no_of_word):
        letter=word[position]
        if letter == Input:
              if letter in Input_list and letter not in word_list :
                  print("Guess Invalid\n")
              else:
               print("\nYour Guess is Correct\n")
               Input_list.append(Input)
               word_list.remove(Input)
               display[position]=letter
      if Input not in word:
        lives=lives-1
        print(f"Your Guess is wrong.\nNumber of lives left{lives}\n")
        if lives<=0:
          print(f"You Lose.\nThe answer is {word}\n")
          word_list.clear()
          end=True
          last = input("Want to continue (y) or (n)\n")
          if last == "n":
              game = True
          else:
              starting = int(input(
                  "Please select your prefered level.\n1.Easy(10lives)\n2.Novice(7Lives)\n3.Hard(5lives)\n4.Hell(2lives)\nPlease select your prefered option as (1),(2),(3)or(4)\n"))
              lives = 0
              if starting == 1:
                  lives = 10
              elif starting == 2:
                  lives = 7
              elif starting == 3:
                  lives = 5
              elif starting == 4:
                  lives = 2
              else:
                  print("Please Restart\n")
      if"_"not in display:
        end=True
        print("You Win\n")
        word_list.clear()
        last=input("Want to continue (y) or (n)\n")
        if last=="n":
         game=True




