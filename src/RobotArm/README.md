# Smart System - Hololens Robotarm

## Summary
Voor dit project zijn verschillende zaken en objecten die een belangrijke werking en functie hebben in het volledige plaatje van het project. In dit deel wordt uitgelegd wat de gedachtegang was omtrent de robotarm en hoe (én waarom) het is uitgewerkt op deze specifieke manier.
De vereisten voor de robotarm waren dat er een reikwijdte vanuit de basis was van 0,5m (vanaf heden zal naar dit als de restricted enveloppe worden verwezen)) en dat er dan nog steeds een voorwerp van 1 kilogram kon worden opgetild en verzet worden. Voor de aandrijving van de stepper motoren werken we met een raspberry pi en een specifieke shield voor deze motoren.
Allereerst is er onderzoek gedaan naar de verschillende soorten robotarmen die er bestaan, de materialen die er tot onze beschikking werden gesteld en de materialen die we eventueel zelf moesten voorzien/3D printen.
Na dit onderzoek is besloten om een Articulated design voor de robotarm toe te passen met 3 gewrichten en een end-effector met 2 vingers (een end-effector is het uiteinde van de arm waarmee objecten kunnen worden vastgenomen). Er is ook gekozen voor het type gripper voor de end-effector, aangezien andere mogelijkheden niet mogelijk waren wegens te moeilijk/kostelijk. De keuze voor de gripper en 2 vingers geeft ook de meeste opties met betrekking tot het vastgrijpen van verschillende formaten van objecten (denk hierbij aan grote langwerpige objecten die met 4 vingers moeilijk tot onmogelijk vast te grijpen zijn, …).
[Eerste_schets](./img/eerste_schets.PNG)
Op de schets valt te zien naar wat voor type arm er gestreefd zou worden. Aangezien dit een eerste, snelle en ruwe schets was is er uiteraard niet veel aandacht gegaan naar het design en de hoe en wat van de arm. De materialen stonden op dit moment nog niet 100% vast namelijk.
Het maken van een 3D schets is hierna gestart in Autodesk Fusion360. Er is gekozen voor Fusion360 doordat bleek dat dit bij uitstek geschikt was voor het designen van een robotarm en er hier ook veel tutorials over te vinden waren op het internet, wat het leerproces weer vergemakkelijkte. 
Als stepper motor werd ons de Wantai Stepper Motor 42BYGHM809 aangeboden. Deze stepper motor is van het type nema 17, wat simpelweg de grootte van deze motor weergeeft. Er is ook een datasheet van de stepper motor bijgevoegd in deze repository. Voor het testen van de robot hebben we gebruik gemaakt van de shield en de buffer board, voor de raspberry pi, die ons werd aangeboden door de school. Dit testen van de motoren wordt gedaan zodat na kan worden gegaan wat de maximale kracht is van de stepper motoren. Dit kan dan meegenomen worden in de krachtberekeningen en het design van de robotarm.
Elke component is dan nagemaakt of gedesigned in Fusion360 om op deze manier een compleet beeld te kunnen geven van de volledige robotarm en zijn afmetingen. De componenten zijn gecombineerd in 1 bestand dat dan de volledige robotarm voorstelt. Uiteraard zijn de componenten ook los te bekijken, maar de robotarm is ook volledig in zijn geheel zichtbaar.


## De arm
Er is nog niet besloten wat voor een soort arm we gaan gebruiken. De opties zijn alvast:
* **Articulated:** Een armdesign dat bestaat uit 2 of meer (max 10) gewrichten. De arm is verbonden met de basis m.b.v. een draaiend gewricht en de verbinding tussen de verschillende "statische" delen gebeurt ook met deze gewrichten. Elk gewricht wordt gezien als een eigen as, dus hoe meer gewrichten, des te meer assen er gaan zijn. Elke as geeft meer vrijheden of bewegingsmogelijkheden. Meestal zijn er 4 tot 6 assen.
* **Cartesiaans:** Ook wel rectalineaire of gantry robots genoemd. Ze hebben 3 lineaire gewrichten die het cartesiaanse coördinatenstelsel (x, y en z) gebruiken. Ze kunnen ook een extra gewricht (pols in dit geval) voor rotatie gerelateerde bewegingen. De 3 prismatische gewrichten leveren een een lineaire bewegingen langs de as.
* **Cylindrisch:** De robot heeft minstens 1 draaibaar gewricht op de basis en 3 prismatische gewrichten om de verschillende "statische" delen te verbinden. Het rotatie gewricht beweegt over de gewrichtsas terwijl de prismatische gewrichten langs gewrichtsas in een lineaire beweging bewegen. Ze opereren in een cylindrische omgeving.
* **Polair:** Ook wel spherische robots genoemd, in deze configuratie is de arm verbonden met de basis d.m.v. een draaiend gewricht, een combinatie van 2 roterende gewrichten en een lineair gewricht. De assen vormen een polair coördinatensysteel en creëren een spherische werkplek.
* **SCARA:** Meestal gebruikt in assemblage toepassingen, deze selectieve en toegevende arm voor assemblage is vooral cylindrisch in design. Het bevat 2 parallelle gewrichten die meegaandheid voorzien in een geselecteerd paneel.
* **Delta:** Spinachtige robot die gebouwd is uit verbonden parallellogrammen die verbonden zijn aan een gezamenlijke basis. De parallellogrammen bewegen een enkele "end of arm tooling (EOAT)" in een koepelvormige werkplek. Veelgebruikt in de voedsel, farmaceutische en elektronische industrieën. Deze robot kan heel precieze en delicate bewegingen uitvoeren.

## End effector
*De end effector is in feite de "hand" van de robotarm.*

We zullen een end effector van het type gripper gebruiken voor de robotarm. De hoeveelheid vingers is nog niet beslist.
    In de meeste industriële toepassingen wordt gekozen voor een 2-vingerige end effector, maar dit staat niet vast.

ivm krachtsberekeningen en de arm:
* https://blog.robotiq.com/bid/72863/End-Effector-Gripping-Strategies 
* https://en.wikipedia.org/wiki/Robot_end_effector

## Krachtsberekeningen

*Hangt nog af van de hoeveelheid vingers die gebruikt zullen worden.*
Er worden 2 vingers gebruikt.

## Specificaties
Bereik (in degrees of freedom):

Er zijn 3 verschillende fasen bij deze degrees of freedom:
* Maximum enveloppe: De maximale bewegingsradius van de robotarm.
* Restricted enveloppe: De bewegingsradius die door het programma dat op de robotarm staat zal worden gebruikt.
* Operating enveloppe: De zone waar de robotarm zich in een specifieke momentopname in bevindt.


## De arm die wij gaan gebruiken
We gaan voor een articulated design van de robotarm zelf. Dit komt het beste uit m.b.t. de servo-motoren (?types moeten nog opgezocht worden!) en de vele bewegingen die moeten worden uitgevoerd door de arm. 

Voor de end effector zouden we kunnen gaan voor een hand met 2 vingers, dit wordt in de meeste industriële toepassingen het meest gebruikt.

Berekeningen:
* F = ((m * a)/(µ * n))
Waarbij:
* F de kracht van de grip op het object is
* m de massa van het object
* a de versnelling van het object
* µ de coëfficiënt van de frictie het object
* n is het aantal vingers van de grijphand

Er zullen 6 servos worden gebruikt:
* 1 voor de horizontale rotatie van de arm
* 3 voor de 3 verticaal beweegbare delen van de arm te besturen, ieders op een gewricht geplaatst
* 1 voor de rotatie van de end effector, deze moet ook kunnen meedraaien voor wanneer het doel object "scheef" zou taan t.o.v. de arm.
* 1 voor de vingers van de end effector te doen openen en dichtdoen.

De robotarm zal geprint worden met behulp van een 3D printer, het plastic materiaal dat we hiervoor gebruiken moet nog beslist worden in overeenkomst met wat AP hogeschool te bieden heeft.
We kunnen gebruik maken van:
* PLA: voor de eerste prototypes (de hand die op de huidige robot komt) gebruiken we PLA. Een natuurlijk polymeer dat biologisch afbreekbaar is. Hoge modulus en hoge sterkte. In amorfe toestand zacht boven ca. 55 °C, maar indien semi-kristallijn bruikbaar tot hogere temperatuur. Rek bij breuk vrij laag, maar afhankelijk van MW.
* ABS: Het materiaal is mechanisch sterk waardoor je je geen zorgen hoeft te maken over de levensduur van jouw 3D geprinte model. Niet biologisch afbreekbaar en heeft een specifieke manier van voorbereiden nodig wanneer het wordt gebruikt voor 3D printen. Zal gebruikt worden voor de uiteindelijk robotarm.

**Concreet zal de arm dus bestaan uit:**
* 3 gewrichten verbonden aan elkaar, aan 1 zijde aan het rotatievlak en aan de andere zijde verbonden met de end effector.
* 6 servos (zoals reeds eerder vermeld).

### Servo's die gebruikt zullen worden:
We gebruiken de Wantai Stepper Motor 42BYGHM809.
*Datasheet bijgevoegd in deze map.*

**Specificaties**
* +/-5% step accuracy
* Ambient temperature range 20 - 50°C
* Insulation resistance 100 mega Ohm min 50V DC
* Step angle: 0,9°
* 400 steps/revolution (400 stappen per revolutie)
* Voltage rating 2,7V
* Current rating 1,68A
* Inductance: 3,5 mH per coil
* Temperature rise tolerance: 80°C
* Holding torque: 4200 g*cm ====//==== 48N.cm volgens https://www.sparkfun.com/products/10846 
* Detent torque: 260 g*cm
* Number of leads: 4 (rood, blauw, groen en zwart)
* Motor length: 4,8cm
* Nema 17 form factor
* Weight 340g

*In de volgende tekst is een punt een maalteken, indien er een zineinde is zal dit aangegeven worden door 2 punten op elkaar volgend..*
De servo kan dus wanneer er geen stroom geleverd wordt een object in stilstand houden aan een kracht van 260 g.cm s.. De maximale torque wanneer er stroom geleverd wordt, en dus de servo de mogelijkheid heeft om het object stil te houden, is gelijk aan 4200 g.cm..
