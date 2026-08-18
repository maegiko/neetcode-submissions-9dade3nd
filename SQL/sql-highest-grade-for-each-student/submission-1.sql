-- Write your query below
select e1.student_id, e1.exam_id, e1.score
from exam_results e1
where e1.exam_id = (
    select e2.exam_id
    from exam_results e2
    where e1.student_id = e2.student_id
    order by e2.score desc, e2.exam_id asc
    limit 1
)
order by student_id asc;