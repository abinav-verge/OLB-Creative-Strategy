---
name: strategize
description: Strategic recommendations for what ad to create next based on gaps, learnings, and testing balance
tags: [strategy, creative, planning]
---

# Creative Strategist Skill

This skill helps you decide **WHAT to create next**. It analyzes the current state, identifies gaps, and recommends the next strategic test.

**Output:** A creative brief that can be fed directly to `/write-copy`.

---

## Process

### STEP 1: Load Strategic Context

Read these files to understand the current landscape:

1. `_CREATIVE_STRATEGISTS_BRAIN_CORE.md` - Strategic mindset frameworks
2. `_DISTRIBUTION_TRACKER.md` - What's been tested, what's winning/losing
3. `_LEARNINGS.md` - Patterns from winners and losers
4. `_ANGLES_SUMMARY.md` - Quick reference of all available angles

**Output to user:**
- Brief state summary (2-3 sentences)
- Example: "Currently testing 24 ads across 8 angles. 5 winners, 3 mega winners. Financial_Bleed and Medication_Horror are strongest performers."

---

### STEP 2: Analyze Current State

**Scan all avatar folders:**
- Check what folders exist at root level (SkinAllergies, etc.)
- For each avatar folder, check for angle subfolders
- Analyze distribution across all avatars

**What to analyze:**

#### A) Testing Balance (40/40/20 Split)
- New tests vs Iterations vs Moonshots
- Are we exploring enough new angles?
- Are we iterating on winners?
- Any wild experiments recently?

#### B) Angle Coverage (Per Avatar)
- Which angles have the most tests?
- Which angles are undertested?
- Which angles have winners? (Need more volume/iterations)
- Which angles have only losers? (Need different variables or abandon?)

#### C) Format Diversity
- Which formats have been tested most?
- Are winners concentrated in one format? (Opportunity to test winning angles in new formats)
- Any formats completely untested for specific angles?

#### D) Variable Diversity
- **Speaker:** Are we testing different speakers? (Authority vs Dog Owner vs Expert)
- **Tone:** Different tones? (Empathetic, Urgent, Validating, Desperate, etc.)
- **Hook psychology:** What hook types have we tested?
- **Messaging structure:** Story-first, proof-first, curiosity-first, etc.

#### E) Winner Patterns
- What do winners have in common?
- What variables appear in mega winners?
- Are there clear patterns to double down on?

#### F) Loser Patterns
- What consistently doesn't work?
- Are there variables to avoid?

**Output to user:**
- Summary of gaps and opportunities
- Example: "Gaps: Only 2 tests for Vet_Gave_Up angle. No Doctor speaker tested yet. All winners are UGC format - opportunity to test winners in MiniVSL."

---

### STEP 3: Check for User Constraints/Direction

**Ask the user:**

"What are we optimizing for today?"

**Present options:**
- **Full autonomy:** "You decide - recommend the highest-leverage tests"
- **Specific direction:** "I want to test [angle/format/speaker/variable]"
- **Iteration focus:** "Only iterations on winners today"
- **New angle exploration:** "Only new angles/variables today"
- **Moonshot mode:** "Wild experiments only"
- **Time constraint:** "Quick wins only (low production effort)"

**Wait for user input.**

---

### STEP 4: Make Strategic Recommendations

Based on analysis (Step 2) and user direction (Step 3), recommend **1-3 tests**.

**For each recommendation, provide:**

#### A) Type
New Test / Iteration / Moonshot

#### B) Variables
- Angle
- Format
- Speaker
- Tone
- Hook psychology (what the hook accomplishes)
- Messaging structure (arrangement of elements)

#### C) Hypothesis
- What are we testing?
- What do we believe will happen?
- What will we learn from this test?

#### D) Rationale
- Why this test makes strategic sense right now
- What gap it fills
- Why these specific variables

#### E) Effort Estimate
Low / Medium / High (production complexity)

**Example recommendation:**

```
═══════════════════════════════════════════════════════
RECOMMENDATION 1: New Test
═══════════════════════════════════════════════════════

TYPE: New Test

VARIABLES:
- Angle: Vet_Gave_Up
- Format: UGC
- Speaker: Dog Owner (Personal Sufferer)
- Tone: Frustrated + Vindicated
- Hook Psychology: Authority abandonment + "I figured it out myself"
- Messaging Structure: Frustration-first → Self-discovery → Validation

HYPOTHESIS:
Testing whether "I solved it when vets couldn't" narrative resonates with Vet_Gave_Up segment.

We believe: Self-empowerment angle will validate their frustration and position the product as the "answer the vet didn't have."

We'll learn: Does this segment respond better to empowerment messaging vs authority validation.

RATIONALE:
- Vet_Gave_Up only has 2 tests (undertested angle)
- No "vindicated dog owner" speaker tested yet
- This segment feels abandoned by authority - peer discovery might resonate stronger
- Fills gap in speaker diversity

EFFORT: Low (UGC is fastest format)
```

**Output to user:**
- Present 1-3 recommendations
- Ask: "Which direction do you want to go? Or should I adjust?"

---

### STEP 5: Adjust Based on User Feedback

**User might:**
- Choose one of the recommendations → Proceed to Step 6
- Request changes to variables → Revise and re-present
- Provide new direction → Go back to Step 4
- Ask for more options → Generate additional recommendations

**Iterate until user approves a specific test.**

---

### STEP 6: Generate Creative Brief

Once user approves a recommendation, **ASK:** "Ready to create the brief file?"

**Wait for explicit approval to create the file.**

When approved:

1. **Determine next B number:**
   - Read `_DISTRIBUTION_TRACKER.md`
   - Find highest B number
   - Increment by 1

2. **Create brief file:**
   - Location: `[Avatar]/[AngleName]/[Format]/`
   - Filename: `Bxxx_[AngleName]_[Format]_BRIEFED.txt`
   - Status: BRIEFED

3. **Brief structure:**

```markdown
# Bxxx - [AngleName]_[Format]

**STATUS:** BRIEFED

**TYPE:** [New Test / Iteration / Moonshot]

**ANGLE:** [Angle name]
**FORMAT:** [Format type]
**SPEAKER:** [Who delivers the message]
**TONE:** [Dominant mood]
**HOOK PSYCHOLOGY:** [What the hook accomplishes]
**MESSAGING STRUCTURE:** [Arrangement of elements]

**HYPOTHESIS:**
[What we're testing and what we believe will happen]

**WHAT WE'RE LEARNING:**
[What this test will reveal about the market]

**RATIONALE:**
[Why this test makes strategic sense right now]

**EFFORT:** [Low/Medium/High]

**DATE CREATED:** [Today's date]

---

## FINAL COPY
[To be written - use /write-copy with this brief]

---

## PERFORMANCE NOTES
[To be added after 7 days]
```

4. **Update `_DISTRIBUTION_TRACKER.md`:**
   - Add new entry with B number, angle, format, speaker, tone, hook psychology, messaging structure, status (BRIEFED), date created

5. **Confirm to user:**
   - "Brief created: [filename]"
   - "Status: BRIEFED"
   - "Ready to write copy? Use `/write-copy` and reference this brief."

---

## Key Reminders

- **Load CORE brain file** (not DEEP) - token efficiency
- **Scan all avatar folders** - future-proof for multiple avatars
- **Wait for user direction** - don't assume what they want to optimize for
- **Present clear recommendations** - type, variables, hypothesis, rationale, effort
- **Wait for approval** before creating brief files
- **Status starts as BRIEFED** - changes to COPY_WRITTEN when copy is added

---

## Error Handling

**If _DISTRIBUTION_TRACKER.md doesn't exist:**
- Alert user: "Distribution tracker not found. Cannot determine next B number. Create tracker first?"

**If no avatar folders exist:**
- Alert user: "No avatar folders found. Create avatar + angle structure first?"

**If _LEARNINGS.md doesn't exist:**
- Proceed but note: "No learnings file found. Recommendations based on distribution only."

**If no angles have been tested yet:**
- Recommend: "Starting fresh. Recommend testing 3-5 different angles across different psychological entry points to find initial winners."
