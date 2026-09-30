import sys

# Format: python transfer.py TIKET-GENESIS-000 Nednicpi Budi [NOTE_HARGA_BEBAS]

if len(sys.argv) < 4:
    print("Pakai: python transfer.py ID_TIKET OWNER_LAMA OWNER_BARU [NOTE]")
    sys.exit()

tiket_id = sys.argv[1]
owner_lama = sys.argv[2]
owner_baru = sys.argv[3]
note = sys.argv[4] if len(sys.argv) > 4 else "harga terserah user"

with open("ledger.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()

found = False
for line in lines:
    if tiket_id in line and f"OWNER:{owner_lama}" in line:
        found = True
        break

if not found:
    print(f"GAGAL: {tiket_id} bukan milik {owner_lama}")
    sys.exit()

# Kita TIDAK hapus history, kita TAMBAH baris baru = decentralized
with open("ledger.txt", "a") as f:
    f.write(f"\n{tiket_id} | TRANSFER from {owner_lama} to {owner_baru} | OWNER:{owner_baru} | NOTE:{note}")

print(f"SUKSES: {tiket_id} {owner_lama} -> {owner_baru} | NOTE:{note}")
