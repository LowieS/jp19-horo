**Hololens Documentatie**

**inleiding :**

Als gebruiker wil je een blok opnemen met een robot arm. Deze blokken worden
waargenomen door een intel realsense die dan deze informatie doorstuurt naar de
robot arm. 

> TODO: wat is realsense

Hierbij willen we nog een input van de user insteken. Deze input
wordt verwerkt via een Microsoft Hololens 1 en doorgestuurd naar de robot arm om
zo het juiste blokje op te nemen.

> TODO: geef voorbeeld van wat user input is

![](media/83b10f5c9c219c4e822b426620acda8d.png)

**Wat:**

We maken gebruik van een Hololens dit is een device(bril) die hologrammen
projecteren op de glazen van de bril. Deze hologrammen worden geprojecteerd over
de echte wereld. Dit houdt in dat de gebruiker de echte wereld nog kan blijven
zien en dat de hologrammen reageren met die wereld. Ook kan de gebruiker zelf
omgaan met de hologrammen door ze te kunnen selecteren en verslepen. Dit wordt 
mixed-reality genoemd. De hololens heeft een aantal basis features die worden gebruikt:

1.  Gesture manager: dit is een feature van de hololens dat handbewegingen
    analyseert en omzet in input dat hij kan verwerken. 
    
    De handbewegingen zijn:
    - airtab > TODO geef definitie van deze handbewegingen!
    - bloom
    - gaze

    ![D:\\school\\2ea4\\HORO\\doc\\mixed-reality-met-microsoft-hololens-11-638.jpg](media/3d7ba9116a30d182120839e3a690e649.jpg)

2.  Spatial mapping: Dit geeft een digitale 3D map van de omgeving. Dit geeft de
    gebruiker de vrijheid om hologrammen te laten plaatsen op echte elementen
    van de echte wereld vb: (tafels, vloer en stoelen). Deze map blijft statisch
    en wordt geüpdatet door de hololens en heeft een eigen coördinaten stelsel
    die ook statisch word bijgehouden.

    ![](media/5539c94a01b495840e72c7f31433c663.jpg)

3.  Voice Input: De hololens heeft een ingebouwd voice input lib die luistert
    via zijn micro. Als de gebruiker deze lib aanzet kan hij keywords instellen
    en de hololens reageert hierop.

**Hoe:**

Het project is gemaakt in unity 2017.4.20 met gebruik van VS2017 c\# scripts een
goede start voor een hololens project Cursus:
<https://docs.microsoft.com/en-gb/windows/mixed-reality/holograms-101>.

> TODO: beschrijf hoe je unitiy project moet configureren: vanaf opstart unity + welke plugins moet je installeren

De stappen en features van dit project zijn:

-   De eerste stap was implementatie van een cursor. Deze cursor is een 3D
    object in unity dat een script heeft WorldCursor. Dit script zend een
    raycast uit als deze een object raakt verplaatst het script de cursor naar
    de locatie van de raycast intersectie. Ook regelt het script de
    draairichting van de cursor zodat deze op de oppervlakte ligt van het
    object.

-   Daarna de implementatie van spatial mapping dit is een object voorzien door
    microsoft met een script dat dit implementeert

-   Als derde stap de implementatie van air-tab op de cursor dit doen we door
    code bij te voegen bij het World cursor script. Deze code maakt een nieuwe
    gestureRecognizer aan deze zal kijken naar eventuele gestures. Als er de
    gebruiker airTab gebruikt zal het dit herkennen en de code in het event
    uitvoeren.

    ![](media/16fff27520838b4efb46b97756adce30.png)

-   Nadat de gesturemanager geconfigureerd is wordt ervoor gezorgd dat de
    coördinaten kunnen worden verkregen worden van de cursor wanneer er airtab
    gebruikt wordt. Als het programma een airtab registreert dan worden de
    coördinaten gelogd.

    ![](media/be2007e27743d37792379238490244ff.png)

    ![Afbeeldingsresultaat voor xyz](media/329fd3b89755d3f0bb60404a13f865f2.jpg)

    dit is de xyz oriëntatie van de hololens

    Deze code geeft een 3D vector terug. Zo zijn er een aantal metingen gedaan
    om te bepalen of dat de coördinaten zouden veranderen moest de gebruiker
    bewegen en dan terug keren naar dezelfde locatie. Dit leek zo te zijn

>   meting 1: meeting van een vlak zodat er kan bepaald worden hoe accuraat deze
>   metingen zijn

(-0.4, -0.2, 0.8) punt 1

(-1.7, -0.2, 1.5) punt 2

(-0.8, -0.2, 1.8) punt 3

(-1.4, -0.2, 0.5) punt 4

meting 2: meeting van een positie na rondwandelen in de ruimte

(0.4, -0.7, 1.2) positie van de test meting

(0.1, -0.7, -3.7) meting ongeveer 3 meter weg van de test positie

(0.4, -0.7, 1.2) meting na terugkeer test positie

-   Nu dat de coördinaten beschikbaar zijn kunnen deze gebruikt worden om een
    algoritme te maken. Dit algoritme zal bepalen waar een blok gaat gezet
    worden. Door 2 airtabs uit te voeren op de linkse boven hoek en rechtse
    onder hoek van het werk veld kunnen de lengte en de hoogte berekend worden.
    Met deze waarden kunnen we berekenen waar dat het blokje gegenereerd zal
    worden als we een percentage krijgen van de afstand tegenover de linkse
    boven hoek.

![](media/3855fff6967339fa1b4b86d38a0a5e7d.png)

-   Als het algoritme is uitgevoerd en de locatie is berekend zal deze vector
    worden doorgestuurd. De bestemming van deze vector is het hologram dat de
    locatie zal aanduiden in de omgeving. Dit doen we door communicatie tussen
    het script van de cursor en dat van de hologram door gebruik te maken van
    delegates.

    ![](media/bac7b97111058721b70c0b4a95cb600b.png)

    ![](media/7e6ca465c7f5b781c43b413a786bf168.png)

    Als hij deze vector krijgt zal hij de positie van dit object zetten naar
    deze positie.

-   Om de gebruiker feedback te geven en een configuratie modus te maken wordt
    er op de airtab van het werk veld ook een speciale marker geplaatst. Deze
    marker wordt ook via dezelfde manier als hierboven verplaatst naar de
    locatie van de airtab. Ook moet de gebruiker twee keer airtab gebruiken voor
    hij uit deze configuratie modus gaat.

    ![](media/258087991ca1e7d3592c3cb53b0d5760.png)

-   De gebruiker heeft ook de optie om het configuratie proces opnieuw te
    starten. Dit is gedaan met een voice commando “Reset”. Hiervoor is dan ook
    een delegate gemaakt waarop alle scripts reageren en hun eigen te resetten.
    Het voice commando maakt men door een keywordRecognizer aan te maken en een
    methode te maken en deze te laten gebruiken door deze keywordRecognizer. Als
    dit gebeurt is kunnen de keyword of voice commando’s aangemaakt worden. Hier
    wordt de code dan ingevoerd die de delegate aanroept.

    ![](media/47d3adf8ec80344ac10c9be8695b98c1.png)

    ![](media/da26ecc3c3a3ce551e280e8488534b1b.png)

-   Voor de gebruiker een makkelijk configuratie proces te geven word er een
    textfield aan de main camera gehangen. Dit textfield laat de coördinaten van
    de airtabs zien en waar je zit in de configuratie.

**Waarom:**

In een praktische toepassing is het altijd nodig dat de gebruiker aangeeft welk
blok hij wil opnemen met de robot arm. Dit is gerealiseerd door gebruik te maken
van een hololens zo kan de gebruiker ook feedback krijgen en eventuele
simulaties zien.

Bij deze opdracht is er beslist om gebruik te maken van een configuratie modus
om zo het werkveld te bepalen. Dit is zo beslist omdat de hololens niet zo goed
is in herkennen van objecten. Een latere uitbreiding zou kunnen zijn dat we in
de configuratie stap vermijden dat we airtab moeten gebruiken op de hoekpunten.
Dit zou dan kunnen gedaan worden met markers. Deze markers zouden dan
automatisch de hoekpunten herkennen en zo het veld te genereren.
