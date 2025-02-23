SELECT
    SUM(SCORE) SCORE, E.EMP_NO, EMP_NAME, POSITION, EMAIL
FROM
    HR_EMPLOYEES AS E
JOIN
    HR_GRADE AS G
ON
    E.EMP_NO = G.EMP_NO
GROUP BY
    G.EMP_NO
ORDER BY
    SCORE DESC
LIMIT
    1