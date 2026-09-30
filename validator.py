import hashlib

TARGET = "0000"

def sha256(s):
    return hashlib.sha256(s.encode()).hexdigest()

print("=== AUDIT TRANSPARAN TIKET_CHAIN_QUANTUM ===")

try:
    with open("ledger.txt") as f:
        lines = [l.strip() for l in f if l.strip() and not l.strip().startswith("#")]
    if not lines:
        print("ledger.txt masih kosong / genesis - OK")
    else:
        for i, line in enumerate(lines, 1):
            parts = line.split()
            tiket = parts[0]
            nonce = parts[1].split(":")[1]
            h_claim = parts[2].split(":")[1]
            h_real = sha256(tiket + nonce)
            if h_real!= h_claim or not h_real.startswith(TARGET):
                print(f"FAIL Baris {i}: {line}")
                exit(1)
            print(f"OK Baris {i}: {tiket}")
        print(f"✅ {len(lines)} tiket VALID")
except FileNotFoundError:
    print("ledger.txt belum ada - OK untuk genesis")

print("=== SELESAI ===")
