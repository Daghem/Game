import random
import ch
import item


class World:
    def __init__(self, entities: dict, description: str, type: int, boss_name: list, enemy_name: list):
        self.entities = entities
        self.description = description
        self.type = type
        type = random.randint(1,4)
        self.boss_name = boss_name
        self.enemy_name = enemy_name
        boss_name = ["tua mamma con la ciabatta in mano", "tua nonna col mattarello", "un goblin lancere", "un politico con pensieri radicali"]
        enemy_name = ["un Demogorgone", "Pietro", "un Drago", "Sacchetto"]

    def build_random(self):
        if self.type == 1:
            self.description = "La stanza è bloccata, sembra che tu \nnon possa entrare in nessun modo"
            return (self.description)

        elif self.type == 2:
            self.description = f"C'è un boss molto pauroso di fronte a te, \nha l'aspetto di {self.boss_name[random.randint(0, len(self.boss_name)-1)]} e ti senti preso in causa."
            
            self.entities = ch.Boss.generate_boss("samuel", 100)
            return (self.description, self.entities)

        elif self.type == 3:
            self.description = "La stanza è piena di oggetti, \nforse potresti trovare qualcosa di utile qui dentro."
            return (self.description, item.Item.generate_items())

        elif self.type == 4:
            self.description = f"C'è un nemico di fronte a te, \npreparati a combattere!\nSembra si tratti di {self.enemy_name[random.randint(0, len(self.enemy_name)-1)]}."
            self.entities = ch.ch.generate_enemy()
            return (self.description, self.entities)
