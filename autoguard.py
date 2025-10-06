import re, sys, os

PATTERNS = [r'AKIA[0-9A-Z]{16}', r'(?i)password\s*=\s*[\'"].+[\'"]']
issues = []

for root, _, files in os.walk('.'):
    for f in files:
        if f.endswith(('.py', '.js', '.env', '.yml', '.txt')):
            content = open(os.path.join(root, f)).read()
            for p in PATTERNS:
                if re.search(p, content):
                    issues.append(f"{f} → {p}")

if issues:
    print("🚨 AutoGuard detected potential secrets:")
    [print(i) for i in issues]
    sys.exit(1)
else:
    print("✅ No secrets found. Safe to deploy.")
