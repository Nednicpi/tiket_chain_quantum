import hashlib, time
print("=== TIKET CHAIN QUANTUM MINER ===")
tiket = input("ID Tiket: ").strip()
nonce = 0
start = time.time()
print(f"Mining {tiket} target 0000...")
while True:
    data = f"{tiket}{nonce}"
    h = hashlib.sha256(data.encode()).hexdigest()
    if h.startswith("0000"):
        print(f"\n✅ KETEMU!")
        print(f"{tiket} Nonce:{nonce} Hash:{h}")
        print(f"Waktu: {time.time()-start:.2f}s")
        break
    nonce+=1
    if nonce % 50000 == 0:
        print(f"{nonce} hash: {h[:12]}...")
