from Bio import SeqIO
file_path = r"C:\Users\user\Desktop\1 семестр\Программирование\example cds.gb"
entries = []
for record in SeqIO.parse(file_path, "genbank"):
    for feature in record.features:
      if feature.type == "CDS":
        seq = str(feature.extract(record.seq)).upper()
        gc_content = (seq.count('G') + seq.count('C')) / len(seq) if seq else 0.0
        desc = record.description or record.id
        entries.append((gc_content, f"{record.id}: {desc}, GC = {gc_content}"))

entries.sort()
for gc, entry in entries:
    print(entry)
