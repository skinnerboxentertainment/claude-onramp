"""Generate deterministic sample files for the exercises. Run from the repo root."""
import os, random, datetime, zlib
random.seed(7)
ROOT = os.path.join(os.path.dirname(__file__), "..", "exercises")

def w(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

# ---------- notes/ : 9 short notes on one topic, with two contradictions ----------
notes = {
 "2026-03-02-kickoff.md": "# Kickoff: neighborhood market website\n\nGoal: a simple site listing the 40 vendors at the Saturday market.\nBudget: 300 dollars. Deadline: end of May.\nDecided: one page, no login, Spanish first, English second.\n",
 "2026-03-09-vendors.md": "# Vendor list status\n\n28 of 40 vendors have sent photos. 12 still missing.\nMaria (bakery) wants her stall listed as 'Panaderia Maria', not 'Maria's Bread'.\nNote: the fruit stall changed owners in February.\n",
 "2026-03-16-design.md": "# Design decisions\n\nColors: green and cream. Font: something readable on phones.\nEach vendor gets: name, photo, 2-line description, WhatsApp button.\nWe will NOT show prices. They change weekly.\n",
 "2026-03-23-budget.md": "# Budget check\n\nDomain 15/yr. Hosting free (GitHub Pages).\nPhotographer for missing photos: 120.\nRemaining: about 165.\nDeadline moved to mid June because of the photographer.\n",
 "2026-04-06-content.md": "# Content rules\n\nDescriptions: max 30 words, written by us, approved by the vendor on WhatsApp.\nPhotos: landscape, no faces of children.\nShow prices for the 5 anchor vendors only, as a trial.\n",
 "2026-04-13-feedback.md": "# Feedback from three vendors\n\nAll three want a map. One wants opening hours per stall.\nMaria says the photo makes her bread look grey. Retake.\nIdea: a 'new this week' box at the top.\n",
 "2026-04-20-tech.md": "# Tech notes\n\nSingle HTML file plus a JSON file of vendors. No build step.\nQR code on each stall pointing to its section.\nBackup: the JSON is also kept in a Google Sheet.\n",
 "2026-05-04-status.md": "# Status\n\n35 of 40 photos done. Map done. Hours: skipped for now.\nStill open: prices trial (5 vendors), 'new this week' box.\nLaunch target: June 14.\n",
 "ideas.md": "# Loose ideas\n\n- Print a poster with the QR code for the market entrance\n- Ask the municipality to link to us\n- A recipe of the week from a vendor\n- Newsletter? Probably too much work for now\n",
}
for name, text in notes.items():
    w(os.path.join(ROOT, "notes", name), text)

# ---------- messy-downloads/ : 40 mixed files ----------
kinds = [("report", ".pdf"), ("invoice", ".pdf"), ("photo", ".jpg"), ("IMG", ".png"), ("data", ".csv"),
         ("notes", ".txt"), ("draft", ".docx"), ("presentation", ".pptx"), ("setup", ".exe"), ("archive", ".zip"),
         ("contract", ".pdf"), ("screenshot", ".png"), ("export", ".csv"), ("readme", ".md")]
base = datetime.date(2025, 11, 3)
for i in range(40):
    stem, ext = random.choice(kinds)
    d = base + datetime.timedelta(days=random.randint(0, 300))
    suffix = random.choice(["", " (1)", "_final", "_v2", "-copy", " - Copy", f"_{d.strftime('%Y%m%d')}", f"{random.randint(1000,9999)}"])
    name = f"{stem}{suffix}{ext}"
    path = os.path.join(ROOT, "messy-downloads", name)
    if ext == ".csv":
        rows = ["date,item,amount"] + [f"{(d - datetime.timedelta(days=k)).isoformat()},item{k},{random.randint(5,400)}" for k in range(random.randint(3, 12))]
        w(path, "\n".join(rows) + "\n")
    elif ext in (".txt", ".md"):
        w(path, f"Downloaded {d.isoformat()}. Placeholder content for {name}.\n")
    else:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(b"PLACEHOLDER-" + name.encode() + b"\n" + bytes(random.getrandbits(8) for _ in range(random.randint(200, 2000))))
    os.utime(path, (datetime.datetime.combine(d, datetime.time(10)).timestamp(),) * 2)

# ---------- receipts/ : 12 minimal real PDFs (text only) ----------
def pdf(lines):
    content = "BT /F1 12 Tf 50 750 Td 16 TL " + " ".join("(" + l.replace("(", r"\(").replace(")", r"\)") + ") Tj T*" for l in lines) + " ET"
    objs = [
        "<< /Type /Catalog /Pages 2 0 R >>",
        "<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        "<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>",
        f"<< /Length {len(content)} >>\nstream\n{content}\nendstream",
        "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    ]
    out = "%PDF-1.4\n"; offsets = []
    for i, o in enumerate(objs, 1):
        offsets.append(len(out.encode("latin-1"))); out += f"{i} 0 obj\n{o}\nendobj\n"
    xref = len(out.encode("latin-1"))
    out += f"xref\n0 {len(objs)+1}\n0000000000 65535 f \n" + "".join(f"{o:010d} 00000 n \n" for o in offsets)
    out += f"trailer\n<< /Size {len(objs)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n"
    return out.encode("latin-1")

vendors = ["Ferreteria Central", "Cafe Luna", "Papeleria Sol", "Uber", "Farmacia Vida", "Super Compro", "Libreria Norte", "Taller Ruiz"]
for i in range(12):
    d = datetime.date(2026, random.randint(1, 8), random.randint(1, 28))
    v = random.choice(vendors); total = round(random.uniform(4, 380), 2)
    items = [(f"Item {k+1}", round(random.uniform(1, 90), 2)) for k in range(random.randint(1, 4))]
    lines = [v, "RECIBO / RECEIPT", f"Fecha: {d.strftime('%d/%m/%Y')}", f"Recibo No. {random.randint(10000, 99999)}", ""] + \
            [f"{n}   {p:.2f}" for n, p in items] + ["", f"TOTAL: {total:.2f}", "Gracias por su compra"]
    path = os.path.join(ROOT, "receipts", random.choice([f"scan{i+1:03d}.pdf", f"IMG_{random.randint(2000,9999)}.pdf", f"receipt ({i+1}).pdf", "documento.pdf" if i == 3 else f"Recibo_{i+1}.pdf"]))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(pdf(lines))

print("samples written under", os.path.abspath(ROOT))
