# Import libraries
from tinydb import TinyDB, Query
from random import randint
from numpy.random import choice
import numpy as np
import os
import time
import sys
import json


class TinyDbInterface:
    # Static variables
    poke_arr = []       # Used for choosing
    weights = []        # Used for assigning weights to respective poke_arr

    # Increment the pokemon count in an array
    def IncrementPokeArr(arr, pokemon):
        arr[pokemon] = arr[pokemon] + 1

        return arr

    # Decrement the pokemon count in an array
    def DecrementPokeArr(arr, pokemon):
        arr[pokemon] = arr[pokemon] - 1

        return arr

    # Convert the 'rarity' number to a probability value (0<i<1) so we can use scientific library 
    #   to pick a weighted random number/pokemon
    def ConvertToProb(arr):
        converted = []
        for i in arr:
            if arr[i] == 1:
                converted[i] = 0.40
            if arr[i] == 2:
                converted[i] = 0.20
            if arr[i] == 3:
                converted[i] = 0.15
            if arr[i] == 4:
                converted[i] = 0.10
            if arr[i] == 5:
                converted[i] = 0.05
            if arr[i] == 6:
                converted[i] = 0.02
            if arr[i] == 7:
                converted[i] = 0.02
            if arr[i] == 8:
                converted[i] = 0.01

        return converted

    def SetWeights():
        arr = []
        prob = []

        data = json.loads(open('PokemonData.json').read())

        for i in data:
            if data[i] != "{}":
                data[i]['rarity']

        prob = ConvertToProb(arr)

        return prob

        # output_file = open(fileName).read()
        # output_json = json.loads(output_file)

    # Initialize a constructor
    def __init__(self):
        self.poke_arr = array.array('i',(1 for i in range(0,10)))
        self.weights = SetWeights()


    # Add user (each user is an array of 150)
    def AddUser(username):
        my_pokemon = [0] * 152 # Matching arr index to pokemon index (0 is disregarded)

        db = TinyDB('users.json')
        db.insert({'username': username, 'pokemon': my_pokemon})
        
        pass # RETURN: check bool


    # Add pokemon to user (pokemon and quantity)
    def AddPokemon(username, pokemon):
        db = TinyDB('users.json')
        user = db.search(User.username == username)
        my_pokemon = user[0]['pokemon']
        my_pokemon_new = IncrementPokeArr(username, my_pokemon)

        db.update({'pokemon': my_pokemon_new}, Username.username == username)

        pass # RETURN: check bool

    # Remove pokemon from user
    def RemovePokemon(username, pokemon):
        db = TinyDB('users.json')
        user = db.search(User.username == username)
        my_pokemon = user[0]['pokemon']
        my_pokemon_new = DecrementPokeArr(username, my_pokemon)

        db.update({'pokemon': my_pokemon_new}, Username.username == username)

        pass # RETURN: check bool


    # Trade pokemon
    def TradePokemon(user1, user2, pokemon):
        # Add [p1]
        AddPokemon(user1, pokemon)

        # Remove
        RemovePokemon(user2, pokemon)

        # Add [p2]
        AddPokemon(user2, pokemon)
        
        # Remove
        RemovePokemon(user1, pokemon)

        pass # RETURN: check bool

    # Check pokemon quantity for one user
    def GetUserPokemon(username):

        pass # RETURN: list of pokemon and quantity List: [1] = 2 (You have 2 bulbasaurs)

    # Pick pokemon by "weighted random"
    def SpawnPokemon():
        rand_pokemon = np.random.choice(poke_arr, 1, weights) # I believe it changes on each call (check on this future brittany)

        # RETURN: Name of pokemon spawned (based on number generated by "random")
        return rand_pokemon[0] # Get the first element of the array returned
        
        




