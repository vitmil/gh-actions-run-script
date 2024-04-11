import os

print('\nHello Unit Test!\n')

ci_cd_outcome = os.getenv('CI_CD_OUTCOME')
if ci_cd_outcome == "OK":
    print("[OK]: Il valore della variabile settata dal workflow-action è == a OK")
else:
    print("[OK]: Il valore della variabile settata dal workflow-action è == a OK")
    exit(1)



