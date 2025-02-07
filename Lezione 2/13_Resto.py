kg_pesche = float(input("Inserisci il numero di kg di pesche: "))
prezzo_kg = float(input("Inserisci il prezzo al kg delle pesche: "))
prezzo_totale = kg_pesche * prezzo_kg
print(f"Il prezzo totale delle pesche è: {prezzo_totale}€")
contanti = float(input("Inserisci i contanti pagati dal cliente: "))
resto = contanti - prezzo_totale
print(f"Il resto dovuto al cliente è: {resto}€")