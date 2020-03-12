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
cicloAutoLine = 0;  # cau
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

    if(userInput == "ali"):
        autoLine += 1
    elif(userInput == "abo"):
        autoBottom += 1
    elif(userInput == "aou"):
        autoOutter += 1
    elif(userInput == "ain"):
        autoInner += 1
    elif(userInput == "ape"):
        autoPegouPowerCell += 1
    elif(userInput == "aer"):
        autoErroPowerCell += 1
        

    elif(userInput == "tbo"):
        teleopBottom += 1
    elif(userInput == "tou"):
        teleopOutter += 1
    elif(userInput == "tin"):
        teleopInner += 1
    elif(userInput == "ter"):
        teleopErroPowerCell += 1
    elif(userInput == "tpa"):
        teleopParouDeFuncionar += 1
        
    elif(userInput == "cta"):
        cicloTarget += 1
    elif(userInput == "cau"):
        cicloAutoLine += 1
    elif(userInput == "ctr"):
        cicloTrincheira += 1
    elif(userInput == "cre"):
        cicloRendezvous += 1
    elif(userInput == "cat"):
        cicloAtrasTrincheira += 1
        

    elif(userInput == "ees"):
        endEstaciona += 1
    elif(userInput == "eso"):
        endSobe += 1
    elif(userInput == "eni"):
        endNivelaSozinho += 1
    elif(userInput == "efa"):
        endFalhouSubida += 1
   
    elif(userInput == "exit"):
        break;

    else:
        log[len(log)-1][1] = "ERRO: " + log[len(log)-1][1]

for i in range(len(log)):    
    print(log[i]);

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
print("cicloAutoLine: {}".format(cicloAutoLine));
print("cicloTrincheira: {}".format(cicloTrincheira));
print("cicloRendezvous: {}".format(cicloRendezvous));
print("cicloAtrasTrincheira: {}".format(cicloAtrasTrincheira));

print("endEstaciona: {}".format(endEstaciona));
print("endSobe: {}".format(endSobe));
print("endNivelaSozinho: {}".format(endNivelaSozinho));
print("endFalhouSubida: {}".format(endFalhouSubida));






