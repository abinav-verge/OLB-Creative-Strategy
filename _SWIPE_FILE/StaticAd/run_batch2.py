import os, csv, json

base_dir = "D:/0 Ecom Clients/Olb/OLB-Creative-Strategy/_SWIPE_FILE/StaticAd/Norse"
csv_path = os.path.join(base_dir, "rename_log.csv")
json_path = os.path.join(base_dir, "taxonomy_log.json")
timestamp = "2026-02-25"

batch1_suffix_updates = [
    ("Norse_SolutionAware_SocialProof_Testimonial_Raw_TOF_Bold_NewParent.jpg", "Norse_SolutionAware_SocialProof_Testimonial_Raw_TOF_Bold_NewParent_01.jpg"),
    ("Norse_SolutionAware_Identity_Branded_Branded_TOF_Bold_HealthConscious.jpg", "Norse_SolutionAware_Identity_Branded_Branded_TOF_Bold_HealthConscious_01.jpg"),
    ("Norse_ProblemAware_EmotionalResonance_Branded_Branded_TOF_Empathetic_NewParent.jpg", "Norse_ProblemAware_EmotionalResonance_Branded_Branded_TOF_Empathetic_NewParent_01.jpg"),
]

for old, new in batch1_suffix_updates:
    src = os.path.join(base_dir, old)
    dst = os.path.join(base_dir, new)
    try:
        os.rename(src, dst)
        print("UPDATED:", old, "->", new)
    except Exception as e:
        print("ERROR updating", old, ":", e)

existing_rows = []
with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        existing_rows.append(dict(row))

for row in existing_rows:
    for old, new in batch1_suffix_updates:
        if row["new_filename"] == old:
            row["new_filename"] = new
            break
