SELECT e.essayid_sql, e.essay, em.essay_set, em.ai_llm, em.ai_generated
FROM essay_raw e
JOIN essay_metadata em ON e.essayid_sql = em.essay_id;


SELECT tm.teacher_id, tm.teacher_grades, sm.student_id, sm.student_grade
FROM teacher_metadata tm
JOIN student_metadata sm ON tm.teacher_id = tm.teacher_id;


SELECT tm.teacher_id, tm.teacher_grades, sm.student_id, sm.student_grade
FROM teacher_metadata tm
JOIN student_metadata sm ON tm.teacher_id = sm.teacher_id;

SELECT essayid_sql, essay
FROM essay_raw;


