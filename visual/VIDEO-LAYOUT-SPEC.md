# Persib Content Factory — Vertical Video Layout v1

Status: **DRAFT — layout direction agreed; visual implementation pending editor review**

## 1. Canvas
- Format: vertical 9:16 (1080 × 1920 reference canvas).
- Background: dark navy / near-black.
- Accent palette: Persib blue and white; use yellow only as a restrained highlight.
- Overall style: clean football-editorial motion graphics, not a full-screen slideshow.

## 2. Screen zones
| Zone | Height | Purpose |
|---|---:|---|
| Header + category tab | 12.5% | Persistent channel identity and changing content category |
| Main visual panel | 35% | Photos, match moments, stats, tables, maps, or tactical diagrams |
| Chibi host / narration | 52.5% | Consistent Bobotoh Casuals host, expressions and gestures support narration |

Percentages are initial layout proportions, not locked pixel measurements. Revisit after the first phone preview.

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

## 5. Chibi host
- One consistent Bobotoh Casuals character, shown in the lower host zone.
- Character direction: Bandung casual / awayday terrace style; technical parka, cargo trousers, retro/outdoor sneakers, small sling bag, Persib-blue and white accents.
- Permanent sleeve identity: original circular **FLOWER CITY CASUALS** concept patch. This is a channel character design, not an official club or community emblem.
- Use one master character sheet containing multiple expressions/poses. Keep face, hair, clothing, colors, and patch consistent between expressions.
- Required expression set: NORMAL, HAPPY, ANALYSIS, FIRED-UP, SHOCKED, DISAPPOINTED.
- The master sheet is not approved yet; do not treat the current prototype SVG/PNGs as final. Replace/rebuild expression assets after the character master is approved.

## 6. Motion and pacing
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
- Keep the pitch on the **left half** of the main visual panel.
- Place compact player reveal cards in a neat column on the **right half**, aligned by line/role where possible.
- Each card flips to reveal: small portrait thumbnail on its left edge, shirt number, then player name and short position label.
- When a card reveals, illuminate the matching player's marker on the left-side pitch; then return it to the normal state.
- For the final hold, show all 11 markers on the pitch and all 11 compact cards together. If text becomes too small at phone size, split the reveal into defensive, midfield, and attacking groups rather than shrinking labels.
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
- [ ] Readable on a typical Android phone without zooming.
- [ ] Header/category is clear but does not dominate.
- [ ] Main panel can show photos, statistics, and tactical diagrams without changing the overall layout.
- [ ] Chibi host remains visually prominent in the lower zone.
- [ ] Persib identity is unmistakable through the character's styling and blue/white accents, without relying only on a logo.
- [ ] All six expressions look like the same character.
- [ ] No unlicensed footage or imagery is included.

## 9. Next implementation step
Build a single 9:16 sample scene with placeholder visuals and a temporary host silhouette. Replace the placeholder with the approved Bobotoh Casuals master sheet once image generation is available and the editor approves the design.
