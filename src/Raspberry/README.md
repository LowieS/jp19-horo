# MQTT

We hebben in dit project gekozen om de verbindingen tussen alle toestellen te doen met MQTT. Dit omdat het ons het gemakkelijkste leek om alles met 1 protocol te doen en over wifi wat sneller en betrouwbaarder is als bluetooth.

## Wat is MQTT?

MQTT is een Client Server publish/subcribe messaging transport protocol. Het is een licht, open, gemakkelijk en gemaakt om gemakkelijk te implementeren. Deze karaktereigenschappen maken het ideaal om ge gebruiken in heel veel situaties, inclusief omgeving met een beperkte mogelijkheid om te communiceren zoals bij Machine to Machine(M2M) en IOT.

De voordelen van MQTT zijn:
* gemakkelijk om te implementeren
* makkelijk schaalbaar
* neemt weinig bandbreedte van het netwerk

Het MQTT protocol is gebaseerd op het TCP/IP.

## Hoe werkt MQTT
### Het publish/subcribe patroon
De publish/subcribe patroon (pub/sub) geeft een alternatief voor de traditionele client-server architectuur.In de traditionele client-server architectuur, communiceert de client direct met het eindpunt. De publisher en subcriber staan nooit direct met elkaar in verbinding. De connectie wordt mogelijk gemaakt door de broker. De taak van de broker is de inkomende berichten filteren en deze afleveren aan de juiste subscribers. De connectie is altijd tussen één client en de broker.

#### Publish
Als een client verbonden is met een broker kan deze berichten publishen. Elke bericht moet een topic hebben dat de broker kan gebruiken om het bericht naar de geïnteresseerde clients te verzenden.

#### Subcribe
Een client moet verbonden worden met de broker anders heeft het geen zin om berichten te verzenden als niemand deze ontvangt. Om berichten te krijgen van een bepaalde topic moet de client een subcribe bericht sturen naar de broker.
Een client kan ook altijd unsubcribe van een topic als het geen berichten meer wil ontvangen in verband met een topic. Hiervoor moet de client een unsubcribe bericht schrijven naar de broker.

#### Topics
De broker gebruikt topics voor het filteren van berichten(topics) voor iedere connectie. De topics kunnen bestaan van één of meerdere topics levels. Elk level is gescheiden door een forward slash (dit worde de topic level separator genoemd).

> myhome/groundfloor/livingroom/temprature
> - Dit is een voorbeeld van ene topic met meerdere levels

De client moet de topics niet creëren voor dat ze er iets op kunnen publishen of aan kunnen subcriben. De broker accepteert elke geldige topic.
Merk op dat elke topic minstens één karakter moet hebben en ze geen spaties mogen bevatten. Ze zijn ook hoofdletter gevoelig.

## Waarom MQTT
We hebben voor mqtt gekozen omdat dit een makkelijke manier is om alle apparaten met elkaar te verbinden. We kunnen hierdoor ze allemaal berichten tegelijk sturen of apart door met verschillende topics te werken.

###structuur van de MQTT
#### basis project (zonder input van de hololens)
Hierbij is er enkel een verbinding nodig tussen de realsense camera en de robotarm. Wat we willen verwezelijken is dat van de objecten die de realsense detecteert we de 
