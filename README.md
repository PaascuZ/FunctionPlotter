# Progetto Numerica: Plotter Radici di Funzioni

## Descrizione
Questo progetto è un tool interattivo per analizzare funzioni matematiche e calcolare i loro zeri utilizzando metodi numerici. Consente di:

- Inserire una funzione matematica personalizzata.
- Calcolare gli zeri della funzione tramite vari metodi numerici.
- Visualizzare graficamente la funzione e gli zeri trovati.
- Esplorare intervalli specifici o analizzare un intervallo generale.

Il progetto è pensato per essere intuitivo, educativo e flessibile, rendendolo ideale per studenti, appassionati di matematica e professionisti.

---

## Caratteristiche Principali

### Supporto per Metodi Numerici
- **Metodo della Secante**
- **Metodo di Newton-Raphson (Tangente)**
- **Metodo di Bisezione**
- **Metodo di Regula Falsi**

### Grafico Interattivo
- Visualizzazione degli zeri trovati.
- Grafico degli assi cartesiani (x e y) per un contesto visivo migliore.

### Derivata Automatica
- Calcolo simbolico della derivata della funzione inserita.

---

## Requisiti
Assicurati di avere installate le seguenti dipendenze:

- **Python 3.8+**
- Librerie Python:
  - `plotext`
  - `numpy`
  - `sympy`

Puoi installarle utilizzando pip:
```bash
pip install plotext numpy sympy
```

---

## Come Usarlo

1. **Esegui il programma**:
   ```bash
   python main.py
   ```

2. **Inserisci la funzione**:
   - Puoi usare notazione Python (es. `x**2` per \(x^2\)).
   - Usa `^` per potenze e il programma la trasformerà automaticamente (es. `x^2` → `x**2`).

3. **Scegli il metodo**:
   - Secante, Newton-Raphson, Bisezione o Regula Falsi.

4. **Specifica un intervallo** o analizza l'intero dominio:
   - Puoi calcolare uno zero specifico o cercare più zeri in un intervallo predefinito.

5. **Visualizza il risultato**:
   - Gli zeri trovati vengono stampati in console.
   - Scegli se visualizzare un grafico con la funzione e gli zeri trovati.

---

## Esempio di Esecuzione

```text
Insert function: x^3 - 2*x + 1
Derivata: 3*x**2 - 2
Vuoi usare il metodo della Secante (S), Tangente (T), Bisezione (B) o Regula Falsi (R)? [S/T/B/R]: T
Vuoi fornire un intervallo specifico? (y/n): y
Inserisci x0: -2
Inserisci x1: 0
Zeri trovati:
Zero 1: -1.0000
Vuoi plottare la funzione con gli zeri trovati? (y/n): y
```

### Grafico Output
Il programma genera un grafico simile a questo:

- La funzione viene rappresentata graficamente.
- Gli zeri sono evidenziati in rosso.
- Gli assi cartesiani aiutano a visualizzare meglio il contesto.

---

## Struttura del Progetto

- `main.py`: File principale che contiene il programma.
- `README.md`: Documentazione del progetto.

---

## Contributi
Siamo aperti a contributi! Sentiti libero di:

- Segnalare problemi.
- Proporre nuove funzionalità.
- Contribuire con codice tramite pull request.

---

## Licenza
Questo progetto è distribuito sotto la licenza **MIT**. Sentiti libero di utilizzarlo e modificarlo come desideri.
