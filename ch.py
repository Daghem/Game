#Character
import random 

class Personaggio:
    
    def __init__(self, nome, hp):
        self.nome = nome
        self.hp = hp

    def is_alive(self):
        return self.hp > 0
    
    def subisci_danno(self, danno):
        self.hp = self.hp - danno
        if self.hp < 0:
            self.hp = 0
        print(f" {self.nome} subisce {danno} danni. ({self.hp})")
    
    def set_hp(self, hp_nuovi):
        self.hp = hp_nuovi


class Giocatore(Personaggio):
    def __init__(self, nome):
        hp_random = random.randint
        super().__init__(nome, hp_random)

        print(f"Spawn {self.nome} con {self.hp} casuali.")
    
    def attacco(self, nemico):
        danno = random.randint

        print(f"{self.nome} attacca {nemico}")
        nemico.subisci_danno(danno)


class Mostro(Personaggio):
    def __init__(self):
        nome_casuale = random.randint
        hp_random = random.randint
        super().__init__(nome_casuale, hp_random)
        
        print(f"È apparso un mostro {self.nome} (HP: {self.hp})")

    def attacca(self, bersaglio):
        danno = random.randint
        
        print(f"{self.nome} ti attacca")
        bersaglio.subisci_danno(danno)


class Boss(Personaggio):
    def __init__(self):
        nome_casuale = random.randint
        hp_random = random.randint
        super().__init__(nome_casuale, hp_random)

        print(f"È apparso il boss: {self.nome} (HP: {self.hp})")
    
    def attacca(self, bersaglio):
        danno = random.randint

        print(f"{self.nome} ti ha fatto danno.")
        bersaglio.subisci_danno(danno)
