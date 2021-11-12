# Widerstands-Wirrwarr

Das Weihnachtsgeschäft steht vor der Tür, aber das neue MEDION Tablet ist noch zu teuer. Bei einem Design Review stellt sich heraus, dass der ODM in China den Schaltplan zu kompliziert angelegt hat. An einigen Stellen werden verschachtelte Widerstandsnetzwerke genutzt, die aus zu vielen Bauteilen bestehen.

Als kleine Erinnerung: Widerstandsnetzwerke bestehen aus Widerständen, die in Reihe oder parallel geschaltet sind. Für jeden der beiden Fälle kann man einen Gesamtwiderstand wie folgt berechnen und die beiden Widerstände durch einen einzelnen ersetzen:

1) Reihenschaltung

    Formel: Rges=Ra+Rb   
    Syntax: \<Ra-Rb>

2) Parallelschaltung

    Formel: Rges=1/(1/Ra+1/Rb)   
    Syntax: \<Ra/Rb>

So lässt sich zum Beispiel das folgende Widerstandsnetzwerk   
R0=<50/<20-30>>   
reduzieren auf einen einzelnen Widerstand von 25 Ohm.

Schaut Euch die Datei mit den Widerstandsnetzwerken R1 bis R12 an und optimiert diese, so dass nur jeweils ein einzelner Gesamtwiderstand übrig bleibt. Rundet das Ergebnis auf 10 Ohm.

Könnt Ihr das Weihnachtsgeschäft von MEDION retten? Es steht viel auf dem Spiel! Die Firma zählt auf Euch! :)