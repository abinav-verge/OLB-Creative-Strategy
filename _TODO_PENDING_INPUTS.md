# PENDING INPUTS - TODO TRACKER

This file tracks everything you mentioned you'll provide later.

**Last Updated:** 2026-02-09

---

## 1. GUARDRAILS (Universal)
**Status:** PENDING
**What:** Universal compliance/brand voice rules
- Avoid over-hyped claims
- Health claim regulations (supplement guidelines)
- Words/phrases to avoid
- Brand voice boundaries

---

## 2. FORMAT TEMPLATES
**Status:** PENDING
**What:** File structure templates for each format
- UGC copy structure
- MiniVSL script structure
- Static ad copy structure
- Native image ad structure
- etc.

**Includes:** Copy length requirements per format

---

## 3. FORMAT EXECUTION SKILLS (Articles to Internalize)
**Status:** PENDING
**What:** Detailed articles/guides for writing each format
- How to write UGC ads
- How to write MiniVSLs
- How to write static ads
- etc.

**Purpose:** I internalize these processes and execute them consistently

---

## 4. PRIMARY COPYWRITING TECHNIQUES (Skills)
**Status:** PENDING
**What:** Core copywriting principles to incorporate in ALL copy
- Hook frameworks
- Psychological journey architecture
- Conversion mechanisms
- Pattern interrupts
- etc.

---

## 5. RECURSIVE LEARNING LOOP SKILL
**Status:** PENDING
**What:** Skill for pattern extraction from learnings file
**Purpose:** Automate cross-session learning

---

## 6. SWIPE FILE vs COMPETITOR BREAKDOWN (Decision)
**Status:** PENDING DECISION
**What:** Decide if competitor ad breakdowns should be:
- In the swipe file folder (organized by format)
- OR separate folder for skill development purposes

**Note:** Breaking down competitor ads = skill development for YOU (not just reference material)

---

## 7. 7-DAY STATUS REMINDER FEATURE
**Status:** PENDING - BUILD LATER
**What:** Automated system to remind you to update batch status after 7 days of testing

**How it works:**
- Maintain running file of batch + date published
- Every day, pull up ads that need status updates (7 days old)
- Prompt: "These ads have been testing for 7 days - update status?"

**Implementation:** Build this feature later

---

## 8. RESEARCH APPROACH (Finalization)
**Status:** PENDING - FIGURE OUT LATER
**What:** Determine best approach for handling large research documents
- Current plan: Full research doc + Grep search
- May need refinement based on actual research size/structure

---

## 9. LEARNINGS ACROSS SESSIONS (More Inputs)
**Status:** PENDING - MORE INPUTS COMING
**What:** Additional inputs about cross-session learning system
**Current:** _LEARNINGS.md file maintained manually
**Future:** May integrate with recursive learning loop skill

---

## 10. COPY FILE TEMPLATE UPDATES
**Status:** PENDING - REMIND TO UPDATE LATER
**What:** Refine the copy file structure template
**Current structure:**
```
# Bxxx - [ANGLE]_[FORMAT]_[SPEAKER]_[TONE]_[STATUS]

**HYPOTHESIS:** [What we're testing]

**WHAT WE'RE LEARNING:** [What this test will reveal]

---

[Copy starts here]
```

**Action needed:** 
- Remind to add more fields/structure later
- Update copy file template to include a dedicated section for noting down learnings from ads after testing is complete (post-test analysis).

---

## 11. RESPONSE FLOW CHECK
**Status:** PENDING - REMIND TO CHECK
**What:** Review my response flow when you say "let's create the next ad"
**Current flow:**
1. Read distribution tracker
2. Read learnings
3. Check testing balance (40/40/20)
4. Analyze gaps
5. Suggest next concept/batch with hypothesis

**Action needed:** Remind to check if this flow needs refinement

---

## 12. SWIPE FILE REFERENCE INDEX
**Status:** PENDING - IMPLEMENT WHEN SWIPE FILE GROWS (10+ REFERENCES PER FORMAT)
**What:** Create `_INDEX.md` files in each format folder to index reference copies

**Purpose:** When there are many reference files (50+ UGC examples), enable smart filtering instead of loading all references.

**File location:** `_SWIPE_FILE/[Format]/_INDEX.md`

**Structure:**
```markdown
# [FORMAT] REFERENCE INDEX

## REF_[Format]_[Market]_[Brand]_01.txt
- **Angle mapped to:** [Angle name]
- **Speaker:** [Who delivers message]
- **Tone:** [Dominant mood]
- **Hook psychology:** [What hook accomplishes]
- **Messaging structure:** [Arrangement of elements]
- **Key strength:** [What makes this copy work]
- **Use when:** [Situations to reference this copy]
```

**Integration with write-copy skill:**
- Skill already checks for `_INDEX.md` existence
- If index exists → Read index, load only 2-3 most relevant references based on variables
- If index doesn't exist → Load all references (current behavior)

**Action needed:** Create index files when swipe file per format exceeds 10 references. Then edit write-copy skill if needed (though it's already set up to use the index).

---

## 13. WEEKLY PLANNING SYSTEM
**Status:** PENDING - IMPLEMENT LATER
**What:** Weekly planning workflow with accountability tracking

**Structure:**
- `_WEEKLY_PLANNING/` folder with individual week files (2026-Week-06.md, etc.)
- Each weekly file contains: goals, accountability tracker, insights/notes, review of what worked

**Purpose:**
- Set weekly targets (number of ads, angles to test, experiments)
- Track progress throughout the week
- Keep accountability
- Weekly reflection and learning

**Integration with creative strategist skill:**
- `/plan-week` command to set up weekly strategy
- Skill analyzes gaps, recommends tests for the week
- User approves, briefs created and added to queue

**Action needed:** Design weekly planning workflow and integrate with creative strategist skill.

---

## 14. CONTENT QUEUE SYSTEM
**Status:** PENDING - IMPLEMENT LATER
**What:** Persistent queue of prioritized briefs ready to execute

**Structure:**
- `_QUEUE/ACTIVE_QUEUE.md` - Prioritized list of briefs
- `_QUEUE/COMPLETED_BRIEFS/` - Archive of completed briefs + copy

**Queue logic:**
- Priority ordering (Next Up, This Week, Backlog)
- Can be modified/reprioritized throughout the week
- Checked off as completed

**Integration:**
- User says "next ad" → Pull top priority brief from queue
- After copy written and approved → Move to completed, update queue
- Reminders about weekly queue progress

**Action needed:** Design queue system, priority logic, and integration with creative strategist skill.

---

## 15. ACCOUNTABILITY REMINDERS
**Status:** PENDING - FIGURE OUT LATER
**What:** System for reminding about weekly targets and queue progress

**Options:**
- When user starts a session?
- After completing each ad?
- Only when user asks?
- Mid-week check-ins?

**Action needed:** Determine frequency and triggers for accountability reminders.

---

## 16. CREATIVE STRATEGIST SKILL SCHEDULING
**Status:** PENDING - FIGURE OUT LATER
**What:** Determine when creative strategist skill should run

**Options:**
- Only at start of week (weekly planning)
- Available mid-week for ad-hoc recommendations
- Both

**Likely answer:** Both - `/plan-week` for weekly planning, `/strategize` for ad-hoc recommendations

**Action needed:** Finalize workflow and scheduling of creative strategist skill.

---

## 17. 7-DAY PERFORMANCE CHECK-IN
**Status:** PENDING - BUILD LATER
**What:** Automated reminder to check ad performance after 7 days

**How it works:**
- When ad file status changes to TESTING, note the date
- 7 days later, remind user to check performance
- Update status: TESTING → WINNER/LOSER/MEGA_WINNER
- Add performance notes to file

**Action needed:** Build reminder system that tracks TESTING ads and prompts for status updates after 7 days.

---

## 18. KANBAN BOARD / DASHBOARD
**Status:** IDEA - ADD TO BACKLOG
**What:** Visual tracking system for ads and angles

**Features:**
- Kanban board by status (Not Tested, Testing, Winner, Loser, Mega Winner)
- Board for angles with cards showing format, speaker, tone details
- Distribution tracker insights with ASCII graphs
- Queue status visualization
- Weekly progress tracker
- Top performing angles/formats

**Similar to:** Notion functionality for project management

**Implementation:** ASCII/character-based dashboard that can be displayed in terminal

**Action needed:** Design dashboard structure and visualization approach. Future feature.

---

## 19. COPY REVIEW SKILL
**Status:** PENDING - CREATE SKILL
**What:** Skill that reviews copy after it's written against execution standards

**Purpose:**
- Validate copy against copywriting execution principles (MEMORY.md standards)
- Check for common mistakes (weak hooks, timeline without emotions, performative language, etc.)
- Ensure event-emotion weaving is present
- Verify explanations are paced properly
- Confirm big revelations have proper space
- Check UGC length requirements (180-200 words)

**Execution:**
- Run after copy is finalized but before user approval
- Provide feedback: what's working, what needs revision
- Reference specific framework violations

**Action needed:** Create skill for post-writing copy review.

---

## 20. LONG-TO-SHORT COPY COMPRESSION SKILL
**Status:** PENDING - CREATE SKILL
**What:** Skill that transforms long copy into shorter copy while preserving emotional beats

**Purpose:**
- Compress long-form copy for different formats (UGC vs MiniVSL vs Static)
- Maintain emotional journey and core message
- Don't artificially shorten—capture essence in fewer words
- Preserve event-emotion weaving (just more efficient)

**How it works:**
- Takes long copy as input
- Target length specified (e.g., "180-200 words for UGC")
- Rewrites from scratch (not surgical cutting)
- Maintains same emotional landing

**Action needed:** Create skill for copy compression/adaptation across formats.

---

## 21. LEARNING ROUTINE (Daily/Periodic)
**Status:** PENDING - DEFINE PROCESS
**What:** Define and operationalize a routine for gathering insights
- **Own Ads:** Systematic review of performance data (Daily/Weekly) to extract "What worked/What didn't"
- **Competitor Ads:** Scheduled "Swipe Sessions" to analyze market trends and new creative angles

**Purpose:** Turn passive observation into active data entry for the `_LEARNINGS.md` file and recursive learning loop.

**Action needed:** Create a checklist or skill-guided workflow for these periodic reviews.

---

## 22. OBSIDIAN VAULT MIGRATION
**Status:** IDEA - PLAN MIGRATION
**What:** Migrate the current folder structure into an Obsidian Vault
**Why:**
- Cleaner interface for previewing and sorting files
- Use of Frontmatter/Properties (YAML) for better metadata management (Status, Format, Angle, etc.)
- Graph view to visualize connections between angles and learnings
- Run Gemini CLI directly inside the Vault for integrated workflow

**Action needed:** Plan the migration steps and folder restructuring for Obsidian compatibility.

---

## 23. INPUT SOURCE MAPPING (The "Idea Lab")
**Status:** PENDING - BRAINSTORM & CATEGORIZE
**What:** Map out every possible way an idea or insight can enter this system.

**Potential Input Sources:**
- **Learnings from Own Ads:** Performance data (CTR, CVR, Hook Rate, Hold Rate) from Meta/TikTok/Google.
- **Comments on Posts:** Raw customer feedback, common objections, slang, and specific pain points mentioned in the comments.
- **Market Research:** Official surveys, customer interviews, focus groups.
- **TikTok/Social Media Inspiration:** Trending sounds, visual patterns, viral hook structures, and influencer content.
- **Competitor Ad Libraries:** Analyzing Meta Ad Library, TikTok Creative Center, and curated swipe files (Foreplay/Motion).
- **Amazon/E-commerce Reviews:** Deep dives into 1-star (unmet needs/pain points) and 5-star (benefits/gratitude) reviews.
- **Reddit/Quora/Forums:** Raw, uncurated emotional language and "secret" conversations about the problem.
- **Customer Support/DMs:** Direct questions, misunderstandings, and common friction points from customers.
- **Scientific/Medical Research:** New studies, data points, or "authority" proof points.
- **Search Trends:** Google Trends and Pinterest Trends to see what's currently top-of-mind.
- **Previous Failures:** Analyzing what *didn't* work to identify anti-patterns.
- **Intuition/Observations:** Real-world observations of the target audience and "shower thoughts."

**Purpose:** Ensure no "aha!" moment is lost and create a systematic way to process these diverse inputs into actionable creative strategy.

**Action needed:** Categorize these inputs and decide how each one should be "formatted" for the system to ingest (e.g., does a TikTok link get a breakdown file, or just a note in _LEARNINGS.md?).

---

## 24. RECENT LEARNINGS & NOTES
**Status:** PENDING
**What:** Insights from recent videos and a strategy shift towards simplicity.
- **Evolve - Losers Video 1:** Analyze the "Nic vs Flow" ad. Note: It brought up the product very directly/straight away (contrary to typical intuition), but it worked for them.
- **Spencer - Anti-Dandruff Shampoo:** Learning that simple execution worked even in a highly sophisticated market.
- **Strategic Takeaway:** "Keep it simple, you don't need some crazy logic." Avoid over-complicating the hook or the bridge if simplicity is effective.
- **Action:** Bring these points up with **Pritish** for discussion.

---

## 25. EVOLVE/ZAKARIA PROCESS IMPLEMENTATION
**Status:** PENDING - HIGHEST PRIORITY
**What:** Implement the complete creative strategy and execution process from Evolve / Zakaria.
**Goal:** Leave no stones unturned. Ensure every step of their methodology is integrated into our workflow, from research to brief to final copy and analysis.
**Action needed:** Map out the full Zakaria/Evolve process and audit our current setup against it to identify and close any gaps.

---

## 26. SYSTEMIC PRODUCTIVITY & ADHD RITUALS
**Status:** IN-PROGRESS (Defining rituals)
**What:** Design and implement a system to manage ADHD, reduce "scattered brain," and promote consistent rituals.

### THE RITUALS:

**🌅 STARTUP RITUAL (Session Start)**
1. **Clear the Deck:** Close non-essential tabs/apps.
2. **Mindset Reset:** Read `_CREATIVE_STRATEGISTS_BRAIN_CORE.md` (3 mins).
3. **Review Priorities:** Read this file (`_TODO_PENDING_INPUTS.md`).
4. **Log Intent:** State exactly what you will accomplish in this session.

**🌙 SHUTDOWN RITUAL (Session End)**
1. **Daily Log:** Record what actually got done vs. distractions.
2. **Quick Capture Cleanup:** Move items from `_QUICK_CAPTURE.md` to permanent homes.
3. **Set Tomorrow's "Big One":** Define the single most important task for the next session.
4. **Tracker Sync:** Ensure finished ads are in `_DISTRIBUTION_TRACKER.md`.

**⚡ QUICK CAPTURE (The ADHD Safety Net)**
- Use a `_QUICK_CAPTURE.md` file to dump random ideas immediately so they don't derail your current task.

**📓 DAILY LOGS (`_DAILY_LOGS/` folder)**
- Create dated entries (`YYYY-MM-DD.md`) to track focus, tasks done, blockers, and learnings.

**Action needed:** Finalize the "How-To" for these rituals and decide if we want specific CLI commands (like `/ritual-start`) to automate the logging and mindset reset process.
