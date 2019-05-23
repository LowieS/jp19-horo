**ROS**

Het Robot operating system bestaat uit een I2c verbinding tussen de Raspberry-Pi
en de arduino om de robot arm te besturen via de gewenste coordinaten. De
Raspberry-Pi zal coordinaten aankrijgen van de Realsense camera door middel van
een MQTT channel en deze doorsturen naar de Arduino. De Arduino zal deze waardes
omrekenen naar servo graden via een library om zo te bepalen of deze positie
bereikbaar is. Indien deze bereikbaar is zal de arduino, via een shield dat
ontworpen is om verschillende servo motoren tegelijk aan te sturen, de arm zijn
servo motoren op deze waardes plaatsen.

**Raspberry Pi**

De Raspberry-Pi is in ons geval het hoofd van onze verbinding. De Raspberry-pi
is een mini computer met een GPIO pinout die we kunnen aansturen doormiddel van
scriptjes. In dit geval zorgt ons scriptje voor een stabiele en vertrouwbare I2c
verbinding met de Arduino. Via deze I2c verbinding stuurt de Raspberry-Pi de
aangekregen coördinaten door naar de Arduino.

Bij onze zelf ontworpen robot arm kunnen we de arduino achterwegen laten en
kunnen we alle berekeningen voor de servos ook doen op de Raspberry-Pi, bij ons
prototype arm/test robot arm hebben we de arduino shield nodig en is het
praktischer om de Arduino te verbinden met de Raspberry-Pi in plaats van andere
manieren te zoeken.

**Arduino**

De Arduino is een soort microcontroller en is in ons geval de
werkende/aansturende kracht van onze robot arm op dit moment. De Arduino zal
constant luisteren naar zijn I2c poorten om te horen of er een waarde wordt door
gestuurd naar hem. Indien hij zijn 14 bytes heeft aangekregen, zal hij via het
programma dat erop staat en de 14 bytes, eerst elke positie byte omvormen naar
gehele getallen (dus de 3 bytes optellen en kijken naar de sign byte) en dan
deze 3 gehele getallen omvormen naar servo motor posities via een library die
driehoeks wiskunde uitvoert.


De Arduino kunnen we in ons afgewerkte project geheel laten vallen. De
Raspberry-Pi zelf is helemaal instaat om zelf deze berekeningen uit te voeren en
zelf de waardes naar de Robot arm door te sturen. Op dit moment is de Arduino
enkel in gebruik omdat het meegekregen shield voor onze test robot arm gemaakt
was voor de Arduino en we niet weten of we de Raspberry-Pi kunnen gebruiken om
de shield aan te sturen. Later zullen we dus de library proberen over te zetten
naar Raspberry.

**I2c**

Het I2c data transmission protocol is een protocol dat ervoor zorgt dat 1 master
meerdere slaves kan aansturen via dezelfde pinnen. Hierdoor als we later
bijvoorbeeld willen afschakelen van de Arduino (bij onze zelf ontworpen robot
arm) is het nog steeds mogelijk om meerdere servo motoren tegelijk aan te
sturen.

We sturen in totaal 14 bytes door. Deze bytes bestaan uit 3 X positie bytes, 3 Y
positie bytes, 3 Z positie bytes,3 bytes om te bepalen voor elke coördinaat of
deze positief of negatief is, 1 byte voor de grijp hoek waaronder deze het
object moet opnemen en tenslotte 1 byte om de bepalen hoeveel kracht de greep
nodig heeft (bijvoorbeeld 0 zou hier klauw helemaal open zijn en 255 zou
helemaal dicht zijn).

Via deze 11 bytes kan de Arduino perfect berekenen welke PWMs de servo motoren
nodig hebben om de gewenste coördinaten te bereiken.

I2c is een snelle en vertrouwbare manier om data te versturen tussen onze 2
microcontrollers in dit geval. Door de snelheid van I2c is het mogelijk om onze
robot arm in real time al deze bewegingen te laten doen.

**De Arm**

De Robot arm zelf bestaat op dit moment uit 6 servo motoren. De eerste dient om
de robot arm in zijn geheel te draaien, de 2de servo dient om de arm ten
opzichte van zijn grond platform hoger of lager te laten grapen, de 3de servo is
hetzelfde als de 2de servo maar dan ten opzichte van het midden deel van de arm,
de 4de servo dient om klauw een te plaatsen in een gewenste hoek, de 5de servo
dient heeft als nut de klauw te kunnen draaien rond zijn eigen as terwijl de
laatste servo de klauw kan open zetten of sluiten.

Alle 6 de servo motoren krijgen hun waardes via de Arduino maar enkel de eerste
4 motoren hun waardes zullen berekent worden via de library. De 5de servo motor
zijn waarde zullen we zelf moeten bereken afhankelijk van de hoek die het blokje
heeft ten opzichte van de arm en de 6de servo zullen we gewoon moeten kieze
afhankelijk van de arm zijn opdracht op dat moment (moet hij een blokje opnemen
of een blokje los laten).
