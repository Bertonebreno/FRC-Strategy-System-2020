import time

team = input("TIME: ");
jogo = input("JOGO: ");

autoLine = 0;  # 
autoBottom = 0;  # abo
autoOutter = 0;  # aou
autoInner = 0;  # ain
autoPegouPowerCell = 0;  # ape
autoErroPowerCell = 0;  # aer

teleopBottom = 0;  # tbo
teleopOutter = 0;  # tou
teleopInner = 0;  # tin
teleopErroPowerCell = 0;  # ter
teleopParouDeFuncionar = 0;  # tpa

cicloTarget = 0;  # cta
cicloLine = 0;  # cau
cicloTrincheira = 0;  # ctr
cicloRendezvous = 0;  # cre
cicloAtrasTrincheira = 0;  # cat

endEstaciona = 0;  # ees
endSobe = 0;  # eso
endNivelaSozinho = 0;  # eni
endFalhouSubida = 0;  # efa

initialTime = time.time();

log = []
while(True):
    userInput = input();
    log.append([(time.time() - initialTime), userInput]);

    try:
        number = int(userInput.split()[1]);
        userInput = userInput.split()[0];
    except:
        number = 1

    if(userInput == "ali"):
        autoLine += 5
    elif(userInput == "abo"):
        autoBottom += number
    elif(userInput == "aou"):
        autoOutter += number
    elif(userInput == "ain"):
        autoInner += number
    elif(userInput == "ape"):
        autoPegouPowerCell += number
    elif(userInput == "aer"):
        autoErroPowerCell += number
        

    elif(userInput == "tbo"):
        teleopBottom += number
    elif(userInput == "tou"):
        teleopOutter += number
    elif(userInput == "tin"):
        teleopInner += number
    elif(userInput == "ter"):
        teleopErroPowerCell += number
    elif(userInput == "tpa"):
        teleopParouDeFuncionar += 1
        
    elif(userInput == "cta"):
        cicloTarget += number
    elif(userInput == "cli"):
        cicloLine += number
    elif(userInput == "ctr"):
        cicloTrincheira += number
    elif(userInput == "cre"):
        cicloRendezvous += number
    elif(userInput == "cat"):
        cicloAtrasTrincheira += number
        

    elif(userInput == "ees"):
        endEstaciona += 5
    elif(userInput == "eso"):
        endSobe += 25
    elif(userInput == "eni"):
        endNivelaSozinho += 15
    elif(userInput == "efa"):
        endFalhouSubida += 1
   
    elif(userInput == "exit"):
        break;

    else:
        log[len(log)-1][1] = "ERRO: " + log[len(log)-1][1]

for i in range(len(log)):    
    print(log[i]);


print();
print("TIME: {}".format(team));
print("JOGO: {}".format(jogo));
print();
print("autoLine: {}".format(autoLine));
print("autoBottom: {}".format(autoBottom));
print("autoOutter: {}".format(autoOutter));
print("autoInner: {}".format(autoInner));
print("autoPegouPowerCell: {}".format(autoPegouPowerCell));
print("autoErroPowerCell: {}".format(autoErroPowerCell));

print("teleopBottom: {}".format(teleopBottom));
print("teleopOutter: {}".format(teleopOutter));
print("teleopInner: {}".format(teleopInner));
print("teleopErroPowerCell: {}".format(teleopErroPowerCell));
print("teleopParouDeFuncionar: {}".format(teleopParouDeFuncionar));

print("cicloTarget: {}".format(cicloTarget));
print("cicloLine: {}".format(cicloLine));
print("cicloTrincheira: {}".format(cicloTrincheira));
print("cicloRendezvous: {}".format(cicloRendezvous));
print("cicloAtrasTrincheira: {}".format(cicloAtrasTrincheira));

print("endEstaciona: {}".format(endEstaciona));
print("endSobe: {}".format(endSobe));
print("endNivelaSozinho: {}".format(endNivelaSozinho));
print("endFalhouSubida: {}".format(endFalhouSubida));






