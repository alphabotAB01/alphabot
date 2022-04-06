### CLIENT
Questo programma attraverso delle richieste HTTP, comanda autonomamente l'Alphabot evitando gli ostacoli.

#### Funzionamento
Il funzionamento è il seguente:
L'alphabot va avanti e controlla se sono presenti degli ostacoli (utilizzando l'api http://192.168.0.125:5000/api/v1/sensor/obstacles ).
* Se non rileva ostacoli continua ad andare avanti
* Se rileva un ostacolo a destra ferma i motori e gira di alcuni gradi a sinistra
* Se rileva un ostacolo a sinistra ferma i motori e gira di alcuni gradi a destra
* Se rileva un ostacolo da entrambi i sensori ferma i motori e gira di circa 90° a sinistra

Se al successivo controllo la situazione non è stata risolta allora non fermerà più i motori, ma provvederà solo a ruotare di alcuni gradi 
a sinsitra nel caso abbia rilevato l'ostacolo a destra e a destra nel caso abbia rilevato l'ostacolo a sinistra o da entrambi.
