prezzo_jeans1 = int(input("Inserisci il prezzo del primo paio di jeans: "))
prezzo_scontato1 = prezzo_jeans1 - prezzo_jeans1 * 0.20
print("Il prezzo scontato del primo paio di jeans è:", prezzo_scontato1)
prezzo_jeans2 = int(input("Inserisci il prezzo del secondo paio di jeans: "))
prezzo_scontato2 = prezzo_jeans2 - prezzo_jeans2 * 0.20
print("Il prezzo scontato del secondo paio di jeans è:", prezzo_scontato2)
totale_scontato = prezzo_scontato1 + prezzo_scontato2
print("Il totale da pagare dopo lo sconto è:", totale_scontato)
contanti = int(input("Inserisci i contanti che hai: "))
resto = contanti - totale_scontato
print("Il resto che otterrai è:", resto)