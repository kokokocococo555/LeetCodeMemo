# LeetCode勉強記録（SQL編）

- LeetCodeの勉強記録
- 自力で実装したコードの他にも、Solution, Discussionに投稿されている内容等を参照し、自分でも実装してみる
- 復習が必要な問題には▲をつけている
- 使用言語は`MySQL`

## Easy
### [175. Combine Two Tables](https://leetcode.com/problems/combine-two-tables/)

- 2つのテーブルをPersonIdをキーにして左外部結合する
    - 結合するテーブル名、キーはFROM句に書く

```sql
select FirstName, LastName, City, State
from Person LEFT OUTER JOIN Address ON Person.PersonId=Address.PersonId;
```

### [176. Second Highest Salary](https://leetcode.com/problems/second-highest-salary/)

- 普通にMySQLを書いたが、レコードが1つのケースに対応できず
- Solutionではサブクエリ、または`IFNULL`関数を使用
    - `IFNULL(x1, x2)`...x1がNULLでない場合はx1を返し、NULLの場合はx2を返す
    - 似た関数に`IF(x1, x2, x3)`もある
        - x1がTRUEの場合はx2, FALSEの場合はx3を返す
    - 重複を削除するには`SELECT DISTINCT ...`を使用

```sql
-- Solutionを参考に実装
SELECT
    (SELECT DISTINCT Salary
    FROM Employee
    ORDER BY Salary DESC
    LIMIT 1
    OFFSET 1) AS SecondHighestSalary
;
```

```sql
-- IFNULL版（Solutionを参考に実装）
SELECT
    IFNULL(
        (SELECT DISTINCT Salary
         FROM Employee
         ORDER BY Salary DESC
         LIMIT 1 OFFSET 1),
        NULL) AS SecondHighestSalary
;
```

### [181. Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/)

- 自己結合してWHEREで条件付けて抽出した

```sql
-- 自力実装
SELECT e.Name AS Employee
    FROM Employee AS e
    LEFT OUTER JOIN Employee AS m ON e.ManagerId=m.Id
    WHERE e.Salary>m.Salary
;
```

### [182. Duplicate Emails](https://leetcode.com/problems/duplicate-emails/)

- ググって実装
    - [参考にした記事](https://qiita.com/necoyama3/items/4c24defd6f504366aebe)

```sql
-- 記事を参考に実装
SELECT DISTINCT
    Email
FROM 
    Person
GROUP BY
    Email
HAVING
    COUNT(Email) > 1
```

### [183. Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/)

- 書籍を見ながら、`NOT EXISTS`を用いたサブクエリを使用
- Solutionでは`NOT IN`を使用していた
    - `NOT EXISTS`の方が速い

```sql
-- 自力実装
SELECT
    Name AS 'Customers'
FROM
    Customers AS c
WHERE NOT EXISTS
    (SELECT
        *
     FROM
        Orders AS o
     WHERE
        c.Id = o.CustomerId)
;
```

```sql
-- NOT IN（Solutionを参考に実装）
SELECT
    Name AS 'Customers'
FROM
    Customers AS c
WHERE 
    c.Id NOT IN
    (SELECT
        CustomerId
     FROM
        Orders)
;
```

### [196. Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/)

- ググって実装
    - [参考にした記事](https://qiita.com/aosho235/items/d748dcb6386d8ce75604)
- Solutionでは`WHERE`句で`p1.Email = p2.Email AND p1.Id > p2.Id`として削除していた
    - Solutionの方が遅い

```sql
-- 記事を参考にした自力実装
DELETE
FROM
    Person
WHERE
    Id NOT IN 
        (SELECT
            min_id
         FROM
            (SELECT
                MIN(Id) AS min_id
            FROM
                Person
            GROUP BY
                Email) tmp
        )
;
```

```sql
-- Solutionを参考に実装
DELETE
    p1
FROM
    Person AS p1,
    Person AS p2
WHERE
    p1.Email = p2.Email AND
    p1.Id > p2.Id
;
```

### ▲[197. Rising Temperature](https://leetcode.com/problems/rising-temperature/)

- 分からず
    - MySQLの詳しい文法や道具をもっと知る必要あり
- ▲Solutionやそこにあるコメントを見ると、`SUBDATE()`や`DATEDIFF()`を使用している

```sql
-- SUMDATE()を使用（Solutionのコメントを参考に実装）
SELECT
    Weather.Id AS 'Id'
FROM
    Weather
JOIN
    Weather AS w
ON w.RecordDate = SUBDATE(Weather.RecordDate, 1)
WHERE
    Weather.Temperature > w.Temperature
;
```

```sql
-- DATEDIFF()を使用（Solutionのコメントを参考に実装）
SELECT
    t.Id AS 'Id'
FROM
    Weather AS t,
    Weather AS y
WHERE
    DATEDIFF(t.RecordDate, y.RecordDate) = 1
    AND t.Temperature > y.Temperature
;
```

