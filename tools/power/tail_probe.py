"""Which half of the tail test fails for good pods, and how the margin changes it (synthetic; part of 3.3)."""
import sys, numpy as np, pandas as pd
sys.argv=['x']; import power_3_3 as P
rows=[]
for gl,g in (("GARCH-t5",None),("Gaussian iid",dict(df=None,a=0,b=0,ar=0.0))):
    for sh,S,rho in (("FULL432",0.4,0.0),("FULL432",0.3*1.23+0.4*np.sqrt(1-.09),0.3),("RULE_q25_L12",0.4,0.0),("STRIP250",0.4,0.0)):
        o,ir,td=P.run_cell(dict(P.SHAPES[sh],S=S),500,1.23,rho,gen=g)
        ddd=(o["dd_c"]-o["dd_b"])*100; dwm=(o["wm_c"]-o["wm_b"])*100
        r=dict(gen=gl,shape=sh,rho=rho,S=round(S,3),true_IR=round(ir,3),
               dd_diff_p10=np.percentile(ddd,10),dd_diff_med=np.median(ddd),wm_diff_p10=np.percentile(dwm,10),wm_diff_med=np.median(dwm))
        for m1,m2 in ((2,1),(3,1.5),(4,2),(2,99),(99,1)):
            r["pass_dd%g_wm%g"%(m1,m2)]=np.mean((ddd>=-m1)&(dwm>=-m2))
        rows.append(r); print(r,flush=True)
pd.DataFrame(rows).to_csv(P.os.path.join(P.RAW,"tail_probe.csv"),index=False)
