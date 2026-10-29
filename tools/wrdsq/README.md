# wrdsq: reusable WRDS access for any chat (user ttdlisa, WRDS Cloud)

WRDS policy forbids loading WRDS Data into AI tools ("loading Data retrieved from WRDS into LLMs and other Generative
A.I. tools is prohibited"; exceptions only for enterprise-protected instances for some vendors). So:
Claude writes a job -> the user pastes one PowerShell line -> the job runs on WRDS Cloud (automation is permitted there)
-> data stays in ~/wrdsq/data on WRDS -> only metadata and analysis results come back (wrds_result.txt in Downloads).

- Runner: `wrdsq.py` (installed at ~/wrdsq/wrdsq.py on WRDS Cloud; step reference in its docstring).
- Line builder: `python3 tools/wrdsq/mkjob.py job.json` -> prints the paste line (one password + Duo).
- Install / update (user, PowerShell, wrdsq.py in Downloads):
  `scp $HOME\Downloads\wrdsq.py ttdlisa@wrds-cloud.wharton.upenn.edu:~/ ; ssh -t ttdlisa@wrds-cloud.wharton.upenn.edu "python3 ~/wrdsq.py install"`
- Storage: 10 GB home quota (pulls refused above 90%). Jobs run on a compute node via qrsh (head-node rule).
- Jobs used so far: `jobs/`.
- The account-level skill "wrds-data" carries the same instructions to chats outside this repo.
