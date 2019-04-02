# Smart System - Hololens Robotarm

## Summary
In dit bestand zal de volledige tekst en uitleg te vinden zijn over de robotarm.

Nog niet zeker of krachtmetingsberekeningen hier ook in zullen worden toegevoegd.

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
* PET: stijf maar licht van gewicht materiaal dat eveneens sterk en schobestendig is. Is recycleerbaar en laat geen vuile geuren vrij bij hoge temperaturen.

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
