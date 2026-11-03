from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import requests
from pathlib import Path

ROOT = Path(__file__).parent
app = FastAPI(title="Bybit Scalping Bot - Demo")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Public TESTNET market data only. No API credentials and no order endpoints.
BASE = "https://api-testnet.bybit.eu"

@app.get("/api/health")
def health():
    return {"ok": True, "mode": "paper", "orders_enabled": False}

@app.get("/api/tickers")
def tickers():
    symbols = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
    items = []
    for symbol in symbols:
        response = requests.get(
            f"{BASE}/v5/market/tickers",
            params={"category": "spot", "symbol": symbol},
            timeout=8,
        )
        response.raise_for_status()
        payload = response.json()
        if payload.get("retCode") != 0:
            raise RuntimeError(payload.get("retMsg", "Bybit API error"))
        rows = payload.get("result", {}).get("list", [])
        if rows:
            row = rows[0]
            items.append({
                "symbol": symbol,
                "lastPrice": row.get("lastPrice", "0"),
                "change24h": row.get("price24hPcnt", "0"),
            })
    return {"items": items}

@app.get("/")
def index():
    return FileResponse(ROOT / "index.html")

app.mount("/static", StaticFiles(directory=ROOT), name="static")
