# Analyse

## Probleemstelling

### Hoofdprobleem
We willen een robotarm maken en hiermee kunnen werken. Deze robotarm moet bestuurbaar zijn met de hololens en de digitale blokjes kunnen detecteren aan de hand van intel realsense. Het is de bedoeling dat de handelingen die de robotarm gaat doen getoond zullen worden via de hololens voordat deze in werkelijkheid plaatsvinden.
* Maken van Robotarm
* Robotarm laten bewegen
* Robotarm objecten laten oppakken.
* Visualiseren op hololens
* robotarm besturen met de hololens
* Programmeren van de robotarm
* Detecteren van objecten met Intel realsense
* Connectie tussen  robotarm en hololens
* Connectie tussen de hololens en Intel realsense 
 



## Mindmap

Maak een mindmap met alle functionaliteit die je wilt voorzien in je project.
Dit zal je startpunt zijn voor een verdere analyse.

## Beschrijving

Het doel van het project is om de robotarm als een COBOT te kunnen laten functioneren in combinatie met de Hololens. Om dit voor elkaar te krijgen gaan we gebruik maken van een Raspberry Pi, een arduino uno, een Hololens en een Intel Realsense.
De camera's van de Intel Realsense worden gebruikt voor het opvangen van de bewegingen. Deze bewegingen zijn afkomstig van zowel de persoon die de opdracht uitvoert alsook de bewegingen die gemaakt worden door de robot. De camera van de Hololens zal ook gebruikt worden om de bewegingen van de gebruiker in real time te volgen. Zo krijgen we 2 camera's die dan de bewegingen van de gebruiker kunnen opvolgen en 1 die de bewegingen van de robot zal kunnen opvolgen.
De Intel Realsense en de Hololens worden gekoppeld aan een Raspberry Pi. Deze zal de gegevens die worden verzameld door de camera's koppelen aan wat er in het virtuele beeld (dat gegenereerd en meegegeven wordt door de Hololens) aan het gebeuren is. De Pi is ook nog verbonden met een arduino uno die als aansturing dient voor de shield van de robot.
** INSERT SHIELD
De robot arm zal dan de virtuele blokken kunnen detecteren en dan is het de bedoeling dat met behulp van de interne servo motoren de robot kan draaien volgens 3 assen. Natuurlijk kan de robotarm deze virtuele blokken dan oppakken, verplaatsen en bewerken (?). De grijphand van de robot kan dus ook klemmen en lossen met behulp van de interne servo motoren.



Zet hier de beschrijving van je project. Licht de functionaliteit van het project toe.

Minimaal 3000 tekens.

## Hardware analyse

Plaats hier een high level blokdiagram van de hardware. Hierin moet duidelijk worden weergegeven wat de verschillende delen zijn en hoe deze met elkaar verbonden zijn. Geef ook een woordje uitleg bij het schema

## Software analyse

Plaats hier een flow-chart van de software. Hierin moet de werking van de software duidelijk worden weergegeven. Voorzie ook de nodige uitleg.

## User stories en Engineering Tasks

Geef hier de userstories en engineering tasks. De beschrijving moet conform zijn met de methode zoals gezien in de lessen  van projectmanagement vn dhr Peeters.

## systeemspecificaties

Geef hier de systeemspecificaties waaruit je de hardware en software kan ontwerpen



