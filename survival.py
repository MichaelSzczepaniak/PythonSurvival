import numpy as np
import pandas as pd

# Appends 
def appendAtRisk(sdata, init_risk,
                 time2e_name = 'Time2E',
                 event_name = 'EventCount',
                 censor_name = 'CensorCount',
                 at_risk_name = 'AtRiskCount'):
    risk_col = [init_risk]
    for i in range(1, sdata.shape[0]):
        risk_col.append(risk_col[i-1] - sdata.loc[i-1, event_name] - sdata.loc[i-1, censor_name])
        # print(sdata.loc[i-1, event_name])
    
    sdata[at_risk_name] = pd.Series(risk_col).values
    # reorder col's to look like example spreadsheet
    sdata = sdata[[time2e_name, at_risk_name, event_name, censor_name]]
    
    return sdata