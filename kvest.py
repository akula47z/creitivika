print("Вы просыпаетесь у себя в замке")
vybor = input ("Вам надо сделать серьёзный выбор, продолжать спать, пойти на прогулку или идти решать городские проблемы.").lower ()
while vybor != "продолжать спать" and vybor != "пойти на прогулку" and vybor != "идти решать городские проблемы":
    vybor = input ("Дак что же вы выберите?").lower()
if vybor == "продолжать спать":
    print("Народ устроил бунт:[Почему король дремлет и ничего не делает?].\nОни сжигают ваш замок.\nБольше вы не проснётесь.\nПоздравляю! Концовка Короля лентяя.")
elif vybor =="идти решать городские проблемы":
    print("Неожиданно для вас на город наподает дракон. Он разрушает замок.\nПоздравляю! Неожиданная концовка.")
elif vybor=="пойти на прогулку":
    print("Вы смотрите в окно. ваш взор падает на город, Ваш сад и лес")
    while vybor != "город" and vybor != "лес" and vybor != "сад":
        vybor = input ("Куда хочется Королю?").lower()
        if vybor == "лес":
            print("Вы бродите по лесу со своей гвардией. Вам очень хочется приключений, но к сожалению в лесу их н найти.\nВсех жутких животных и монстров давно переловили местные охотники и герои.\nВдруг появились тучи и начался дожд.\nВ вас из-за металлической кароны попала молния.\nПоздравляю! Концовка Короля, не учившего в школе ОБЖ.")
        elif vybor =="сад":
            print("Вы бодите по саду. Тут множество красивых цветов и различных запахов. Вам тут нравится. Вы чувтвуете, что вы в безопасности.\nДо конца дня вы проходили в саду. Когда вы ложились спать, непроизвольно нахлынули лучшие восспоминания вашей жизни. Ваше детство. Родители. Неожиданно для себя Вы прослезились.\nПоздравляю! Хорошая настольгиическая концовка).")
        elif vybor =="город":
            print("Вы гуляете по городу. Вы замечаете, что к городу кто-то приближается. Приглядевшись, вы узнаёте героя. В его руках была голова дракона.\nИ неожиданнодля себя, Вы понимаете, что работа кароля никапли не скушная и не весёлая. Вы решаете бросить престол и уйти из города на встречу приключениям.\nВы были в множестве сражений, повидали много богатств, приключений, и друзей. Познали предательтво и дружбу. Нашли свою любовь и призвание.\nВ конце концов вы дожили до старости. Вокруг вас сидят Ваши дети и Ваша жена. Вы ни о чём не жалете.\nС гордостью, в последний раз, Вы закрываете глаза.\nПоздравляю! Настоящая концовка!")
  
  
    