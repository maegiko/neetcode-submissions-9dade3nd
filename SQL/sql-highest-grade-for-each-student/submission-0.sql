-- Write your query below
create or replace view max_scores(student_id, exam_id, score)
as
select
    student_id,
    exam_id,
    score
from exam_results e1
where e1.score = (
    select max(e2.score)
    from exam_results e2
    where e2.student_id = e1.student_id
)
;

create or replace view max_scores_distinct(student_id, exam_id, score)
as
select * from max_scores m1
where m1.exam_id = (
    select min(m2.exam_id)
    from max_scores m2
    where m1.student_id = m2.student_id
)
;

select * from max_scores_distinct
order by student_id;