import hashlib, sys

def sha256(s):
    return hashlib.sha256(s.encode()).hexdigest()

tiket_id = input("Masukkan ID TIKET (contoh: TIKET-COLDPLAY-001): ").strip()

# CEK ANTI-DOUBLE SEBELUM MINING
with open("ledger.txt") as f:
    ledger = f.read()
    if tiket_id in ledger:
        print(f"❌ GAGAL! {tiket_id} SUDAH ADA DI LEDGER! Tidak bisa ditambang lagi!")
        print("Ini mencegah cloning / copy paste.")
        sys.exit(1)

print(f"Mining {tiket_id}...")
nonce = 0
while True:
    h = sha256(tiket_id + str(nonce))
    if h.startswith("0000"):
        print(f"✅ KETEMU!")
        print(f"{tiket_id} Nonce:{nonce} Hash:{h}")
        # LANGSUNG CATAT KE LEDGER
        with open("ledger.txt","a") as f:
            f.write(f"{tiket_id} Nonce:{nonce} Hash:{h}\n")
        print("Sudah dicatat di ledger.txt - Push sekarang!")
        break
    nonce += 1
