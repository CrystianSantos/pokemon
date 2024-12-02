from mysql.connector import connect
from os import path


SEPARADOR = '\\'
endereco = path.dirname(path.realpath(__file__)).removesuffix('model') + 'assets' + SEPARADOR + 'fotos_pokemons' + SEPARADOR
print(endereco)
pokemons = [
    [1, 'Bulbassauro', 'Grama', 'Venenoso', endereco + '1.png', 5, 5, 5, 'descrição'],
    [2, 'Ivyssauro', 'Grama', 'Venenoso', endereco + '2.png', 5, 5, 5, 'descrição'],
    [3, 'Venussauro', 'Grama', 'Venenoso', endereco + '3.png', 5, 5, 5, 'descrição'],
    [4, 'Charmander', 'Fogo', 'NULL', endereco + '4.png', 5, 5, 5, 'descrição'],
    [5, 'Charmeleon', 'Fogo', 'NULL', endereco + '5.png', 5, 5, 5, 'descrição'],
    [6, 'Charizard', 'Fogo', 'Voador', endereco + '6.png', 5, 5, 5, 'descrição'],
    [7, 'Squirtle', 'Água', 'NULL', endereco + '7.png', 5, 5, 5, 'descrição'],
    [8, 'Wartortle', 'Água', 'NULL', endereco + '8.png', 5, 5, 5, 'descrição'],
    [9, 'Blastoise', 'Água', 'NULL', endereco + '9.png', 5, 5, 5, 'descrição'],
    [10, 'Caterpie', 'Inseto', 'NULL', endereco + '10.png', 5, 5, 5, 'descrição'],
    [11, 'Metapod', 'Inseto', 'NULL', endereco + '11.png', 5, 5, 5, 'descrição'],
    [12, 'Butterfree', 'Inseto', 'Voador', endereco + '12.png', 5, 5, 5, 'descrição'],
    [13, 'Weedle', 'Inseto', 'Venenoso', endereco + '13.png', 5, 5, 5, 'descrição'],
    [14, 'Kakuna', 'Inseto', 'Venenoso', endereco + '14.png', 5, 5, 5, 'descrição'],
    [15, 'Beedrill', 'Inseto', 'Venenoso', endereco + '15.png', 5, 5, 5, 'descrição'],
    [16, 'Pidgey', 'Normal', 'Voador', endereco + '16.png', 5, 5, 5, 'descrição'],
    [17, 'Pidgeotto', 'Normal', 'Voador', endereco + '17.png', 5, 5, 5, 'descrição'],
    [18, 'Pidgeot', 'Normal', 'Voador', endereco + '18.png', 5, 5, 5, 'descrição'],
    [19, 'Rattata', 'Normal', 'NULL', endereco + '19.png', 5, 5, 5, 'descrição'],
    [20, 'Raticate', 'Normal', 'NULL', endereco + '20.png', 5, 5, 5, 'descrição'],
    [21, 'Spearow', 'Normal', 'Voador', endereco + '21.png', 5, 5, 5, 'descrição'],
    [22, 'Fearow', 'Normal', 'Voador', endereco + '22.png', 5, 5, 5, 'descrição'],
    [23, 'Ekans', 'Venenoso', 'NULL', endereco + '23.png', 5, 5, 5, 'descrição'],
    [24, 'Arbok', 'Venenoso', 'NULL', endereco + '24.png', 5, 5, 5, 'descrição'],
    [25, 'Pikachu', 'Elétrico', 'NULL', endereco + '25.png', 5, 5, 5, 'descrição'],
    [26, 'Raichu', 'Elétrico', 'NULL', endereco + '26.png', 5, 5, 5, 'descrição'],
    [27, 'Sandshrew', 'Terrestre', 'NULL', endereco + '27.png', 5, 5, 5, 'descrição'],
    [28, 'Sandslash', 'Terrestre', 'NULL', endereco + '28.png', 5, 5, 5, 'descrição'],
    [29, 'NidoranF', 'Venenoso', 'NULL', endereco + '29.png', 5, 5, 5, 'descrição'],
    [30, 'Nidorina', 'Venenoso', 'NULL', endereco + '30.png', 5, 5, 5, 'descrição'],
    [31, 'Nidoqueen', 'Venenoso', 'Terrestre', endereco + '31.png', 5, 5, 5, 'descrição'],
    [32, 'NidoranM', 'Venenoso', 'NULL', endereco + '32.png', 5, 5, 5, 'descrição'],
    [33, 'Nidorino', 'Venenoso', 'NULL', endereco + '33.png', 5, 5, 5, 'descrição'],
    [34, 'Nidoking', 'Venenoso', 'Terrestre', endereco + '34.png', 5, 5, 5, 'descrição'],
    [35, 'Clefairy', 'Fada', 'NULL', endereco + '35.png', 5, 5, 5, 'descrição'],
    [36, 'Clefable', 'Fada', 'NULL', endereco + '36.png', 5, 5, 5, 'descrição'],
    [37, 'Vulpix', 'Fogo', 'NULL', endereco + '37.png', 5, 5, 5, 'descrição'],
    [38, 'Ninetales', 'Fogo', 'NULL', endereco + '38.png', 5, 5, 5, 'descrição'],
    [39, 'Jigglypuff', 'Normal', 'Fada', endereco + '39.png', 5, 5, 5, 'descrição'],
    [40, 'Wigglytuff', 'Normal', 'Fada', endereco + '40.png', 5, 5, 5, 'descrição'],
    [41, 'Zubat', 'Venenoso', 'Voador', endereco + '41.png', 5, 5, 5, 'descrição'],
    [42, 'Golbat', 'Venenoso', 'Voador', endereco + '42.png', 5, 5, 5, 'descrição'],
    [43, 'Oddish', 'Grama', 'Venenoso', endereco + '43.png', 5, 5, 5, 'descrição'],
    [44, 'Gloom', 'Grama', 'Venenoso', endereco + '44.png', 5, 5, 5, 'descrição'],
    [45, 'Vileplume', 'Grama', 'Venenoso', endereco + '45.png', 5, 5, 5, 'descrição'],
    [46, 'Paras', 'Inseto', 'Grama', endereco + '46.png', 5, 5, 5, 'descrição'],
    [47, 'Parasect', 'Inseto', 'Grama', endereco + '47.png', 5, 5, 5, 'descrição'],
    [48, 'Venonat', 'Inseto', 'Venenoso', endereco + '48.png', 5, 5, 5, 'descrição'],
    [49, 'Venomoth', 'Inseto', 'Venenoso', endereco + '49.png', 5, 5, 5, 'descrição'],
    [50, 'Diglett', 'Terrestre', 'NULL', endereco + '50.png', 5, 5, 5, 'descrição'],
    [51, 'Dugtrio', 'Terrestre', 'NULL', endereco + '51.png', 5, 5, 5, 'descrição'],
    [52, 'Meowth', 'Normal', 'NULL', endereco + '52.png', 5, 5, 5, 'descrição'],
    [53, 'Persian', 'Normal', 'NULL', endereco + '53.png', 5, 5, 5, 'descrição'],
    [54, 'Psyduck', 'Água', 'NULL', endereco + '54.png', 5, 5, 5, 'descrição'],
    [55, 'Golduck', 'Água', 'NULL', endereco + '55.png', 5, 5, 5, 'descrição'],
    [56, 'Mankey', 'Lutador', 'NULL', endereco + '56.png', 5, 5, 5, 'descrição'],
    [57, 'Primeape', 'Lutador', 'NULL', endereco + '57.png', 5, 5, 5, 'descrição'],
    [58, 'Growlithe', 'Fogo', 'NULL', endereco + '58.png', 5, 5, 5, 'descrição'],
    [59, 'Arcanine', 'Fogo', 'NULL', endereco + '59.png', 5, 5, 5, 'descrição'],
    [60, 'Poliwag', 'Água', 'NULL', endereco + '60.png', 5, 5, 5, 'descrição'],
    [61, 'Poliwhirl', 'Água', 'NULL', endereco + '61.png', 5, 5, 5, 'descrição'],
    [62, 'Poliwrath', 'Água', 'Lutador', endereco + '62.png', 5, 5, 5, 'descrição'],
    [63, 'Abra', 'Psíquico', 'NULL', endereco + '63.png', 5, 5, 5, 'descrição'],
    [64, 'Kadabra', 'Psíquico', 'NULL', endereco + '64.png', 5, 5, 5, 'descrição'],
    [65, 'Alakazam', 'Psíquico', 'NULL', endereco + '65.png', 5, 5, 5, 'descrição'],
    [66, 'Machop', 'Lutador', 'NULL', endereco + '66.png', 5, 5, 5, 'descrição'],
    [67, 'Machoke', 'Lutador', 'NULL', endereco + '67.png', 5, 5, 5, 'descrição'],
    [68, 'Machamp', 'Lutador', 'NULL', endereco + '68.png', 5, 5, 5, 'descrição'],
    [69, 'Bellsprout', 'Grama', 'Venenoso', endereco + '69.png', 5, 5, 5, 'descrição'],
    [70, 'Weepinbell', 'Grama', 'Venenoso', endereco + '70.png', 5, 5, 5, 'descrição'],
    [71, 'Victreebel', 'Grama', 'Venenoso', endereco + '71.png', 5, 5, 5, 'descrição'],
    [72, 'Tentacool', 'Água', 'Venenoso', endereco + '72.png', 5, 5, 5, 'descrição'],
    [73, 'Tentacruel', 'Água', 'Venenoso', endereco + '73.png', 5, 5, 5, 'descrição'],
    [74, 'Geodude', 'Pedra', 'Terrestre', endereco + '74.png', 5, 5, 5, 'descrição'],
    [75, 'Graveler', 'Pedra', 'Terrestre', endereco + '75.png', 5, 5, 5, 'descrição'],
    [76, 'Golem', 'Pedra', 'Terrestre', endereco + '76.png', 5, 5, 5, 'descrição'],
    [77, 'Ponyta', 'Fogo', 'NULL', endereco + '77.png', 5, 5, 5, 'descrição'],
    [78, 'Rapidash', 'Fogo', 'NULL', endereco + '78.png', 5, 5, 5, 'descrição'],
    [79, 'Slowpoke', 'Água', 'Psíquico', endereco + '79.png', 5, 5, 5, 'descrição'],
    [80, 'Slowbro', 'Água', 'Psíquico', endereco + '80.png', 5, 5, 5, 'descrição'],
    [81, 'Magnemite', 'Elétrico', 'Aço', endereco + '81.png', 5, 5, 5, 'descrição'],
    [82, 'Magneton', 'Elétrico', 'Aço', endereco + '82.png', 5, 5, 5, 'descrição'],
    [83, "Farfetch'd", 'Normal', 'Voador', endereco + '83.png', 5, 5, 5, 'descrição'],
    [84, 'Doduo', 'Normal', 'Voador', endereco + '84.png', 5, 5, 5, 'descrição'],
    [85, 'Dodrio', 'Normal', 'Voador', endereco + '85.png', 5, 5, 5, 'descrição'],
    [86, 'Seel', 'Água', 'NULL', endereco + '86.png', 5, 5, 5, 'descrição'],
    [87, 'Dewgong', 'Água', 'Gelo', endereco + '87.png', 5, 5, 5, 'descrição'],
    [88, 'Grimer', 'Venenoso', 'NULL', endereco + '88.png', 5, 5, 5, 'descrição'],
    [89, 'Muk', 'Venenoso', 'NULL', endereco + '89.png', 5, 5, 5, 'descrição'],
    [90, 'Shellder', 'Água', 'NULL', endereco + '90.png', 5, 5, 5, 'descrição'],
    [91, 'Cloyster', 'Água', 'Gelo', endereco + '91.png', 5, 5, 5, 'descrição'],
    [92, 'Gastly', 'Fantasma', 'Venenoso', endereco + '92.png', 5, 5, 5, 'descrição'],
    [93, 'Haunter', 'Fantasma', 'Venenoso', endereco + '93.png', 5, 5, 5, 'descrição'],
    [94, 'Gengar', 'Fantasma', 'Venenoso', endereco + '94.png', 5, 5, 5, 'descrição'],
    [95, 'Onix', 'Pedra', 'Terrestre', endereco + '95.png', 5, 5, 5, 'descrição'],
    [96, 'Drowzee', 'Psíquico', 'NULL', endereco + '96.png', 5, 5, 5, 'descrição'],
    [97, 'Hypno', 'Psíquico', 'NULL', endereco + '97.png', 5, 5, 5, 'descrição'],
    [98, 'Krabby', 'Água', 'NULL', endereco + '98.png', 5, 5, 5, 'descrição'],
    [99, 'Kingler', 'Água', 'NULL', endereco + '99.png', 5, 5, 5, 'descrição'],
    [100, 'Voltorb', 'Elétrico', 'NULL', endereco + '100.png', 5, 5, 5, 'descrição'],
    [101, 'Electrode', 'Elétrico', 'NULL', endereco + '101.png', 5, 5, 5, 'descrição'],
    [102, 'Exeggcute', 'Grama', 'Psíquico', endereco + '102.png', 5, 5, 5, 'descrição'],
    [103, 'Exeggutor', 'Grama', 'Psíquico', endereco + '103.png', 5, 5, 5, 'descrição'],
    [104, 'Cubone', 'Terrestre', 'NULL', endereco + '104.png', 5, 5, 5, 'descrição'],
    [105, 'Marowak', 'Terrestre', 'NULL', endereco + '105.png', 5, 5, 5, 'descrição'],
    [106, 'Hitmonlee', 'Lutador', 'NULL', endereco + '106.png', 5, 5, 5, 'descrição'],
    [107, 'Hitmonchan', 'Lutador', 'NULL', endereco + '107.png', 5, 5, 5, 'descrição'],
    [108, 'Lickitung', 'Normal', 'NULL', endereco + '108.png', 5, 5, 5, 'descrição'],
    [109, 'Koffing', 'Venenoso', 'NULL', endereco + '109.png', 5, 5, 5, 'descrição'],
    [110, 'Weezing', 'Venenoso', 'NULL', endereco + '110.png', 5, 5, 5, 'descrição'],
    [111, 'Rhyhorn', 'Terrestre', 'Pedra', endereco + '111.png', 5, 5, 5, 'descrição'],
    [112, 'Rhydon', 'Terrestre', 'Pedra', endereco + '112.png', 5, 5, 5, 'descrição'],
    [113, 'Chansey', 'Normal', 'NULL', endereco + '113.png', 5, 5, 5, 'descrição'],
    [114, 'Tangela', 'Grama', 'NULL', endereco + '114.png', 5, 5, 5, 'descrição'],
    [115, 'Kangaskhan', 'Normal', 'NULL', endereco + '115.png', 5, 5, 5, 'descrição'],
    [116, 'Horsea', 'Água', 'NULL', endereco + '116.png', 5, 5, 5, 'descrição'],
    [117, 'Seadra', 'Água', 'NULL', endereco + '117.png', 5, 5, 5, 'descrição'],
    [118, 'Goldeen', 'Água', 'NULL', endereco + '118.png', 5, 5, 5, 'descrição'],
    [119, 'Seaking', 'Água', 'NULL', endereco + '119.png', 5, 5, 5, 'descrição'],
    [120, 'Staryu', 'Água', 'NULL', endereco + '120.png', 5, 5, 5, 'descrição'],
    [121, 'Starmie', 'Água', 'Psíquico', endereco + '121.png', 5, 5, 5, 'descrição'],
    [122, 'Mr. Mime', 'Psíquico', 'Fada', endereco + '122.png', 5, 5, 5, 'descrição'],
    [123, 'Scyther', 'Inseto', 'Voador', endereco + '123.png', 5, 5, 5, 'descrição'],
    [124, 'Jynx', 'Gelo', 'Psíquico', endereco + '124.png', 5, 5, 5, 'descrição'],
    [125, 'Electabuzz', 'Elétrico', 'NULL', endereco + '125.png', 5, 5, 5, 'descrição'],
    [126, 'Magmar', 'Fogo', 'NULL', endereco + '126.png', 5, 5, 5, 'descrição'],
    [127, 'Pinsir', 'Inseto', 'NULL', endereco + '127.png', 5, 5, 5, 'descrição'],
    [128, 'Tauros', 'Normal', 'NULL', endereco + '128.png', 5, 5, 5, 'descrição'],
    [129, 'Magikarp', 'Água', 'NULL', endereco + '129.png', 5, 5, 5, 'descrição'],
    [130, 'Gyarados', 'Água', 'Voador', endereco + '130.png', 5, 5, 5, 'descrição'],
    [131, 'Lapras', 'Água', 'Gelo', endereco + '131.png', 5, 5, 5, 'descrição'],
    [132, 'Ditto', 'Normal', 'NULL', endereco + '132.png', 5, 5, 5, 'descrição'],
    [133, 'Eevee', 'Normal', 'NULL', endereco + '133.png', 5, 5, 5, 'descrição'],
    [134, 'Vaporeon', 'Água', 'NULL', endereco + '134.png', 5, 5, 5, 'descrição'],
    [135, 'Jolteon', 'Elétrico', 'NULL', endereco + '135.png', 5, 5, 5, 'descrição'],
    [136, 'Flareon', 'Fogo', 'NULL', endereco + '136.png', 5, 5, 5, 'descrição'],
    [137, 'Porygon', 'Normal', 'NULL', endereco + '137.png', 5, 5, 5, 'descrição'],
    [138, 'Omanyte', 'Pedra', 'Água', endereco + '138.png', 5, 5, 5, 'descrição'],
    [139, 'Omastar', 'Pedra', 'Água', endereco + '139.png', 5, 5, 5, 'descrição'],
    [140, 'Kabuto', 'Pedra', 'Água', endereco + '140.png', 5, 5, 5, 'descrição'],
    [141, 'Kabutops', 'Pedra', 'Água', endereco + '141.png', 5, 5, 5, 'descrição'],
    [142, 'Aerodactyl', 'Pedra', 'Voador', endereco + '142.png', 5, 5, 5, 'descrição'],
    [143, 'Snorlax', 'Normal', 'NULL', endereco + '143.png', 5, 5, 5, 'descrição'],
    [144, 'Articuno', 'Gelo', 'Voador', endereco + '144.png', 5, 5, 5, 'descrição'],
    [145, 'Zapdos', 'Elétrico', 'Voador', endereco + '145.png', 5, 5, 5, 'descrição'],
    [146, 'Moltres', 'Fogo', 'Voador', endereco + '146.png', 5, 5, 5, 'descrição'],
    [147, 'Dratini', 'Dragão', 'NULL', endereco + '147.png', 5, 5, 5, 'descrição'],
    [148, 'Dragonair', 'Dragão', 'NULL', endereco + '148.png', 5, 5, 5, 'descrição'],
    [149, 'Dragonite', 'Dragão', 'Voador', endereco + '149.png', 5, 5, 5, 'descrição'],
    [150, 'Mewtwo', 'Psíquico', 'NULL', endereco + '150.png', 5, 5, 5, 'descrição'],
    [151, 'Mew', 'Psíquico', 'NULL', endereco + '151.png', 5, 5, 5, 'descrição']
]

banco = connect(
  host="localhost",
  user="root",
  password="",
  database="Pokedex"
)
cursor = banco.cursor()
for pokemon in pokemons:
    pokemon = tuple(pokemon)
    cursor.execute('insert into tb_pokemons (id, nome, tipo_1, tipo_2, foto, ataque, defesa, hp, descrição) values (%s, %s, %s, %s, %s, %s, %s, %s, %s);', pokemon)
banco.commit()
cursor.close()
banco.close()
