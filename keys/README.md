# Cross-world collectible keys

The single encrypted list is **v1/players.txt**. Clients string-load it once,
decrypt it, and match their exact current VRChat display name. It includes the
card catalogue, five-language titles/unlock conditions and artwork cell indices,
as well as names needed for a future per-world completion board.

Decrypted schema 1: revision, card registry, and `players` rows of
`[displayName, cardBitmask]`. Bit 0 is the Library Key Card; bit 1 is an admin-only
Debug Key Card for testing the shared loader. Names retain Unicode,
spaces, punctuation and case. The existing `config/runtime.json` is independent.

These are **unverified client completion claims matched by display name**, not
authenticated VRChat accounts. Names can change, collide, or be spoofed. Cards
are cosmetic; do not use them for valuable access, moderation, or identity.

Names are encrypted in the published file. No client IPs, API secrets or Git
credentials are published. The shipped world contains the decryption material;
encryption obscures the list but cannot guarantee secrecy from those clients.

The receiver and publisher live in the owner's yoikita project, `vrc-connect/`.
The publisher updates this one text file when records or metadata change.
**v1/cards-0.png** and **v1/cards-1.png** are the two transparent 2048x2048 image
sheets. Each has sixteen permanent 512px cells. A client downloads only the
sheets needed by its owned cards and shares the texture across slot thumbnails
and the selected-card preview. It does not request a file per card.

The catalogue's atlas `version` selects one of the client's preset `?v=0` through
`?v=255` URLs when artwork changes. These all reference the same two PNG files;
they do not create more list/image files. Existing IDs/cells must never be moved
or reused. Up to 31 positive card bits are supported by this v1 client format.

Once a world contains the shared loader, future card artwork and translated
metadata can be added centrally without re-uploading that world. A new world
still supplies its own completion adapter. GitHub Pages/CDN updates are
asynchronous. Repeated visits do not create duplicate entries.
