# goit-algo-hw-06

## Task 2

| №   | dfs steps:    | bfs steps:    |
| --- | ------------- | ------------- |
| 1   | Bob's House   | Bob's House   |
| 2   | Town Hall     | Town Hall     |
| 3   | Marketplace   | Marketplace   |
| 4   | Post Office   | Post Office   |
| 5   | Alice's House | Shop          |
| 6   | Cabin         | Alice's House |
| 7   | Shop          | Grete's House |
| 8   | Grete's House | Cabin         |
| 9   | Ernie's House | Ernie's House |
| 10  | Daria's House | Farm          |
| 11  | Farm          | Daria's House |

Крок № 5 вже відрізняється оскільки алгоритм dfs йде далі у глиб, а bfs спочатку перебере усіх сусідів вузла "Marketplace": "Post Office" і "Shop", і тільки потім перейде на наступний рівень в глиб графа.
