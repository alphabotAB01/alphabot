## Alphabot 3.0

In questa versione del progetto dell'Alphabot abbiamo utilizzato una comunicazione client-server attraverso il **protocollo HTTP**.

---

### Funzionamento

In questo progetto il client invia un comando al server che lo esegue fino a quando non gliene viene dato un altro, eccetto per il comando *destra* e *sinistra* dove viene effettuata una rotazione di 45°.

I **comandi** che possono essere dati sono:
| Nome comandi  | Descrizione
| :------------ | :-------- 
| ` w`          | Procede avanti  
|` s`           | Procede indietro 
|` a`           | Gira su se stesso verso sinistra
|` d`           | Gira su se stesso verso destra
|` q`           | Si ferma  

