### Overview
<p>
    This is a small project intended to get back into the python mindset
    <br>
    I aim to create pokemon with abilities 
    <br>
    Be able to evolve pokemon to new states 
    <br>
    Use pokemon abilities
    <br>
</p>

### Setup
<p>
    Using python v 3.13.0 in a virtual enviornment
    <br>
    No 3rd party lib are used
    <br>
    Run main.py to execute the application
</p>

### Quick Notes
<p>
    If this was going to be a game, there would be a game engine insted of a hard coded main function
    <br><br>
    The bulk of the work is in the fallowing classes / scripts:
    <li>domain/pokemon.py</li>
    <li>domain/helper_sripts/evolve_pokemon_with_data.py</li>
    <li>domain/helper_sripts/execute_ability.py</li>
    <li>domain/helper_scripts/deal_damage.py</li>
    <br><br>
    There are some half emplamented ideas here and there but the stated goals should all be there
</p>

### What is Pokemon, what is going on and how are we doing !TLDR :D
<p>
    Pokemon is a TCG where character entities are used to battle, they start out in evolution state 0 and can go up to state 4 in cases in a sequential mannor. 
    <br><br>
    In this app we represent fully created pokemon via json files in json/base_pokemon_data. This represents their base stats and data as well as abilities they can use in battle.
    <br><br>
    We represent evolution states with json files in json/evolution_data. These json files represent a pokemon that they can evolve (The id of the pokemon) as well as all the changes / additions the pokemon will incure when it evolves. This includes increasing stats, upgrading existing abilities and adding new abilities.
    <br><br>
    Once we have created multiple pokemon they can interact with eachother by using their abilities on one another. 
    <br><br>
    All relevent information happening in the sudo game is logged via the Game log singleton object (domain/game_log.py)
</p>