class Classe:
    def __init__(self,fome,saude,nivel,forca,exp):
        self.fome = fome
        self.saude = saude
        self.nivel = nivel
        self.forca = forca
        self.exp = exp

pet = Classe(0,10,0,1,0)
pet2 = Classe(0,4,0,1,0)

def luta():
    pet2.saude = 4
    while True:
        if (pet.saude <= 0 or pet2.saude <= 0):
            break
        else:
            resposta = input("\nPara atacar digite: atacar\n")
            if resposta == "atacar":
                pet2.saude -= pet.forca
                print("\n>>>Voce atacou o pet causando dano nele de",pet.forca)
                print("\n>>Pet2 te atacou causando dano de",pet2.forca)
                pet.saude -= pet2.forca
                print("\n Sua saude atual eh:",pet.saude)
                print("\n Saude do adversario:",pet2.saude)
            else:
                print("\nPet2 te atacou causando dano de",pet2.forca)
                pet.saude -= pet2.forca
                print("\n Sua saude atual eh:",pet.saude)
                print("\n Saude do adversario:",pet2.saude)
       


jogo = True

while (jogo == True):
    print("Digite a opção desejada | alimentar | treinar | status | lutar | dormir |")
    escolha = input()
    
    if pet.exp >= 10:
        pet.nivel += 1
        pet.forca += 1
        print("---------------\nSeu Pet subiu de nivel!\n")
        print("Nivel atual:",pet.nivel,"---------------\n")
        print("Forca atual:",pet.forca,"---------------\n")
        pet.exp = 0
        
    
    if pet.fome > 6:
        print("fome maior que 6 fim de jogo")
        break

    elif pet.saude < 1:
        print("saude nivel 0 fim de jogo")
        break
    
    elif (escolha == "alimentar"):
        pet.fome -= 1
        print("---------------\nVirtual Pet Alimentado!\n---------------")
        
    elif (escolha == "treinar"):
        pet.saude -= 1
        pet.fome += 1
        pet.exp += 0.5
        print("Ganhou",pet.exp,"pontos de experiencia")
        print("---------------\nVirtual Pet Treinou!\n---------------")
        
    elif (escolha == "status"):
        print("---------------\n")
        print("Saude:", pet.saude,"\nFome:",pet.fome,"\nNivel:",pet.nivel,"\nForca:",pet.forca,"\nPontos Experiencia:",pet.exp)
        print("\n---------------")
        
    elif (escolha == "lutar"):
        print("---------------\n")
        print("Adversário: pet2:\n Forca:",pet2.forca)
        print("\nSaude:",pet2.saude)
        luta()
        pet.exp += 2
        pet.fome += 2
        print("---------------\nSeu pet ganhou +2 de experiencia ficando com total de",pet.exp,"pontos de experiencia")
        print("\n---------------")
        
    
    elif(escolha == "dormir"):
        pet.saude += 5
        print("---------------\nSeu pet recuperou +5 de saude!\n---------------")
    
    elif(escolha == "codigo"):
        pet.fome -= 40
        pet.saude += 40
        print("------\nfome:",pet.fome,"\nsaude:+",pet.saude,"\n------")


#Developed by Leonardo L M



