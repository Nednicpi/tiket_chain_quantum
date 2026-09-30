import hashlib, sys, os

def sha256(s):
    return hashlib.sha256(s.encode()).hexdigest()

# CEK APAKAH INI GENESIS (LEDGER KOSONG)
is_genesis = True
try:
    with open("ledger.txt") as f:
        content = f.read().strip()
        if content and len([l for l in content.split('\n') if l.strip() and not l.strip().startswith("#")]) > 0:
            is_genesis = False
except FileNotFoundError:
    open("ledger.txt","w").close()

if is_genesis:
    tiket_id = "TIKET-GENESIS-000"
    print(f"=== GENESIS BLOCK DETECTED ===")
    print(f"Sistem otomatis membuat tiket pertama: {tiket_id}")
else:
    tiket_id = input("Masukkan ID TIKET (contoh: TIKET-COLDPLAY-001): ").strip()
    # ANTI DOUBLE
    with open("ledger.txt") as f:
        if tiket_id in f.read():
            print(f"❌ {tiket_id} SUDAH ADA! Tidak bisa ditambang lagi!")
            sys.exit(1)
print(f"Mining {tiket_id}...")
nonce = 0
while True:
    h = sha256(tiket_id + str(nonce))
    if h.startswith("0000"):
        print(f"KETEMU!")
        print(f"{tiket_id} Nonce:{nonce} Hash:{h}")
        with open("ledger.txt","a") as f:
            f.write(f"{tiket_id} Nonce:{nonce} Hash:{h}\n")
        print("-> Genesis berhasil! Push sekarang!")
        break
    nonce += 1
