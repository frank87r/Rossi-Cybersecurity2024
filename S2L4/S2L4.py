
# Funzione per calcolare il perimetro di un rettangolo
def perimetro_rettangolo(lato1, lato2):
    perimetro = 2 * (lato1 + lato2)
    return perimetro

# Funzione per calcolare il perimetro di un quadrato
def perimetro_quadrato(lato):
    perimetro = 4 * lato
    return perimetro

# Funzione per calcolare la circonferenza di un cerchio
def circonferenza(raggio):
    circonferenza = 2 * 3.14 * raggio
    return circonferenza

# Chiedere all'utente che tipo di figura desidera
scelta = input("Vuoi calcolare il perimetro di un rettangolo, un quadrato o la circonferenza  di un cerchio? \n(Inserisci 'rettangolo', 'quadrato' o 'cerchio'): ").lower()

if scelta == 'rettangolo':
    # Input per il rettangolo
    lato1 = float(input("Inserisci la larghezza del rettangolo: "))
    lato2 = float(input("Inserisci l'altezza del rettangolo: "))
    perimetro = perimetro_rettangolo(lato1, lato2)
    print(f"Il perimetro del rettangolo è: {perimetro}")

elif scelta == 'quadrato':
    # Input per il quadrato
    lato = float(input("Inserisci il lato del quadrato: "))
    perimetro = perimetro_quadrato(lato)
    print(f"Il perimetro del quadrato è: {perimetro}")

elif scelta == 'cerchio':
    # Input per il cerchio
    raggio = float(input("Inserisci il raggio del cerchio: "))
    circonferenza = circonferenza(raggio)
    print(f"La circonferenza del cerchio è: {circonferenza}")

else:
    print("Scelta non valida.")
