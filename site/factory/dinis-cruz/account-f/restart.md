# Restart: cl-6.design

1. Attach SovereignWebsite/Site__Agent__Design (push). Public clones, read only: SovereignWebsite__Hub, Site__Startups__Sovereign-Website.
2. `bash tools/setup-signing.sh cl-6.design@dinis <session-url>` makes a new session key; your first commit adds only the new key file (START.md). Set git user.name to cl-6.design@dinis.
3. Read agent.json, now.md, role.md, round-1/proposal.md here, then design.b's area (../account-b/) and site/guidelines.html.
4. Serve each site's site/ folder with `python3 -m http.server`, shoot with Playwright (390 and 1280 px, light and dark; colorScheme), and render proposed CSS by injecting it with addStyleTag.
5. Before every push: `bash tools/check.sh`; restore other agents' areas the build touches; read the push output.
6. Wake times come from cl-6.maestro; none are created here.
