# Brief: claim extraction (one document)

Investor: Dev Kantesaria (Valley Forge Capital Management). Captions may misspell the name (Kesaria, Cantasaria,
Katesaria): it is the same person.

1. Read the spec: SCRATCH/CLAIM_SPEC_v1.md. Follow it exactly.
2. Read your document in full: SCRATCH/src/<DOC>.txt (read it in chunks if needed; read every line).
3. Write the claims JSON list to SCRATCH/<FOLDER>/<DOC>.claims.json. Ids <DOC>-C001, <DOC>-C002, ...
4. Check your quotes: python3 SCRATCH/check_quotes.py SCRATCH/src/<DOC>.txt SCRATCH/<FOLDER>/<DOC>.claims.json
   For every claim with found=false, fix the quote by copying the exact text from the file (or drop the claim), and
   rerun until every quote is found. Fix lines where line_ok is false.
5. Work ONLY in SCRATCH/<FOLDER>/ (your private folder). Do not touch other folders or the src files.
6. Reply with: number of claims, counts by kind and by part, and any passage you left out because the speaker was
   unclear (line numbers). Nothing else.
