---
name: write-copy
description: Write high-converting ad copy for a specific angle, format, speaker, and tone
tags: [copywriting, ads, creative]
---

# Write Copy Skill

This skill guides you through the complete process of writing ad copy for cold traffic campaigns.

## Expected Inputs

You should receive either:
- A **brief** from the creative strategist (90% of cases) with all variables defined
- **Direct constraints** from the user: angle, format, speaker, tone, hypothesis (optional)

## Process

### STEP 1: Load Strategic Context

Read the following files to understand the landscape:

1. `_ANGLES_SUMMARY.md` - Quick angle identification
2. `SkinAllergies/[AngleName]/_ANGLE_PROFILE_[AngleName].md` - Deep psychographics for the specific angle
3. `_DISTRIBUTION_TRACKER.md` - What's already been tested in this angle/format
4. `_LEARNINGS.md` - What's working/not working across all angles

**Output to user:** Brief summary of what you learned (2-3 sentences max)

---

### STEP 2: Check for Similar Existing Ads (CRITICAL - AVOID DUPLICATION)

**Purpose:** Ensure we're not creating a near-duplicate ad.

**Process:**
1. List all files in `SkinAllergies/[AngleName]/[Format]/`
2. Review file names for similar variables (speaker, tone, etc.)
3. **If file names seem similar:**
   - Read the contents of those files
   - Check ALL variables: hook psychology, messaging structure, opening hook, mechanism explanation style
4. **Ensure at least ONE variable is significantly different**
5. **If very similar ads exist:**
   - **STOP before writing**
   - Explain to the user exactly HOW the new ad will be different from existing ones
   - List the existing ads and their key variables
   - Propose differentiation strategy
   - **Wait for user approval** before proceeding to write

**Output to user:**
- If no similar ads: "No similar ads found. Clear to write."
- If similar ads exist: "Found [X] similar ads. Here's how we'll differentiate: [specific strategy]. Approve?"

---

### STEP 3: Load Research Language

Use Grep to pull exact customer language from research:

**Process:**
1. Identify 3-5 keywords/phrases core to the angle
   - Example for Financial_Bleed: "$500", "can't afford", "broke", "debt", "monthly"
2. Grep `RESEARCH_FULL.md` for each keyword
3. Collect exact phrases customers use (verbatim language)

**Output to user:** "Loaded customer language from research."

---

### STEP 4: Load Format Reference

**Process:**
1. Check if `_SWIPE_FILE/[Format]/_INDEX.md` exists
   - **If YES:** Read index, identify 2-3 most relevant references based on variables, load those specific files
   - **If NO:** Read all files in `_SWIPE_FILE/[Format]/` (for now, until index is created)
2. Study patterns: structure, length, hook style, CTA placement

**Output to user:** "Loaded [X] reference examples for [Format]."

---

### STEP 5: Define/Confirm Hypothesis

**IF hypothesis is provided in brief/prompt:**
- Use it as-is
- Confirm with user: "Hypothesis: [hypothesis]. Proceeding with this."

**IF no hypothesis provided:**
- Define one based on the variables:
  - What are we testing? (e.g., "Speaker impact - does vet authority build trust faster?")
  - What do we believe will happen? (e.g., "Authority validation will resonate with DismissedByVets segment")
  - What will we learn from this test? (e.g., "Does authority matter more than peer empathy for this segment?")
- Present to user: "Hypothesis: [hypothesis]. Does this work?"
- Wait for approval

---

### STEP 6: Method Act the Speaker

**Process:**
1. Identify the speaker's psychological state:
   - **Vet/Authority:** Confident, evidence-backed, seen-it-before, clinical
   - **Dog Owner (Personal Sufferer):** Raw, emotional, discovery-driven, vulnerable, relatable
   - **Dog Owner (Success Story):** Hopeful, relieved, eager to share, conversational
2. Internalize that state
3. Let the language flow FROM that psychological state

**Internal note:** Different speakers use different language patterns. Authority won't say "I stumbled on this." Dog owner won't say "In my 15 years of clinical practice."

---

### STEP 7: Write the Copy

**Process:**
1. Use exact customer language from research (Step 3)
2. Apply hook psychology specified in brief/constraints
3. Structure messaging as specified (story-first, proof-first, curiosity-first, etc.)
4. Follow format requirements from reference examples (length, structure, CTA)
5. Write with the speaker's voice (Step 6)

**Use the copy file template:**

```markdown
# Bxxx - [ANGLE]_[FORMAT]_[SPEAKER]_[TONE]_TESTING

**HYPOTHESIS:** [What we're testing and what we believe will happen]

**WHAT WE'RE LEARNING:** [What this test will reveal about the market]

**ANGLE:** [Angle name]
**FORMAT:** [Format type]
**SPEAKER:** [Who is delivering the message]
**TONE:** [Dominant mood]
**HOOK PSYCHOLOGY:** [What the hook accomplishes]
**MESSAGING STRUCTURE:** [Arrangement of elements]

**DATE CREATED:** [Today's date]
**STATUS:** TESTING

---

## COPY

[The actual ad copy goes here]

---

## NOTES

[Any additional context, performance notes, or iteration ideas]
```

**Output to user:** Present the full copy with template structure.

---

### STEP 8: Present for Approval

**Process:**
1. Show the complete copy (with template structure)
2. Wait for user feedback
3. **If user provides feedback:** Iterate and revise
4. **If user approves:** Proceed to Step 9

**Do NOT create the file yet.** Wait for explicit approval.

---

### STEP 9: After Approval - Create File & Update Tracker

**Only execute this step when user explicitly approves the copy and tells you to create the file.**

**Process:**
1. Determine the next B number:
   - Read `_DISTRIBUTION_TRACKER.md`
   - Find the highest B number
   - Increment by 1
2. Create filename: `Bxxx_[ANGLE]_[FORMAT]_[SPEAKER]_[TONE]_TESTING.txt`
3. Save the copy to: `SkinAllergies/[AngleName]/[Format]/[filename]`
4. Update `_DISTRIBUTION_TRACKER.md`:
   - Add new entry with: B number, angle, format, speaker, tone, hook psychology, messaging structure, status (TESTING), date created
5. Confirm to user: "File created: [filename]. Tracker updated."

---

## Key Reminders

- **NEVER skip Step 2** (duplication check) - wasting tests on near-duplicates kills learning velocity
- **ALWAYS wait for approval** before creating files
- **Use exact customer language** from research - don't make up phrases
- **Method act the speaker** - let psychological state drive word choice
- **Reference the angle profile** constantly - every line should resonate with that segment's beliefs/experiences

---

## Error Handling

**If angle folder doesn't exist:** Stop and alert user - "Angle '[AngleName]' folder not found. Create it first?"

**If format folder doesn't exist:** Create it automatically within the angle folder

**If no reference files exist for format:** Alert user - "No reference files found for [Format]. Proceeding without reference examples."

**If _DISTRIBUTION_TRACKER.md doesn't exist:** Alert user - "Distribution tracker not found. Create the file manually or proceed without updating?"
