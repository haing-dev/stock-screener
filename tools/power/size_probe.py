import sys, numpy as np
sys.argv=['x']; import power_3_3 as P
for sh in ("RULE_q10_L12","RULE_q25_L12","FULL432","STRIP250"):
    for rho in (0.0,):
        o,ir,td = P.run_cell(dict(P.SHAPES[sh], S=0.0), 2000, 1.23, rho)
        p=o["p_alpha"]
        print(sh, rho, "size@.025 %.4f @.05 %.4f @.10 %.4f"%((p<.025).mean(),(p<.05).mean(),(p<.1).mean()),
              "episodes med", np.median(o.get("episodes",[0])), "alpha t naive", end=' ')
        print("p quantiles", np.round(np.percentile(p,[1,2.5,5,10,50]),4))
