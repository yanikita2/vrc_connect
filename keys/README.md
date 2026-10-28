# Cross-world collectible keys

The single encrypted list is **v1/players.txt**. Clients string-load it once,
decrypt it, and match their exact current VRChat display name. The list also
contains the names needed for a future per-world completion board.

Decrypted schema 1: revision, card registry, and `players` rows of
`[displayName, cardBitmask]`. Bit 0 is the Library Key Card. Names retain Unicode,
spaces, punctuation and case. The existing `config/runtime.json` is independent.

These are **unverified client completion claims matched by display name**, not
authenticated VRChat accounts. Names can change, collide, or be spoofed. Cards
are cosmetic; do not use them for valuable access, moderation, or identity.

Names are encrypted in the published file. No client IPs, API secrets or Git
credentials are published. The shipped world contains the decryption material;
encryption obscures the list but cannot guarantee secrecy from those clients.

The receiver and publisher live in the owner's yoikita project, `vrc-connect/`.
The publisher updates this one file when records change; GitHub Pages/CDN updates
are asynchronous. Repeated visits do not create duplicate entries.
