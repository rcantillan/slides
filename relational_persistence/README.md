# When Do Alternatives Threaten a Tie? — slides

Presentation of the manuscript *When Do Alternatives Threaten a Tie? Opportunity Sets and Relational Persistence* (Roberto Cantillan). Visual system and Quarto setup follow `../rc28_nyu/`.

## Files

- `slides.qmd` — Quarto revealjs source (render: `quarto render slides.qmd`)
- `slides_backup_2026-10-02.qmd` — the deck as it was before the 3 Oct 2026 restructuring
- `styles.css`, `title-slide.html` — RC28 visual system; `styles.css` now also has `.pending` (red "provisional" tag) and `.step-card-label`
- `center-body.html` — vertically centers each slide's content; add `{.no-vcenter}` to opt out
- `figures/`, `scripts/` — slide figures and the scripts that make them
- `talk_script_16_17min.md` — timed talk script (about 16 min at 74 words per minute)

## What changed on 3 Oct 2026

- New: "What We Do, and What Is New" (replaces "We Ask Three Questions"): question, tool, warning, answer; what is not new.
- New: "The Idea in Plain Words" (count versus value, with a three-row example).
- Rewritten: "Checking the Method: What We Simulated" + "What the Estimators Return" (data-generating process spelled out; Monte Carlo defined).
- Rewritten: "Profiles Persist…" (the agent-based model named and its rules, outcomes and panels explained; stated as a sufficiency demonstration, not calibrated).
- Rewritten for the new evidence: "Online" (α .04–.23 across opportunity-set definitions; α = 1 rejected throughout), "Friendship" (grade-mates ≤ .10 of classmates' pressure; only ego's contacts compete), Takeaways, Limitations (α is relative to the measured set; cap).
- Moved to backup: B5 "Parameters Across Settings". New backup B6: known-truth with a mismeasured opportunity set (`revision_2026_10/sim_struct_mismatch.py`).

## Still to do before presenting

Everything marked with the red "provisional" tag uses the DerStandard panel before the deleted-users correction (`derstandard/rerun_v2_no_deleted_users.sh`). When `revision_2026_10/out_ds_v2/ds_report.txt` exists:
1. Update the tiles on "Online" (range and published specification), the 37 windows / 914,198 on "Two Settings", and table B2.
2. Re-run `scripts/deck_fig_parameters.py` (figure used in B5) with the corrected online estimates.
3. Delete the `.pending` spans (search `pending` in `slides.qmd`) and the sentence "These numbers are being re-estimated…" in the talk script.
