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
| Vertical "IKITA" banner | 1728, 0, 320 x 1024 | two banners on the back wall, either side of the figure |
| Shop poster | 0, 1024, 576 x 1024 | right wall, back |
| Cloak placard | 576, 1024, 1472 x 256 | front of the plinth (click panel for the cloak link) |
| (unused) | 576, 1280, 1472 x 768 | - |

- The click targets (BOOTH links) are fixed in the submission; swapping the image
  does not change where a poster links to.
- Commit, push, wait for GitHub Pages to deploy (~1 min). Visitors who already
  loaded the booth keep the old image until they rejoin the instance.

## Runway film

The booth's front wall and interior screen play `ikita_runway_480x592.txt`, loaded by the booth's
`VketStringDownloader` from

    https://yanikita2.github.io/vrc_connect/vket2026w/ikita_runway_480x592.txt

Format IKTV2: `IKTV2;480;592;464;30.9667;8;7;` then 9 base64 pages of raw DXT1, each a grid of 8 x 7
frames (the last page only has the rows it needs). The booth reads the layout from the header, so a
new film only has to stay within 9 pages and VRChat's 100 MB string limit (this one is 87.9 MB).
The film loops on its own clock; the booth soundtrack is not synced to it.

The MP4s below are the same 31-second film (H.264/AAC, 30 fps), recorded in Unity Play mode with the
original avatar runtime, live Cloth and PhysBones, and the cloak's invisibility effect enabled
throughout. They are reference copies; the booth does not play them.

| File | Resolution | Purpose |
| --- | --- | --- |
| [ikita_runway_led_400x494.mp4](ikita_runway_led_400x494.mp4) | 400 x 494 | Full front LED wall, matching its 4 m x 4.94 m aspect ratio |
| [ikita_runway_master_800x988.mp4](ikita_runway_master_800x988.mp4) | 800 x 988 | Master render |
| [ikita_runway_stream_800x988.mp4](ikita_runway_stream_800x988.mp4) | 800 x 988 | 5 Mbps streaming copy |

Direct download URLs:

- https://raw.githubusercontent.com/yanikita2/vrc_connect/main/vket2026w/ikita_runway_led_400x494.mp4
- https://raw.githubusercontent.com/yanikita2/vrc_connect/main/vket2026w/ikita_runway_master_800x988.mp4

Publishing these files does not change the video URL in the booth submission.
That URL is preset: Udon cannot construct a VRCUrl from downloaded text.
Replacing a file at a preset MP4 URL can update the video without changing the
URL, subject to caching and VRChat's video-host restrictions.

GitHub Pages is trusted for VRChat string/image loading, but GitHub hosting is
not on the separate video-player allowlist. In Public/Group Public instances,
using these MP4 URLs requires the world owner to allow the hosting domain and
visitors to enable Allow Untrusted URLs. See the [VRChat video-player rules](https://creators.vrchat.com/worlds/udon/video-players/www-whitelist/).
