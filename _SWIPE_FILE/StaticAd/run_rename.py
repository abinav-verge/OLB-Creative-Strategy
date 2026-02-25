import os
import csv
import json

base = "D:/0 Ecom Clients/Olb/OLB-Creative-Strategy/_SWIPE_FILE/StaticAd/Norse"

timestamp = "2026-02-25"

# (original_filename, brand, awareness, lever, format, branded_raw, funnel, tone, audience, edge_cases)
renames_data = [
    ("422585428_1561173124618057_4273681970665437027_n.jpg", "Norse", "SolutionAware", "Transformation", "StatCallout", "Raw", "TOF", "Bold", "EmotionalSeeker", ""),
    ("430335164_347325478289766_938460460853448725_n.jpg", "Norse", "SolutionAware", "EmotionalResonance", "UGC", "Raw", "TOF", "Provocative", "EmotionalSeeker", "Format=UGC: rant-style copy voice mimics real-person content"),
    ("439659295_320229687757307_2666825845340136656_n.jpg", "Norse", "ProductAware", "SocialProof", "Testimonial", "Raw", "MOF", "Reassuring", "Skeptic", ""),
    ("447898371_1003939241088446_4287162782158347449_n (1).jpg", "Norse", "SolutionAware", "SocialProof", "Testimonial", "Raw", "TOF", "Bold", "Skeptic", ""),
    ("448630885_1820066891809403_4813353607878452060_n.jpg", "Norse", "SolutionAware", "Identity", "Branded", "Branded", "TOF", "Bold", "HealthConscious", ""),
    ("448641890_796195862705510_2090465759973367700_n.jpg", "Norse", "SolutionAware", "SocialProof", "Testimonial", "Raw", "MOF", "Empathetic", "NewParent", ""),
    ("448774965_1818851365278819_6873626877836685485_n.jpg", "Norse", "SolutionAware", "Transformation", "StickyNote", "Raw", "TOF", "Bold", "EmotionalSeeker", ""),
    ("448792286_1243671613439473_8370630240350158673_n.jpg", "Norse", "ProductAware", "Reciprocity", "StickyNote", "Raw", "MOF", "Bold", "Skeptic", ""),
    ("464013819_1507725476537288_836093697307917632_n.jpg", "Norse", "SolutionAware", "Transformation", "BeforeAfter", "Raw", "TOF", "Bold", "NewParent", ""),
    ("464177306_1618207609104985_1064621534611514735_n.jpg", "Norse", "ProblemAware", "EmotionalResonance", "Branded", "Branded", "TOF", "Empathetic", "NewParent", ""),
    ("464181169_454826387086610_4018723940183252142_n.jpg", "Norse", "ProblemAware", "SocialProof", "Testimonial", "Raw", "MOF", "Reassuring", "HealthConscious", ""),
    ("464188233_434420665983461_6941756418030405399_n.jpg", "Norse", "ProductAware", "Transformation", "BeforeAfter", "Raw", "MOF", "Empathetic", "NewParent", ""),
    ("464192209_8603913463027495_1927437313266727138_n.jpg", "Norse", "SolutionAware", "SocialProof", "Testimonial", "Raw", "TOF", "Bold", "NewParent", ""),
    ("464209313_3038450129627672_7921774548165762323_n.jpg", "Norse", "SolutionAware", "Transformation", "StickyNote", "Raw", "TOF", "Bold", "HealthConscious", ""),
    ("464244402_936937208329598_293151358627083038_n.jpg", "Norse", "ProductAware", "SocialProof", "Testimonial", "Raw", "MOF", "Reassuring", "Skeptic", ""),
    ("464288342_527776280070004_4513794086771129145_n.jpg", "Norse", "SolutionAware", "Transformation", "StickyNote", "Raw", "TOF", "Bold", "HealthConscious", ""),
    ("464314774_1294211598614645_108591071325575374_n (1).jpg", "Norse", "ProductAware", "Transformation", "BeforeAfter", "Raw", "MOF", "Empathetic", "EmotionalSeeker", ""),
    ("464332051_528879009856169_2653524418319340893_n.jpg", "Norse", "SolutionAware", "ValueProof", "Listicle", "Raw", "TOF", "Empathetic", "Skeptic", ""),
    ("464338199_579967581161691_261430975480927194_n.jpg", "Norse", "MostAware", "Scarcity", "StickyNote", "Raw", "BOF", "Urgent", "BudgetBuyer", ""),
    ("464387064_455251677044718_1470379200232451833_n (1).jpg", "Norse", "SolutionAware", "Transformation", "StatCallout", "Raw", "TOF", "Bold", "HealthConscious", ""),
    ("464387119_468132312940950_6037980963560100468_n.jpg", "Norse", "ProductAware", "SocialProof", "UGC", "Raw", "MOF", "Aspirational", "Skeptic", ""),
    ("464440568_2257879354592789_3952708311330449616_n.jpg", "Norse", "SolutionAware", "Transformation", "BeforeAfter", "Raw", "TOF", "Bold", "EmotionalSeeker", ""),
    ("464726353_488002640887349_991290783872009469_n.jpg", "Norse", "ProblemAware", "Identity", "Listicle", "Raw", "TOF", "Bold", "HealthConscious", ""),
]

# First pass: compute all final names handling collisions
base_name_groups = {}
for row in renames_data:
    orig = row[0]
    brand, awareness, lever, fmt, br, funnel, tone, audience = row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]
    base_new = f"{brand}_{awareness}_{lever}_{fmt}_{br}_{funnel}_{tone}_{audience}"
    if base_new not in base_name_groups:
        base_name_groups[base_new] = []
    base_name_groups[base_new].append(orig)

final_name_map = {}
for base_new, originals in base_name_groups.items():
    if len(originals) == 1:
        final_name_map[originals[0]] = base_new
    else:
        for i, orig in enumerate(originals, 1):
            final_name_map[orig] = f"{base_new}_{i:02d}"

# Second pass: execute renames and build log
rename_log_rows = []
success_count = 0
error_count = 0

for row in renames_data:
    orig, brand, awareness, lever, fmt, br, funnel, tone, audience, edge_cases = row
    ext = os.path.splitext(orig)[1]
    new_name = final_name_map[orig] + ext
    
    src = os.path.join(base, orig)
    dst = os.path.join(base, new_name)
    
    try:
        os.rename(src, dst)
        status = "success"
        success_count += 1
        print(f"OK: {orig[:40]}... -> {new_name}")
    except Exception as e:
        status = f"error: {e}"
        error_count += 1
        print(f"ERROR: {orig[:40]}...: {e}")
    
    rename_log_rows.append([orig, new_name, brand, awareness, lever, fmt, br, funnel, tone, audience, edge_cases, timestamp])

# Write rename_log.csv
csv_path = os.path.join(base, "rename_log.csv")
with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['original_filename','new_filename','brand','awareness_level','psychological_lever','format','branded_raw','funnel_stage','emotion_tone','audience_signal','edge_cases_flagged','timestamp'])
    writer.writerows(rename_log_rows)
print(f"\nrename_log.csv written ({len(rename_log_rows)} rows)")

# Write taxonomy_log.json
taxonomy = {
    "custom_values": [
        {
            "variable": "Format",
            "value": "UGC",
            "description": "Static ad where the copy voice is the hero device — first-person rant/story format that mimics real-person content; designed/produced but feels organic",
            "first_seen_in_file": "430335164_347325478289766_938460460853448725_n.jpg",
            "confirmed_by_user": True,
            "date_added": "2026-02-25"
        }
    ]
}
json_path = os.path.join(base, "taxonomy_log.json")
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(taxonomy, f, indent=2)
print(f"taxonomy_log.json written")

print(f"\nDONE: {success_count} renamed, {error_count} errors")
