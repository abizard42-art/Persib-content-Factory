# Persib Content Factory — Vertical Video Layout v1

Status: **APPROVED — OFFICIAL BASE TEMPLATE AND CHIBI CHARACTER DESIGN**

## 1. Canvas
- Format: vertical 9:16 (1080 × 1920 reference canvas).
- Background: dark navy / near-black.
- Accent palette: Persib blue and white; use yellow only as a restrained highlight.
- Overall style: clean football-editorial motion graphics, not a full-screen slideshow.

## 2. Screen zones
| Zone | Height | Purpose |
|---|---:|---|
| Header + category tab | 12.5% | Persistent channel identity and changing content category |
| Main visual panel | 47.5% | Photos, match moments, stats, tables, maps, or tactical diagrams; priority space for analysis and formation graphics |
| Chibi host / narration | 40% | Consistent Bobotoh Casuals host; fixed at 40% of the canvas height |

This is the official base template for Persib Content Factory videos. Keep the proportions fixed: 12.5% header, 47.5% main visual panel, and 40% chibi host. Content inside the main visual panel may change by episode category, but the overall screen zones remain consistent.

## 3. Header and category tabs
Keep the channel name fixed. Change the category label to match the episode:
- TRANSFER
- MATCH PREVIEW
- STARTING XI
- TACTICAL ANALYSIS
- MATCH REVIEW
- STATISTICS
- PERSIB UPDATE

## 4. Main visual panel
The panel changes with the subject being discussed. Use the most informative visual for each narration beat:
- Player profile, availability, or comparison: player photo + concise labels.
- Match preview/review: opponent, fixture/result, key moments, and relevant match photos.
- Starting XI: pitch formation diagram with player names and role labels.
- Tactical analysis: pitch zones, arrows, pressing/build-up patterns, and short annotations.
- Statistics: large readable figures, comparisons, and simple charts.
- Transfer/update: concise headline, source/date, and status label.

Do not force every episode into the same visual type. Keep text short enough to read on a phone.

## 5. Chibi host — approved character design
- The editor has approved the generated master character sheet as the official visual design reference for the Persib Content Factory host.
- Character name is **not yet assigned**. The generated sheet contains the text “Raka”; this is a placeholder/error and must not be used as the Persib host's name. Keep this character separate from Raka, the host of the Sejarah Dunia project.
- Visual identity: youthful anime-chibi Bobotoh, tousled dark hair, expressive brown eyes, friendly energetic face.
- Outfit: dark technical parka with Persib-blue accents, dark shirt, olive cargo trousers, retro/outdoor sneakers, and a small crossbody sling bag.
- Permanent sleeve identity: original circular **FLOWER CITY CASUALS** concept patch. This is a channel character design, not an official club or community emblem.
- Palette: dark navy/black, Persib blue, white, olive, warm skin tones, with restrained yellow accents.
- Keep face, hair, proportions, outfit, patch, and colors consistent across all future poses and expressions.
- Required expression set: NORMAL, HAPPY, ANALYSIS, FIRED-UP, SHOCKED, DISAPPOINTED.
- The approved master sheet is a design/reference sheet, not yet six individually cropped production-ready transparent assets. Prepare consistent expression/pose assets from this reference before animation implementation.

## 6. Motion and pacing
- First render uses a static temporary host placeholder so the layout can be approved before character animation work.
- Chibi animation concept is approved for a later pass: subtle idle/breathing, blinking, mouth movement synced to narration, hand gestures, and context-based expressions.
- Keep the host's base position stable; use expression/gesture changes sparingly to emphasize key beats.
- Change the main visual panel when the narration moves to a new fact, player, tactical point, or statistic.
- Prefer subtle transitions and clear visual hierarchy over constant movement.
- Avoid covering faces, player names, key statistics, or tactical markings with subtitles.

## 6.1 Starting XI reveal animation
For the STARTING XI category, reveal the formation player by player rather than showing the full lineup immediately.

### Sequence
1. Show the empty pitch and formation markers briefly.
2. Reveal the goalkeeper first, then defenders, midfielders, and forwards in a deliberate sequence.
3. Each player marker/card uses a smooth 3D-style flip or horizontal turn to reveal the player information.
4. On reveal, show a small player portrait on the left side of the card, shirt number prominently, and the player's name beside it.
5. Keep the player's position marker on the pitch connected visually to the corresponding card, so viewers can identify the role and location.
6. Finish with the complete XI visible together for a short hold.

### Motion direction
- Use a smooth ease-in-out transition, approximately 350–500 ms per player reveal.
- Stagger reveals with a short 120–180 ms gap; avoid flashing all cards at once.
- Use a subtle Persib-blue glow or edge highlight on the active reveal, then settle to a calm blue/white card.
- Keep the portrait small and cropped consistently; prioritize shirt number and readable name.
- If a licensed player photo is unavailable, use a neutral initials/number tile rather than inventing a likeness.
- The formation should remain readable on a phone. Avoid overlapping cards; use compact labels near the pitch or a paired pitch-and-lineup layout if the full names do not fit.
- The reveal order is a presentation choice, not evidence of the official lineup. Label the graphic **PREDIKSI STARTING XI** until the official team sheet is released.

### Layout composition for the lineup reveal
- Keep the pitch in portrait orientation: the opponent goal is at the top and our goalkeeper is at the bottom.
- Arrange the formation in horizontal lines stacked **from top to bottom** (forwards, midfield, defence, goalkeeper), not as a left-to-right sequence across the screen.
- Keep compact player reveal cards in a neat column beside the vertical pitch, aligned by line/role where possible.
- Each card flips to reveal: small portrait thumbnail on its left edge, shirt number, then player name and short position label.
- When a card reveals, illuminate the matching player's marker on the pitch; then return it to the normal state.
- For the final hold, show all 11 markers on the vertical pitch and all 11 compact cards together. If text becomes too small at phone size, split the reveal into defensive, midfield, and attacking groups rather than shrinking labels.
- The flip should reveal the actual player information on the reverse face; do not use a meaningless mirrored name or a card that only spins decoratively.

### Data per player
- Shirt number
- Player name
- Position / role
- Small portrait (licensed or otherwise authorized)
- Pitch coordinates for the selected formation

## 7. Editorial and rights checks
- Distinguish official information, reputable media reports, unconfirmed rumors, and editorial analysis.
- Predicted lineups must be labeled as predictions, never as official lineups.
- Use match photos/footage only when permission or a valid license is available. Credit alone does not grant usage rights.
- Add source/date labels where a visual makes a factual claim.

## 8. First preview acceptance checklist
- [x] Overall placement and screen-zone proportions approved by the editor.
- [x] Chibi character visual design approved by the editor as the official design reference.
- [ ] Readable on a typical Android phone without zooming.
- [ ] Header/category is clear but does not dominate.
- [ ] Main panel can show photos, statistics, and tactical diagrams without changing the overall layout.
- [ ] Chibi host remains visually prominent in the lower zone.
- [x] Persib identity is clear through the character's Bandung Casuals styling and blue/white accents.
- [x] Six expressions are defined in the approved reference sheet.
- [ ] Production-ready individual expression assets are prepared and checked for consistency.
- [ ] No unlicensed footage or imagery is included.

## 9. Next implementation step
Prepare a clean production asset pack from the approved master character reference: full-body host cutout plus six consistent expression/pose assets, with transparent backgrounds where practical. Do not use the placeholder text “Raka” as the Persib host's name. Then integrate the static host into the approved 9:16 layout and proceed to idle/blink/mouth/gesture animation only after checking the first integrated preview.

## Chibi Host Master Sheet — Production Candidate (2026-11-23)

A new square character model sheet has been generated for the Persib Content Factory host. It contains:
- Main full-body hero pose in Bandung Casuals × gorpcore styling
- Six expression references: NORMAL, HAPPY, ANALYSIS, FIRED-UP, SHOCKED, DISAPPOINTED
- Front, side, rear, and profile turnaround views
- Sleeve patch concept and color palette

**Asset status:** generated production candidate; use as the visual consistency reference pending final human review of fine details. Do not treat generated lettering or any crest-like mark as an official club-issued logo. The sleeve patch is an original FLOWER CITY CASUALS concept.

**Character consistency rules:**
- Keep face, hair silhouette, body proportions, dark technical parka, cargo pants, outdoor/retro sneakers, sling bag, and blue accents consistent.
- Use the six expression references to guide face and pose changes; do not redesign the character between episodes.
- Keep the approved video layout proportions unchanged: header/category 12.5%, main visual panel 47.5%, chibi host zone 40%.
- This sheet is a visual reference, not a set of separated transparent animation layers. Prepare clean individual character/expression assets before rigging or lip-sync animation.

