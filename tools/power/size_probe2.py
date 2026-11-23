"""Size of test 1 forms at alpha = 0 (synthetic): registered-style bootstrap p vs Newey-West t (gm.stats.nw_alpha_t)."""
import sys, numpy as np, pandas as pd
sys.argv=['x']; import power_3_3 as P
from gm import stats as ST
from math import erf, sqrt
rows=[]
for sh in ("FULL432","STRIP250","RULE_q25_L12"):
    for rho,SRb in ((0.0,1.23),(0.3,1.23),(0.6,1.23),(0.3,0.5),(0.3,0.0)):
        if sh.startswith("RULE") and rho==0.6: continue
        spec=dict(P.SHAPES[sh],S=rho*SRb)
        name="size2|%s|%s|%s"%(sh,rho,SRb); rng=P.rng_for(name); R=2000
        pod=P.make_pod(spec,R,rng); t0=P.T_FULL-spec["Tw"]
        book=P.make_book(rng,R,[(pod["z"],rho,t0)],SRb)[:,t0:]
        a,beta,pa=P.boot_alpha(book,pod["net"])
        nw=np.array([ST.nw_alpha_t(pd.Series(pod["net"][i]),pd.Series(book[i])) for i in range(R)])
        pnw=np.array([0.5*(1-erf(t/sqrt(2))) for t in nw])
        r=dict(shape=sh,rho=rho,SRb=SRb,R=R,boot_025=(pa<.025).mean(),boot_05=(pa<.05).mean(),boot_0125=(pa<.0125).mean(),
               boot_q025=np.percentile(pa,2.5),nw_025=(pnw<.025).mean(),nw_05=(pnw<.05).mean())
        rows.append(r); print(r,flush=True)
pd.DataFrame(rows).to_csv(P.os.path.join(P.RAW,"size_alpha.csv"),index=False)
