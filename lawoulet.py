import random,os,pickle
max=10;min=0;nouvo_sko=0;ansyen_sko=0
def test_maj(chaine):
    for i in chaine:
        if i.isupper():
            return True
    return False

def test_space(chaine):
    if " " in chaine:
        return True
    return False

def clear():
    os.system("clear")
clear()
def test_non():
    while True:
        non_itilizatè=input("antre yn non itilizatè : ")
        if not test_maj(non_itilizatè) and not test_space(non_itilizatè):
            clear()
            return non_itilizatè
        else:
            clear()
            print("antre non itilizatè a sans espas ni majiskil : ")
    
non_itilizatè=test_non()
file_name='file.pk1'

def lecture():
    with open(file_name, 'rb') as fichier:
        data = pickle.load(fichier)
    return(data)

def ecriture(file_name,data):
    with open(file_name, 'wb') as fichier:
        pickle.dump(data, fichier)

def eta_jwèt(ansyen_sko,sko,nouvo_sko,chans):
    print(f"Non itilizatè : {non_itilizatè.upper()} \t\tansyen sko :{ansyen_sko}\t\t sko pati a : {sko}\t\t nouvo sko : {nouvo_sko}\t\tchans : {chans}\n")


try:
    data = lecture()
except (FileNotFoundError, EOFError):
    data = {}
ecriture(file_name,data)
    
data=lecture()
        
if not non_itilizatè in data:
    data[non_itilizatè]=0
    ecriture(file_name,data)
data=lecture()

while True:
    clear()
    nomb_ordi=random.randint(min,max)
    tantativ=0;chans=5;score=0
    ansyen_sko=data[non_itilizatè]
    nouvo_sko=ansyen_sko
    while chans>0:
        if chans==5:
            eta_jwèt(ansyen_sko,score,nouvo_sko,chans)
        try:
            nomb_user=int(input(f" {non_itilizatè.upper()} antre yon nomb ant {min} ak {max} :"))
            if nomb_user>=min and nomb_user <= max:
                tantativ+=1;chans-=1
                if nomb_user==nomb_ordi:
                    clear()
                    if chans==0:
                        score=30
                    else:
                        score +=30*(chans)
                    nouvo_sko +=score
                    data[non_itilizatè]=nouvo_sko
                    ecriture(file_name,data)
                    chans=0
                    eta_jwèt(ansyen_sko,score,nouvo_sko,chans)
                    print(f"bravo {non_itilizatè.upper()} !!!\n\n ou gnyn sou {tantativ} tantativ\n")
                    break
                else:
                    clear()
                    eta_jwèt(ansyen_sko,score,nouvo_sko,chans)
                    if nomb_ordi<nomb_user:
                        print(f"ou pèdi {non_itilizatè.upper()} !!\n sa ou chwazi a pi gro pase nomb ki soti nan tiraj la\n")
                    else:
                        print(f" {non_itilizatè.upper()} ou pèdi !!\n\n sa ou chwazi a pi piti pase nomb ki soti nan tiraj la\n")
            else:
                clear()
        except:
            os.system("clear")
            print("sa ou antre a pa yon nomb !!!\n")
    print(f"{non_itilizatè.upper()} nomb kache a se te {nomb_ordi} ")
    kontinye=input(f"\n1- peze K pou'w soti nan jwèt la\n2- nenpot lot touch pou'w kontinye  :")
    if kontinye.lower()=="k":
        break
    os.system("clear")