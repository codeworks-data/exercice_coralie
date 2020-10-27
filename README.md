# Kata Python Number one

## Context and objectives 

This assignment comes in a context of evaluating the technical proficiency in Python of a developer.

The goals of the assignment to produce a solution with:
* A good POO design that reflects the assignment requirements and constraints
* A good quality code 
* A minimum tests on solutions components

## Assignment statement(in french)


« Il faut créer une application pour aider le Père Noël à gérer l’usine de cadeaux pour décembre. Elle est à faire en plusieurs étapes :<br/>
1. Empaqueter les cadeaux
    1. Les cadeaux peuvent être de 3 types :
        1. Petit : il pèse 1kg et met 0.5 seconde à être préparé
        2. Moyen : il pèse 2kg et met 1 seconde à être préparé
        3. Gros : il pèse 5kg et met 2 secondes à être préparé
    2. On dispose d’un stock illimité de cadeaux (c’est le Père Noël, après tout…)
    3. Sur demande, on peut demander à un nain d’empaqueter n’importe quel type de cadeau. Il doit prendre alors le temps nécessaire pour y arriver.
2. Déposer les cadeaux sur le traîneau
    1. Une fois que le cadeau demandé par le nain est préparé, il est placé dans le traîneau, tiré par des rennes.
    2. Le traîneau peut contenir jusqu’à 12kg de cadeau (pas un gramme de plus ! sinon les rennes font grève…). Quand il est plein, le nain refuse de travailler pour rien et n’accepte plus de s’occuper de nouveaux cadeaux.
3. Envoyer les rennes livrer les cadeaux
    1. Les rennes livrent le contenu du traîneau sur demande, tant que celui-ci n’est pas vide.
    2. Elles mettent 0.5 seconde par paquet dans le traîneau (peu importe le poids). Inutile de spécifier une destination : les rennes savent où aller, c’est magique !
    3. Le problème avec les rennes, c’est qu’ils sont stupides : 1 fois sur 5, quand on leur demande de partir, ils refusent parce qu’ils « ont faim »… Dans ce cas-là, il faut juste le leur redemander jusqu’à ce qu’ils partent (ils sont vraiment stupides…)
    4. Quand les rennes sont partis, le nain refuse de travailler car il n’y a plus de traîneau$

Vous avez libre choix concernant le type d’application (console, client lourd, client léger), les technologies utilisées et sur l’ergonomie en général. Faites juste en sorte que votre application soit utilisable par un être humain et que tout ce qu’il se passe dans l’usine soit le plus lisible possible !
Le père noel n'a qu'un traineau, et un seul nain (il a du licencier avec la covid, et y'en a un paquet qui ont pris leurs rtt ... ) 

## Solution explanation (Top-down)

### Main 
The main only receives the number of presents as an argument.
Instantiate a Santa class, a queue of presents then is created.
Ask the Stanta instance to distributre it's presents

### Santa Class
Santa class<br/>
When instantiated, the Santa class create a random queue of 'n' presents, and instantiate an elf (to wrap presents)
When asked to distribute presents, the santa instance, for each present in the queue:
    1. extract the first present from the queue
    2. ask the elf if it's possible to add it to the queue.
    If possible, ask the elf to wrap it and add it to the queue
    3. If the present can't be added or it's end of the queue, deliver the sled by:
        1. Notify the elf that the work is done
        2. Get the sled from the elf
        3. Ask reindeers to deliver presents, (re-ask if negative answer)
        
### Elf class
The elf instance, instantiate a sled to fill, can check if the sled is it possible to add another present to the sled,<br/>
wrap a present and add it to the sled, return a sled when asked (when filled)

### Sled class
The sled instance, gives methods: to check the possibility to add another present to the sled<br/>
to add or remove a present from the sled

### Reindeer class
The reindeer instance take a sled and deliver it's presents (one by one).

## Install package 
```$ pip install .```
## Run App 
```$ python src/presents_distributing_lib/main.py [--n-presents N]```<br/>
(default value for N is 20)
## Unit Testing 
```$ cd tests && python -m unittest```
