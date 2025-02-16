SELECT
    B.BOOK_ID,
    A.AUTHOR_NAME,
    DATE_FORMAT(B.PUBLISHED_DATE,"20%y-%m-%d") AS PUBLISHED_DATE
FROM  
    BOOK AS B
JOIN
    AUTHOR AS A
ON
    B.AUTHOR_ID = A.AUTHOR_ID
WHERE
    B.CATEGORY LIKE '경제'
ORDER BY
    PUBLISHED_DATE ASC