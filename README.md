# Bybit Scalping Bot — prototipo web

## Contenuto
- `index.html`: pannello responsive in italiano.
- `server.py`: backend FastAPI che legge prezzi pubblici Spot da Bybit Testnet.
- `requirements.txt`: dipendenze Python.
- `.env.example`: segnaposto per una futura configurazione protetta (non serve in questa demo).

## Avvio (Windows / macOS / Linux)
1. Installa Python 3.10 o superiore.
2. Apri un terminale nella cartella del progetto.
3. Crea un ambiente virtuale:
   - Windows: `py -m venv .venv` poi `.venv\\Scripts\\activate`
   - macOS/Linux: `python3 -m venv .venv` poi `source .venv/bin/activate`
4. Installa: `pip install -r requirements.txt`
5. Avvia: `uvicorn server:app --host 127.0.0.1 --port 8000`
6. Apri `http://127.0.0.1:8000` nel browser.

## Stato e limiti
Questa è una demo di interfaccia configurata per l'host TESTNET europeo `https://api-testnet.bybit.eu`, con lettura di prezzi pubblici. Non esegue strategie, non crea ordini e non necessita di API key. Il pulsante avvia soltanto il registro della simulazione grafica: non equivale a un motore di trading automatico.

Prima di qualsiasi collegamento reale occorrono:
- test strategia e simulazione con dati storici / paper trading realistico;
- verifica che l'accesso API e gli endpoint V5 Spot siano abilitati per lo specifico account Bybit EU e per il relativo ambiente Testnet/Mainnet;
- backend con autenticazione, segreti fuori dal frontend, limiti di rischio, log e kill switch;
- autorizzazione esplicita dell'utente per abilitare gli ordini reali.

Non inserire mai API secret in `index.html`, nel browser, in chat o in repository pubblici. Non abilitare permessi di prelievo.
