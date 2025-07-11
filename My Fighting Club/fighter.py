# Importação:
import random



class Fighter:
    '''
    Esta é a classe Fighter que irá conter todos os atributos principais dos combatentes,
    mais a frente terá uma função que recebe 2 Fighters como parametro e executa o combate.
    ESTÁ CLASSE SERÀ COMPLETAMENTE REFATORADA PARA MONTAR CLASSES MENORES E AUXILIARES DA CLASSE FIGHTER,
    ONDE ELA IRÁ MANTER APENAS O BÁSICO PARA ESTRUTURA DO FIGHTER EM QUESTÃO.
    MAS ANTES PRECISO FINALIZAR ELA PARA SABER O QUE NECESSARIAMENTE IRÁ PRECISAR DE REFATORAÇÃO.
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
        self.multiplicador_dano_critico = 1.5 # Aumento de 50% base no dano.
        
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
        self.pets = [] # Lista de objetos pets que o lutador poderá ter.

        '''
        Dados Ocultos:
        Todos as taxas e dados abaixo são representados por um valor
        em porcentagem sendo o 0.01 -> 1% e o 1 -> 100%.
        '''

        # Armadura Base:
        ''' Atributo armadura será um percentual que irá reduzir diretamente 
        o dano recebido, após todos os modificadores e manobras
        Ex: Dano = 15 Armadura = 0.08 (8%) -> Dano = 13.8'''
        self._armadura = 0 # Será calculado em porcentagem.
        # Precisão Base:
        ''' Precisão será o atributo base para acertar o antagonista direto da 
        evasão e da reflexão'''
        self._precisao = 0.80 # Valor base se inicia em 80% e é aumentado pelo valor de agilidade.
        # Chance de bloquear o dano:
        '''A taxa de bloqueio é o atributo que determina a chance base padrão para se bloquear
        um ataque, este valor será usando no calculo da propriedade bloqueio que irá retornar
        valor real de bloqueio do Fighter.
        Ao bloquear um ataque o Fighter recebe apenas 10% do dano real do ataque que ainda será reduzido
        pela Armadura
        Ex: Dano = 100 -> Após bloqueado Dano = 10 -> Após Armadura = 0.1 (10% de redução de dano) Dano = 9.
        '''
        self._taxa_bloqueio = 0.05 # O este é o valor base para calculo, não representa a chance real de bloquear.
        # Chance de Evasão base:
        ''' A Evasão é o atributo que determina se o Fighter irá se esquivar ou não, tendo sua chance reduzida pelo
        atributo self.precisao, caso a esquiva seja ativada o Fighter ignora completamente o dano que irá receber.
        Das manobras ela é a prioridade no teste, antes de qualquer outra manobra ser testada ela é sempre a primeira a
        ser validada'''
        self._taxa_evasao = 0.02 # Valor base que é aumentado pelo valor de agilidade
        # Chance de Contra-Atacar:
        self._taxa_contra_ataque = 0 #
        # Chance de Defletir ataques:
        self._taxa_deflexao = 0 #
        # Chance de Desarmar ao atacar:
        self._taxa_desarme = 0.05 #
        # Chance de Reversão ao receber ataques:
        self._taxa_reversao = 0 #
        # Chance de Vingança ao receber ataques:
        self._taxa_vinganca = 0 #

        '''
        Modificadores de Atributo Primario e Secundario:
        Os modificadores serão separados em dois modelos
        FIXOS ->
        PERCENTUAIS -> 
        '''
        # Modificadores de atributo principais:

        # Força:
        self.modificador_percentual_forca = 1 # Aumento em Porcentagem % usado para calculos.
        self.modificador_fixo_forca = 0 # Aumento fixo ↑.
        # Agilidade:
        self.modificador_percentual_agilidade = 1 # Aumento em Porcentagem %
        self.modificador_fixo_agilidade = 0 # Aumento fixo ↑.
        # Velocidade:
        self.modificador_percentual_velocidade = 1 # Aumento em Porcentagem %
        self.modificador_fixo_velocidade = 0 # Aumento fixo ↑
        # Resistência:
        self.modificador_percentual_resistencia = 1 # Aumento em Porcentagem %
        self.modificador_fixo_resistencia = 0 # Aumento fixo ↑

        # Modificadores de atributos secundarios:

        # Pontos de Vida:
        self.modificador_percentual_pontos_vida = 1 # Será em porcentagem.
        self.modificador_fixo_pontos_vida = 0 # Será em porcentagem.
        # Iniciativa:
        self.modificador_percentual_iniciativa = 1 # Será em porcentagem.
        self.modificador_fixo_iniciativa = 0 #
        # Armadura:
        ''' Na Armadura os aumentos serão diferentes, só existem aumentos fixos que impactam
        diretamente no percentual do atriburo self._armadura'''
        self.modificador_fixo_armadura = 0 # 
        # Critico (Chance e Multiplicador de Dano):
        ''' No critico os aumentos fixos que impactam no dano e na chance de causar um acerto critico'''
        self.modificador_fixo_chance_critico = 0 # Este
        self.modificador_fixo_dano_critico = 0 # Este será somado e não multiplicado.


        # Modificadores de Manobras de Combate (Evasão, Contra-Ataque, Reversão, Vingança, etc):

        # Evasão:
        ''' Na Evasão os aumentos serão diferentes, só existem aumentos fixos que impactam
        diretamente no percentual do atriburo self._taxa_evasao ou na chance real de evasão'''
        self.modificador_fixo_evasao = 0 # Será em porcentagem.
        

    '''
    Propriedades da Classe Fighter:
    '''
    
    '''
    # Metodos de uso no combate:
    '''
    # Metodo para causar dano:
    def dano (self):
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
    
    