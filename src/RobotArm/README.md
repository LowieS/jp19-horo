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