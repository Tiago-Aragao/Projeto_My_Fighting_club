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
        Nível e Experiência:
        '''
        self.nivel = 1
        self.experiencia = 0
        
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
        self.lista_de_armas = [] # Será uma lista de Classes (Objetos já prontos das armas).
        self.arma_equipada = None # Será um objeto da arma equipada.
        
        # Lista de efeitos:
        self.vantagens = []
        self.buffs_ativos = []
        self.debuffs_ativos = []
        
        # Pet Padrão:
        self.pets = {
            'cachorros': None,
            'lobos': None,
            'urso': None
        }
               
        '''
        Dados Ocultos:
        '''
        # Precisão Base:
        self.precisao = 0.80 # 80%
        # Chance de bloquear o dano:
        self._taxa_bloqueio = 0.05 # chance de 5%.
        # Chance de se esquivar base:
        self._taxa_evasao = 0.02 # chance de 2%.
        # Chance de contra_atacar:
        self._taxa_contra_ataque = 0

        '''
        Modificadores de Atributo Primario e Secundario:
        '''
        # Modificadores de atributo principais:
        self.modificador_forca = 1 # Será em porcentagem.
        self.modificador_agilidade = 1 # Será em porcentagem.
        self.modificador_velocidade = 1 # Será em porcentagem.
        self.modificador_resistencia = 1 # Será em porcentagem.
        # Modificador de atributos para propriedades: 
        self.modificador_pontos_vida = 1 # Será em porcentagem.
        self.modificador_iniciativa = 1 # Será em porcentagem.
        self.modificador_armadura = 0 # Este será somado, para retornar o valor da armadura em porcentagem.
        self.modificador_evasao = 1 # Será em porcentagem.
        self.modificador_critico = 0 # Este será somado e não multiplicado.
        self.modificador_dano_critico = 1 # Será em porcentagem.
        self.modificador_contra_ataque = 1

    '''
    Propriedades da Classe Fighter:
    '''
    # Pontos de Vida:    
    @property 
    def pontos_vida(self):
        # Calcula o valor base:
        valor_base = self.resistencia * 10
        # Guarda o valor a ser alterado por vantagens:
        modificador = self.calcular_modificadores('modificador_pontos_vida')
        # Retorna o valor calculado com o aumento ou redução em porcetagem:
        return valor_base * modificador # Exemplo: 120 * 1.5 (Daria um aumento de 50% nos pontos de vida base). 
    
    @property
    def chance_critico (self):
        valor_base = self.taxa_critico
        modificadores = self.calcular_modificadores('modificador_critico')
        return valor_base * modificadores
    
    # Iniciativa:
    @property
    def iniciativa(self):
        valor_base = self.velocidade * 2
        modificadores = self.calcular_modificadores('modificador_iniciativa')
        
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
        valor_base = self._taxa_contra_ataque + (((self.agilidade + self.velocidade) / 2) * 0.01)
        modificadores = self.calcular_modificadores('modificador_contra_ataque')
    
    '''
    # Metodo para calcular Modificadores:
    '''
    def calcular_modificadores(self, modificador: str) -> float:
        '''
        Calcula o modificador percentual total para um atributo específico.
        Parâmetros:
        nome_modificador (str): nome exato do modificador, como 'modificador_forca', 
        'modificador_pontos_vida', etc.
        Retorno:
        float: multiplicador final (ex: 1.5 para +50%)
        '''

        modificador_total = float(0)

        # Soma o valor atual do próprio atributo
        if hasattr(self, modificador):
            modificador_total += getattr(self, modificador)

        # Soma das vantagens passivas
        if hasattr(self, "vantagens"):
            for vantagem in self.vantagens:
                if hasattr(vantagem, modificador):
                    modificador_total += getattr(vantagem, modificador)

        # Soma dos buffs ativos
        if hasattr(self, "buffs_ativos"):
            for buff in self.buffs_ativos:
                if hasattr(buff, modificador):
                    modificador_total += getattr(buff, modificador)

        # Soma dos debuffs ativos (valores negativos)
        if hasattr(self, "debuffs_ativos"):
            for debuff in self.debuffs_ativos:
                if hasattr(debuff, modificador):
                    modificador_total += getattr(debuff, modificador)

        # Soma de modificador da arma equipada
        if self.arma_equipada is not None:
            if hasattr(self.arma_equipada, modificador):
                modificador_total += getattr(self.arma_equipada, modificador)

        # Retorna o valor final multiplicativo
        return 1 + modificador_total

    '''
    # Metodos de uso no combate:
    '''
    # Metodo para causar dano:
    def dano (self, arma):
        if self.arma_equipada == None:
            return 5 + self.forca
        else:
            return self.arma_equipada.dano + self.forca
    
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
    
    