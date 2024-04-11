import os
import sys

print('\nHello Unit Test!\n')

ci_cd_outcome = os.getenv('CI_CD_OUTCOME')
if ci_cd_outcome == "OK":
    print("[OK]: Il valore della variabile settata dal workflow-action è == a OK")
    sys.exit(0)
else:
    print("[OK]: Il valore della variabile settata dal workflow-action è == a OK")
    sys.exit(1)



