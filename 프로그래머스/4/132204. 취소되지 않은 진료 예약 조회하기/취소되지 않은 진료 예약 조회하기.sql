# 2022년 4월 13일 취소되지 않은 흉부외과(CS) 진료 예약 내역

WITH VALUE as (SELECT 
    APNT_YMD,
    APNT_NO,
    MCDP_CD,
    MDDR_ID,
    PT_NO
FROM
    APPOINTMENT
WHERE
    APNT_CNCL_YN = 'N' 
    AND MCDP_CD = 'CS'
    AND APNT_YMD LIKE "2022-04-13%")
    
SELECT
    VALUE.APNT_NO as APNT_NO,
    P.PT_NAME as PT_NAME,
    P.PT_NO as PT_NO,
    VALUE.MCDP_CD as MCDP_CD,
    D.DR_NAME as DR_NAME,
    VALUE.APNT_YMD as APNT_YMD
FROM
    VALUE
JOIN
    PATIENT as P
ON
    VALUE.PT_NO = P.PT_NO
JOIN
    DOCTOR as D
ON
    VALUE.MDDR_ID = D.DR_ID
ORDER BY
    APNT_YMD ASC