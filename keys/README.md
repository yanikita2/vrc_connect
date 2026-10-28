# Cross-world collectible keys

`v1/00.txt` through `ff.txt` are encrypted card snapshots consumed by Udon string
loading via GitHub Pages. The existing `config/runtime.json` is independent.

The first two hex digits of the client's exact display-name digest select the
shard. Decrypted schema 1 contains a shard identifier, revision, card registry and
`[nameHash, cardBitmask]` rows. Bit 0 awards the Library Key Card.

These are **unverified client completion claims matched by display name**, not
authenticated VRChat accounts. Names can change, collide, or be spoofed. Cards
are cosmetic; do not use them for valuable access, moderation, or identity.

No plaintext names, client IPs, API secrets or Git credentials are published.
The shipped world contains the decryption material; encryption obscures the
snapshot but cannot guarantee secrecy from clients that possess it.

The receiver and publisher live in the owner's yoikita project, `vrc-connect/`.
Only changed shards are published. GitHub Pages/CDN updates are asynchronous.
