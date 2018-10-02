"""
Runner 
"""
from Workbench import Workbench
from Cleaner import Cleaner
from DOPS import DOPS

wb = Workbench('ccdata.csv', ['BALANCE', 'CREDIT_LIMIT'])

# Cleaning Functions
cl = Cleaner(wb.get_df())
cl.remove_nan()
wb.save_df(cl.get_df())  # Save cleaned df

# Report
wb.report()

dops = DOPS(wb.get_df())
dops.obfuscate(1, "X")
dops.get_obf_df()

