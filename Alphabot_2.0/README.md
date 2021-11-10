## ALPHABOT 2.0
In questo progetto il server esegue un comando che gli viene dato da un client TCP.
Il client può inviare due tipi di comandi:
  * *comandi diretti*
  * *sequenze memorizzare precedentemente*

#### Comandi diretti
I comandi diretti hanno la seguente **sintassi**:
                *`comando* : * tempo di esecuzione in millisecondi*`  
                
I **comandi** che possono essere dati sono:
| Nome comandi  | Descrizione
| :------------ | :-------- 
|` w`           | Va avanti  
|` s`           | Va indietro    
|` a`           | Gira su se stesso verso sinistra  
|` d`           | Gira su se stesso verso destra
|` q`           | Si ferma  
