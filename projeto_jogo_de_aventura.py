print("Você está caminhando em uma floresta escura e encontra dois itens: um FÓSFORO e uma LANTERNA.")
escolha = input(str("Qual você quer pegar? "))
print()

escolha = escolha.lower()
if escolha == "fósforo":
    print("Você pega o fósforo e o acende. Por um instante, a floresta ao seu redor fica iluminada.")
    print("Você vê um grande urso-pardo e então o fósforo se apaga.")
    print()
    escolha = input(str("Você quer CORRER ou SE ESCONDER atrás de uma árvore? "))
    print()
    if escolha == "correr":
        print("Ao começar a correr você percebe que o urso vai te alcançar.")
        escolha = input(str("Então voce vê um tronco de arvoce oca, e um riacho. Você quer ENTRAR no tronco, ou DESCER o riacho? "))
        if escolha == "entrar":
            print("Você rapidamente se esconde no tronco oco.")
            print("Mas depois de um tempo, fica desconfortavel")
            print()
            escolha = input(str("Você quer SAIR e ver se está seguro ou FICAR escondido? "))
            if escolha == "sair":
                print("Você sai e percebe que despistou o urso, voce fugiu dele!")
            elif escolha == "ficar":
                print("Você passa a noite dentro do tronco completamente desconfortavel, pega uma doença e morre.")
                print()
            else:
                print("Essa não é uma opção. ")    
                
        if escolha == "descer":
            print("Você entra no riacho, e a correnteza vai te levando até uma cachoeira.")
            print()
            escolha = input(str("Você quer ARRISCAR descer a cachoeira ou SAIR para o outro lado do riacho? "))     
            print()       
            if escolha == "arriscar":
                print("A correnteza vai te puxando ate a cachoeira, voce vai na cachoeira bate a cabeça e morre.")
            elif escolha == "sair":
                print("Você consegue nadar ate a beira do outro lado do riacho, e o urso fica com medo de entrar no riacho, voce conseguiu fugir dele.")   
            else:
                print("Essa não é uma opção. ")    
        else:
            print("Essa não é uma opção. ")
    if escolha == "se esconder":
        print("Você vai para tras da arvore, e la encontra uma pedra.")
        escolha = input(str("Você pega a pedra, e tem duas opções arriscadas, JOGAR a pedra longe para distrair o urso ou ATACAR o urso com a pedra, o que voce faz? "))
        print()
        if escolha == "jogar":
            print("Você joga a pedra, então o urso vai ate e ela e fica cheirando.")
            escolha = input(str("Voce quer SAIR correndo, ou ATACAR o urso por tras? "))
            print()
            if escolha == "sair":
                print("Voce corre do urso, despista ele, voce consegue fugir!")
            elif escolha == "atacar":
                print("voce ataca o urso, mas ele é mais forte e te mata.")
            else:
                print("Essa não é uma opção. ")  
        if escolha == "atacar":
            print("Você joga a pedra no urso, mas isso não afeta ele em nada, ele descobre aonde voce esta e te mata.")    
        else:
            print("Essa não é uma opção. ")          

if escolha == "lanterna":
    print("Você pega a lanterna e a liga.")
    print("Você vê o caminho iluminado à sua frente, mas pensa que também ouviu algo nas proximidades.")

    escolha = input(str("Você quer SEGUIR o caminho ou PROCURAR nas árvores o que fez aquele barulho?"))
    print()
    if escolha == "seguir":
        print("Você segue, e um pouco mais a frente você ve um urso-pardo.")

        escolha = input(str("O urso ainda está longe, você quer VOLTAR de vagar, ou ATACAR o urso? "))
        print()
        if escolha == "voltar":
            print("Você começa a andar devagar de costas, ainda olhando o urso, fazendo o minimo de barulho, mas pisa em um galho, o urso escuta e te ataca, você morre.")
        elif escolha == "atacar":
            print("Você vai pra cima do urso na mão livre, com grande coragem, mas toma uma patada e morre")
        else:
            print("Essa não é uma opção. ")

    if escolha == "procurar":
        print("Você olha para os lados, observa tudo, e ao lado de um arbusto encontra uma caixa preta.")
        escolha = input(str("Você quer ABRIR a caixa ou CONTINUAR? "))
        print()
        if escolha == "abrir":
            print("Você encontrou um revolver. Não sabe de quem é, mas continua seu caminho.")
            escolha = input(str("Logo a frente encontra um urso-pardo. Voce quer FUGIR ou ATACAR? "))
            print()
            if escolha == "fugir":
                print("Você tenta fugir, mas ao sair correndo tropeça, cai e o urso te mata.")
            elif escolha == "atacar":
                print("Você pega o revolver que achou, e cuidadosamente tenta sair.")
                print("O urso te ve e vai pra cima de você, mas você consegue acertar um tiro no urso, e sai vivo")
            else:
                print("Essa não é uma opção. ")    

        if escolha == "continuar":
            print("Você fica com medo de abrir aquela caixa, então apenas segue em frente.")
            escolha = input(str("Logo a frente encontra um urso-pardo. Voce quer FUGIR ou ATACAR? "))
            print()
            if escolha == "fugir":
                print("Você tenta fugir, mas ao sair correndo tropeça, cai e o urso te mata.")
            elif escolha == "atacar":
                print("Você vai pra cima do urso na mão livre, com grande coragem, mas toma uma patada e morre")
            else:
                print("Essa não é uma opção. ")  
else:
            print("Essa não é uma opção. ")                        