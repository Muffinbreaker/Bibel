
"""
Eine Mathemagierin bittet dich darum, einen ihrer Tricks durch ein kleines Programm zu automatisieren. Der Trick beginnt wie folgt:

1. Denke dir eine Zahl aus (Variable `number`).
2. Multipliziere sie mit 2.
3. Addiere 10 zum Ergebnis.
4. Teile das Ergebnis durch 2.

Führe diese Rechnung  für die Variable _number_ durch und gebe das Ergebnis aus.
"""

number = 55.8954654566464621654651321654

result = (((float(number*2) + 10)/2))

print("Du hast " + str(float(number)) + " ausgewählt " + " das Ergebnis ist " + str(float(result)))


"""
Die Mathemagierin ist sehr zufrieden mit deiner Arbeit und bittet dich um Hilfe bei der Betreuung von ihrem Online-Shop. Sie kennt nur die Mailadressen ihrer Kunden, und du sollst anhand der Mailadressen ein vereinfachtes Verzeichnis mit ihren Namen anlegen.
a. ) Ziehe einen Namen aus einer Mailadresse der Form name@service.com

Wenn die Mailadresse _Max-Mustermann@gmail.com_ lautet, sollst du Max-Mustermann ausgeben; wenn die Mailadresse _KlaraKlarnamen@uni-berlin.de_ heisst, sollst du KlaraKlarnamen ausgeben.

Hinweis: Schau dir dazu auf jeden Fall nochmal die .split() - Methode an. Damit kannst du z. B. eine E-Mail-Adresse am @ - Symbol zersägen / zerlegen.

"""

email = "KlaraKlarnamen@uni-berlin.de"

email.split("@")

print(email.split("@")[0])



"""
Ziehe einen Namen aus einer Mailadresse der Form info@name.com

Manchmal stehen die Namen bei einer Mailadresse auch erst hinter dem @-Zeichen. Gebe auch für solche Fälle die Namen aus; entferne dabei die Endung .com bzw. .de. Du darfst dazu voraussetzen, dass innerhalb 
des Namens kein Punkt vorkommt. Wenn die Mailadresse also _info@Max-Mustermann.com_ lautet, sollst du Max-Mustermann ausgeben.

Hinweis: Es ist okay, wenn du für die Berechnung mehere .split() - Befehle benötigst, oder ein Ergebnis zwischenspeichern möchtest. Gerne kannst du auch den Code aus der Teilaufgabe a) hier mitverwenden.
"""


email = "info@Max-Mustermann.com"

print(email.split("@").pop().split(".")[0])





"""
c.) Berechne: Wie viele Kunden gibt es im Online-Shop?

Aktuell legen alle Kunden (mail1, mail2, mail3) als separate Variable vor. Wir möchten daraus jetzt eine Liste bauen, sodass wir die Möglichkeit hätten, später noch weitere Kunden in diese Liste hinzuzufügen.

Überführe deswegen die Kunden mail1, mail2 und mail3 in die Liste clients und lasse dir anschließend die Anzahl der Elemente der Liste clients mit Hilfe von Python ausgeben.

"""
liste = []

kunde_1 = "Mail_1"
kunde_2 = "Mail_1"
kunde_3 = "Mail_1"

liste.append(kunde_1)
liste.append(kunde_2)
liste.append(kunde_3)


print(len(liste))


"""
d.) Eine Mailadresse aus Strings zusammenbauen

Plötzlich fällt der Mathemagierin ein, dass in der Liste clients noch ihr wichtigster Onlineshop-Kunde fehlt. Die Infos zu ihm wurden bei einem misslungenen Trick in zwei Teile zersägt und liegen seitdem in der Liste ["Buehnenzauberer", "magic.com"] herum.

Rekonstruiere mit Hilfe von Python die Mailadresse des Kunden (da fehlt ein @ zwischen "Buehnenzauberer" und "magic.com") und gebe sie aus, damit sich der Onlineshop-Kundendienst nach seinem Wohlbefinden erkundigen kann.

"""


clients = ["Buehnenzauberer", "magic.com"]

print("@".join(clients))
print(clients[0] + "@" + clients[1])



"""
a.) Gib nacheinander alle Kontinente aus der Liste continents aus.
continents = ["Afrika", "Antarktis", "Asien", "Australien und Ozeanien", "Europa", "Nordamerika", "Südamerika"]
"""

continents = ["Afrika", "Antarktis", "Asien", "Australien und Ozeanien", "Europa", "Nordamerika", "Südamerika"]

#for i in continents:
 #   print(i)


""":
b.) Gib aus der Liste continents nur die bewohnten Kontinente aus.

Hinweis:: Antarktis ist nicht bewohnt. Diesen Kontinent kannst du also bei der Ausgabe einfach überspringen.

"""

#for i in continents:
#    if i == "Antarktis":
#        continue
#    print(i)

""":
c.) Gib aus der Liste stuff nur die Kontinente aus.

Du kannst dafür die Liste stuff mit einer Schleife durchgehen und dann mit Hilfe der Variable continents prüfen, ob ein Element der Liste stuff auch in der Liste continents vorkommt.

"""

stuff = ["Asien", "Max", 101, "Monika", "China", "Simbabwe", "Antarktis"]


index = -1

for i in stuff:
    if i in continents:
        print(i)


"""
d.) Wie viele Kontinente sind in der Liste stuff enthalten?

Schreibe dazu eine Schleife, mit der du die Anzahl der Kontinente in der Liste stuff zählst und gib diesen Wert dann aus.
"""

counter = 0
for i in stuff:
    if i in continents:
        counter += 1

print(counter)



"""
Zurück zur Mathemagierin: Sie möchte in ihrem Shop eine Rabattaktion starten, um das Geschäft anzukurbeln.
Natürlich hat sie dabei wieder etwas zu programmieren für dich. Du sollst die Berechnung der reduzierten Preise mit einer if-elif-else-Struktur vereinfachen.

Dabei ist zu beachten:

Artikel, die zwischen 0 und 20 (einschließlich) Taler kosten, werden um 20 % reduziert; Artikel, die zwischen 20 (nicht einschließlich) und
50 Taler (einschließlich) kosten, werden um 40 % reduziert. Alle anderen Artikel, also solche, die mehr als 50 Taler kosten, werden um 60 % reduziert.
"""
"""
b.) Berechne nun für jeden der alten Preise aus der Liste prices die passenden reduzierten Preise und speichere sie in der neuen Liste new_prices. Gib diese Liste schließlich aus.¶
"""

prices = [2, 50, 70, 30]
new_prices =[]


for price in prices:
    if price <= 20:
        price = price*0.8


    elif price <= 50:
        price = price * 0.4


    else:
        price = price * 0.4


    new_prices.append(price)

#print(new_prices)

"""
c.) Zusatzaufgabe (schwierig!)

Nun überreicht dir die Mathemagierin mit zitternden Händen die Liste _chaos_, in der neue und alte Preise gemischt sind! Angesichts dieser undurchdachten Arbeit schlägst du
dir die Hände vor dem Kopf zusammen, aber es hilft ja nichts: Nur du kannst hier wieder Ordnung schaffen, indem du alles zusammenbringst, was du schon gelernt hast!

Gehe die Elemente in der Liste chaos durch. Bei einem neuen Preis ziehst du bloß den neuen Wert aus dem String und hängst ihn der Liste order an. Bei einem alten Preis 
hingegen holst du dir den alten Wert, berechnest den neuen Preis und hängst diesen Wert an die Liste order.

Schließlich gibst du die vollständige Liste order aus, in der nur noch neue Preise drinstehen (und nur noch Zahlen!).


"""


chaos =["old price: 40", "new price: 21", "old price: 29", "old price: 50", "new price: 101"]
old =[]
new = []
order = []

index = -1
for i in chaos:
    index += 1
    test = chaos[index].split("price: ")
    if test[0] == "old ":
        old.append(test[1])
    elif test[0] == "new ":
        new.append(test[1])

for price in old:
    if int(price) <= 20:
        price = int(price)*0.8
    elif int(price) <= 50:
        price = int(price) * 0.6
    else:
        price = int(price) * 0.4
    order.append(price)

for price in new:
    price = int(price) * 1
    order.append(price)

print(order)
