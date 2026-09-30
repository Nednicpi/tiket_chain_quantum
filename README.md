
## 🌍 Global Open API for Event Organizers

Berbagai Event Organizer di seluruh dunia dapat mengakses API untuk membangun aplikasi tiketing yang terhubung langsung ke blockchain ini.

### API Endpoints (Public)

**Base URL:** `https://api.tiket-chain-quantum.org` *(coming soon, sekarang via GitHub Raw)*

- `GET /ledger.txt` - Ambil semua tiket valid (100 Juta max)
- `GET /validate?ticket=TIKET-XXX&nonce=xxx&hash=xxx` - Validasi 1 tiket
- `POST /mine` - Submit tiket baru hasil mining PoW
- `GET /supply` - Cek sisa supply global (Terpakai / Sisa)

### Untuk Developer EO

```javascript


fetch('https://raw.githubusercontent.com/tiket_chain_quantum/main/ledger.txt')
