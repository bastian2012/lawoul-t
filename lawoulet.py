import random,os,pickle
nomb_user=0;max=50;min=0;nouvo_sko=0
def test_maj(chaine):
    for i in chaine:
        if i.isupper():
            return True
    return False

def test_space(chaine):
    if " " in chaine:
        return True
    return False

def test_non():
    while True:
        non_itilizatè=input("antre yn non itilizatè : ")
        if not test_maj(non_itilizatè) and not test_space(non_itilizatè):
            return non_itilizatè
        else:
            print("antre non itilizatè a sans espas ni majiskil : ")

non_itilizatè=test_non()

while True:
    nomb_ordi=5
    tantativ=0;chans=5;score=0
    while chans>0:
        try:
            nomb_user=int(input(f" {non_itilizatè} antre yon nomb ant {min} ak {max} :"))
            os.system("clear")
            if nomb_user>=min and nomb_user <= max:
                tantativ+=1;chans-=1
                if nomb_user==nomb_ordi:
                    if chans==0:
                        score=30
                    else:
                        score +=30*(chans)
                    nouvo_sko +=score
                    print(f"bravo {non_itilizatè} !!!\n\n ou gnyn sou {tantativ} tantativ ou fè yon sko {score} pwen nouvo sko a se {nouvo_sko}\n\n")
                    break
                else:
                    if nomb_ordi<nomb_user:
                        print(f"ou pèdi {non_itilizatè} !!\n sa ou chwazi a pi gro pase nomb ki soti nan tiraj la\nou rete {chans} chans. sko ou se {score} pwen\n")
                    else:
                        print(f" {non_itilizatè} ou pèdi !!\n\n sa ou chwazi a pi piti pase nomb ki soti nan tiraj la\n\nou rete {chans} chans. sko ou se {score} pwen\n\n")
        except:
            os.system("clear")
            print("sa ou antre a pa yon nomb !!!\n")
    kontinye=input(f"\n{non_itilizatè} peze K pou'w soti nan jwèt la | nenpot lot touch pou'w kontinye  :")
    if kontinye.lower()=="k":
        break
    os.system("clear")