import pandas as pd
import re

FILE_PATH = r"C:\Users\syadi\Documents\Riliv Intern\Raw Data.xlsx"
OUTPUT_PATH = r"C:\Users\syadi\Documents\Riliv Intern\StudyCase_Hasil_Clean.xlsx"

df = pd.read_excel(FILE_PATH)

question_cols = sorted([c for c in df.columns if str(c).startswith("Question")],
                       key=lambda x:int(re.findall(r"\d+",x)[0]))
response_cols = sorted([c for c in df.columns if str(c).startswith("Response")],
                       key=lambda x:int(re.findall(r"\d+",x)[0]))

mapping = {
    "Age":"Usia","Usia":"Usia",
    "Gender":"Gender","Jenis Kelamin":"Gender",
    "Business Entity":"Perusahaan","Perusahaan":"Perusahaan",
    "Nama Perusahaan":"Perusahaan","Nama perusahaan":"Perusahaan",
    "Company Code":"Kode Perusahaan","Company code":"Kode Perusahaan",
    "Kode perusahaan":"Kode Perusahaan","Kode Perusahaan":"Kode Perusahaan",
    "Divisi":"Divisi","Departemen":"Divisi","Departemen/Divisi":"Divisi",
    "Unit Kerja":"Divisi","Divisi/Unit Kerja":"Divisi",
    "Work Division":"Divisi","Work division":"Divisi",
    "Counselling Topic":"Topik","Counselling topic":"Topik",
    "Topik":"Topik","Topik Konsultasi":"Topik",
    "Topik permasalahan yang ingin dibahas pada sesi konseling":"Topik",
    "Topik permasalahan yang ingin dibahas":"Topik",
    "Counselling Service of Choice":"Layanan",
    "Counseling Service of Choice":"Layanan",
    "Pilihan layanan konseling":"Layanan",
    "Pilihan Layanan Konseling":"Layanan",
    "Pilih layanan konseling":"Layanan",
    "Layanan konseling":"Layanan",
    "Bahasa yang digunakan saat konsultasi":"Bahasa",
    "Nomor WhatsApp":"Nomor WhatsApp","Nomor Whatsapp":"Nomor WhatsApp",
    "Nomor Whatsapp Aktif":"Nomor WhatsApp","Nomor Whatssapp":"Nomor WhatsApp",
    "Nomor Whattsapp":"Nomor WhatsApp",
    "Gambaran Singkat Permasalahan":"Gambaran Permasalahan",
    "Gambaran permasalahan":"Gambaran Permasalahan",
    "Gambaran singkat permasalahan":"Gambaran Permasalahan",
    "Gambaran singkat permasalahan (Opsional)":"Gambaran Permasalahan",
}

rows=[]
unknown=set()

for _,row in df.iterrows():
    rec={}
    for c in df.columns:
        if not str(c).startswith("Question") and not str(c).startswith("Response"):
            rec[c]=row[c]
    for qcol,rcol in zip(question_cols,response_cols):
        q=row[qcol]
        if pd.isna(q):
            continue
        q=str(q).strip()
        key=mapping.get(q,q)
        if key==q and q not in mapping:
            unknown.add(q)
        rec[key]=row[rcol]
    rows.append(rec)

clean=pd.DataFrame(rows)
clean.to_excel(OUTPUT_PATH,index=False)

print("Selesai")
print("Output:",OUTPUT_PATH)
print("Jumlah baris:",len(clean))
print("Jumlah kolom:",len(clean.columns))
if unknown:
    print("\\nPertanyaan yang BELUM termapping:")
    for u in sorted(unknown):
        print("-",u)
