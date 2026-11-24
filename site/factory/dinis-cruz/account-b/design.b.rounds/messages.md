# design.b.rounds: messages

Who I send to, and what I expect back. Read an agent's own area before writing to it.

- **design.b** (copied on every review): sets the question and the pace for each site.
- **sites.b** (Car Buyer, the pipeline demo, the WordPress section demo): sends commits to review; gets each review.
- **startups.b** (the five startup brochures), **hub.b** (the hub), **suno.b** (Suno, our songs): the same.
- **conductor.b**: gets the one line for anything that truly waits on Dinis; it routes it through decisions.b.

Every review is published at `/reviews-<site>-<date>-round-<n>.html` and every run at `/runs-<site>-<date>-r<n>.html`.
