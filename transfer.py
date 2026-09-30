cat > transfer.py << 'PY'
import sys

# Format: python transfer.py TIKET-GENESIS-000 Nednicpi Budi

if len(sys.argv)!= 4:
    print("Pakai: python transfer.py ID_TIKET OWNER_LAMA OWNER_BARU")
    sys.exit()

tiket_id, owner_lama, owner_baru = sys.argv[1], sys.argv[2], sys.argv[3]

with open("ledger.txt", "r") as f:
    lines = f.readlines()

found = False
new_lines = []
for line in lines:
    if tiket_id in line and f"OWNER:{owner_lama}" in line:
        found = True
        # ganti owner, NOTE harga terserah user, gak divalidasi
        new_line = line.replace(f"OWNER:{owner_lama}", f"OWNER:{owner_baru}")
        new_lines.append(new_line)
        print(f"TRANSFER SUKSES: {tiket_id} {owner_lama} -> {owner_baru}")
    else:
        new_lines.append(line)

if not found:
    print(f"GAGAL: Tiket {tiket_id} bukan milik {owner_lama} atau tidak ada")
    sys.exit()

with open("ledger.txt", "w") as f:
    f.writelines(new_lines)

print("Tercatat di ledger. Jangan lupa git commit & push!")
PY
