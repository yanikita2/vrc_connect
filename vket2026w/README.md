# Vket 2026 Winter booth (circle 3499) - swappable posters

`ikita_posters.png` is downloaded at runtime by the booth's `VketImageDownloader`
(once, when a visitor enters the booth) and replaces the lightbox poster atlas:

    https://yanikita2.github.io/vrc_connect/vket2026w/ikita_posters.png

If the download fails the booth keeps the atlas baked into the submission.

## Rules for replacing it

- Keep it **2048 x 2048**, PNG or JPG (VRChat image loading max is 2048 x 2048).
- Keep the **same layout** - the lightbox meshes use fixed UV rectangles:

| Slot | Pixels (x, y from top, w x h) | Where it shows |
| --- | --- | --- |
| NPC Pet poster | 0, 0, 576 x 1024 | left wall, front |
| Slime poster | 576, 0, 576 x 1024 | left wall, back |
| Smart Weapon poster | 1152, 0, 576 x 1024 | right wall, front |
| "NOW YOU SEE IT." strip | 1728, 0, 320 x 1024 | both sides of the back screen |
| Shop poster | 0, 1024, 576 x 1024 | right wall, back |
| Cloak plinth label | 576, 1024, 1472 x 256 | front of the cloak plinth |
| (unused) | 576, 1280, 1472 x 768 | - |

- The click targets (BOOTH links) are fixed in the submission; swapping the image
  does not change where a poster links to.
- Commit, push, wait for GitHub Pages to deploy (~1 min). Visitors who already
  loaded the booth keep the old image until they rejoin the instance.

The booth video cannot be swapped this way: Udon cannot build a VRCUrl from a
downloaded string, so the YouTube URL is fixed in the submission.
