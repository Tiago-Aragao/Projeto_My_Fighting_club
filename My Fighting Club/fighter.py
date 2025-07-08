# Accuracy
# Armor
# Block
# Combo
# Counter ()
# Critical_Chance ()
# Critical_Damage ()
# Deflect ()
# Dexterity ()
# Disarm ()
# Evavion ()
# HitSpeed ()
# Initiative ()
# Reversal ()

# Importação:
import random

# Onde ficará os lutadores:
class Fighter:
    '''
    Esta é a classe Fighter que irá conter todos os atributos principais dos combatentes,
    mais a frente terá uma função que recebe 2 Fighters como parametro e executa o combate.
    '''
    def __init__(self, nome:str) -> None:
        '''
        Metodo construtor que recebe como parametro apenas o nome. O resto é definido aleatoriamente
        pelo sistema de criação de ficha.
        '''
        # Atributo básico:
        self.nome = nome # Atributo Nome do tipo str (String).
        
        # Atributos Principais Visiveis para o jogador:
        self.forca = 2 # Influencia no dano dos ataques.
        self.agilidade = 2 # Influencia no combo e na dodge chance
        self.velocidade = 2 # Influencia no hit_speed
        # Atributo Principal não visivel:
        self.resistencia = random.randint(7,12)
        
        # Modificadores de atributo:
        self.mod_forca = 1 # 100%
        self.mod_agilidade = 1 # 100%
        self.mod_velocidade = 1 # 100% 
        # Arma padrão:
        self.arma = None
        
        # Dados Ocultos:
        
        # Accuracy Padrão:
        self.accuracy = 0.80 # 80%
        # Armadura (Redução de Dano):
        self.armor = 0 # 0%
        # Block Chance (Chance de bloquear o dano):
        self.block_chance = 0.05 # chance de 5%.

    # Propriedades:
    
    # Pontos de Vida:    
    @property 
    def pontos_vida(self):
        return (self.resistencia * 10)
    
    # Iniciativa:
    @property
    def iniciativa(self):
        return self.velocidade * 2
    
    @property
    def dano (self, arma=None):
        if arma == None:
            return 5 + self.forca
        else:
            return arma.dano + self.forca
    
    @property
    def iniciativa(self):
        return self.velocidade * 2

    @property
    def block_chance(self):
        return 0.05 + (0.01 * self.forca) 
    # Metodos de combate:
    
    # Metodo para atacar:
    
        
    # Bloquear ataque: Ignora 90% do dano.
    def bloquear(self, dano):
        return dano * 0.1 # Bloqueia 90% do dano.
        
    # Esquivar: Ignora 100% do dano.
    def esquivar(self, dano):
        dano = 0 # ignora 100% do dano.
        return dano
    
    def defleccao (self, dano):
        pass
    
    def contra_ataque():
        pass
    
    