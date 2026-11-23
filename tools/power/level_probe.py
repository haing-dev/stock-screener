"""Power of test 1 (alpha, bootstrap p) at per-pod levels 0.025 / 0.0125 for key cells (synthetic)."""
import sys, numpy as np, pandas as pd
sys.argv=['x']; import power_3_3 as P
rows=[]
for sh in ("FULL432","STRIP250","CURVE260","RULE_q25_L12"):
    for lab,ir in (("a=0",0.0),("IR=0.2",0.2),("IR=0.4",0.4)):
        rho,SRb=0.3,1.23
        spec=dict(P.SHAPES[sh],S=rho*SRb+ir*np.sqrt(1-rho*rho))
        name="lvl|%s|%s"%(sh,lab); rng=P.rng_for(name); R=1500
        pod=P.make_pod(spec,R,rng); t0=P.T_FULL-spec["Tw"]
        book=P.make_book(rng,R,[(pod["z"],rho,t0)],SRb)[:,t0:]
        a,b,pa=P.boot_alpha(book,pod["net"])
        r=dict(shape=sh,label=lab,rho=rho,SRb=SRb,R=R,p_lt_025=(pa<.025).mean(),p_lt_0125=(pa<.0125).mean(),p_lt_05=(pa<.05).mean(),p_lt_0036=(pa<.025/7).mean())
        rows.append(r); print(r,flush=True)
pd.DataFrame(rows).to_csv(P.os.path.join(P.RAW,"level_probe.csv"),index=False)
