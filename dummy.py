import pathlib
from datetime import datetime, timedelta

LINES = 7
COLUMNS = 52
MULTIPLIER = 4

IMAGE = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 0, 0, 0, 0, 4, 4, 0, 4, 0, 4, 4, 4, 0, 4, 0, 0, 0, 4, 0, 0, 4, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 0, 0, 4, 0, 0, 0, 4, 0, 0, 4, 0, 0, 4, 0, 0, 4, 0, 4, 0, 4, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 0, 4, 0, 0, 0, 4, 0, 0, 4, 0, 0, 4, 0, 0, 4, 4, 4, 0, 4, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 0, 0, 4, 0, 4, 0, 4, 0, 0, 4, 0, 0, 4, 0, 0, 4, 0, 4, 0, 4, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 0, 0, 0, 0, 4, 4, 0, 4, 0, 0, 4, 0, 0, 4, 4, 0, 4, 0, 4, 0, 4, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
assert len(IMAGE) == LINES
for i in range(LINES):
    assert len(IMAGE[i]) == COLUMNS

COMMIT_TEMPLATE = 'GIT_AUTHOR_DATE={0} GIT_COMMITTER_DATE={0} git commit --allow-empty -m "dummy" > /dev/null'

output = ["git checkout main", "git reset --hard base"]
noon = datetime.now().replace(hour=12, minute=0, second=0, microsecond=0)
start_date = noon - timedelta(weeks=COLUMNS, days=(noon.weekday() + 1) % LINES)

for x in range(COLUMNS):
    for y in range(LINES):
        for _ in range(MULTIPLIER * IMAGE[y][x]):
            output.append(COMMIT_TEMPLATE.format((start_date + timedelta(days=x * LINES + y)).isoformat()))

output.append("git push origin main --force")

pathlib.Path("dummy.sh").write_text("\n".join(output))
