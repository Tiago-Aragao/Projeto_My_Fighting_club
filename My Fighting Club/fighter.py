# Accuracy - Feito a parte base.
# Armor - Feita a armor base.
# Evavion - FEITO
# Critical Chance - 
# Critical Damage -

# Block Chance - FEITO
# Combo Chance - FEITO
# Counter Chance
# Deflect chance
# Disarm chance
# Reversal Chance

# HitSpeed
# Initiative

# Importação:
import random

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
        
        '''
        Atributos e Informações Básicas:
        '''
        self.nome = nome
        
        # Atributos Principais Visiveis do Fighter:
        self.forca = 2
        self.agilidade = 2
        self.velocidade = 2
        # Atributo Principal não visivel:
        self.resistencia = random.randint(7,12)
                
        '''
        Atributos Secundarios Visiveis:
        '''
        self.taxa_critico = 0.05 # 5%.
        self.multiplicador_dano_critico = 1.5 # Aumento de 50% no dano.
        
        '''
        Lista de Armas e Pets do Fighter:
        '''
        # Arma padrão:
        self.lista_de_armas = []
        self.arma_equipada = None
        
        # Pet Padrão:
        self.pets = {
            'cachorros': None,
            'lobos': None,
            'urso': None
        }
        
        # Modificadores de atributo principais:
        self.modificador_forca = 1 # 100%
        self.modificador_agilidade = 1 # 100%
        self.modificador_velocidade = 1 # 100%
        self.modificador_resistencia = 1 #
        # Modificador de atributos para propriedades: 
        self.modificador_pontos_vida = 1 # 100%
        self.modificador_iniciativa = 1 #
        self.modificador_armadura = 1 #
        self.modificador_evasao = 1 #
        
        
        '''
        Dados Ocultos:
        '''
        # Precisão Base:
        self.precisao = 0.80 # 80%
        # Chance de bloquear o dano:
        self._taxa_bloqueio = 0.05 # chance de 5%.
        # Chance de se esquivar base:
        self._taxa_evasao = 0.02 # chance de 2%.

    '''
    Propriedades da Classe Fighter:
    '''
    # Pontos de Vida:    
    @property 
    def pontos_vida(self):
        # Calcula o valor base:
        valor_base = self.resistencia * 10
        # Guarda o valor a ser alterado por vantagens:
        vantagens = self.mod_pontos_vida
        # Retorna o valor calculado com o aumento ou redução em porcetagem:
        return valor_base * vantagens # Exemplo: 120 * 1.5 (Daria um aumento de 50% nos pontos de vida base). 
    
    # Iniciativa:
    @property
    def iniciativa(self):
        valor_base = self.velocidade * 2
        
    # Chance de Bloquear:
    @property
    def chance_bloqueio (self):
        return self._taxa_bloqueio + (0.01 * self.forca)
    
    # Chance de Esquivar:
    @property
    def chance_evasao (self):
        return self._taxa_evasao + (0.01 * self.agilidade)
    
    # Chance de Combo:
    @property
    def chance_combo (self):
        return self.agilidade * 0.01
    
    # Chance de contra_ataque:
    @property
    def chance_contra_ataque (self):
        return ((self.agilidade + self.velocidade) / 2 ) * 0.01 
    
    '''
    # Metodos de uso no combate:
    '''
    # Metodo para causar dano:
    def dano (self, arma):
        if not arma:
            return 5 + self.forca
        else:
            return arma.dano + self.forca
    
    # Metodo para atacar:
    def atacar(self):
        pass 
        
    # Bloquear ataque: Ignora 90% do dano.
    def bloquear (self, dano):
        return dano * 0.1 # Bloqueia 90% do dano.
        
    # Esquivar: Ignora 100% do dano.
    def esquivar (self, dano):
        dano = 0 # ignora 100% do dano.
        return dano
    
    def deflaxao (self, dano):
        pass
    
    def contra_ataque(self):
        pass
    
    