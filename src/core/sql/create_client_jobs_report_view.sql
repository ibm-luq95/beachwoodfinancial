CREATE OR REPLACE VIEW $view_name AS
SELECT 
  c.id AS client_id,
  c.name AS client_name,
  COUNT(CASE WHEN j.status = 'completed' THEN j.id END) AS job_completed_count,
  COUNT(CASE WHEN j.status = 'past_due' THEN j.id END) AS job_past_due_count,
  COUNT(CASE WHEN j.status = 'not_completed' THEN j.id END) AS job_not_completed_count,
  COUNT(CASE WHEN j.status = 'in_progress' THEN j.id END) AS job_in_progress_count,
  COUNT(CASE WHEN j.status = 'archive' THEN j.id END) AS job_archived_count,
  COUNT(CASE WHEN j.status = 'not_started' THEN j.id END) AS job_not_started_count,
  COUNT(CASE WHEN j.status = 'draft' THEN j.id END) AS job_draft_count,
  COUNT(j.id) AS total_jobs_count,
  c.created_at AS client_created_at,
  j.period_month AS job_period_month,
  j.period_year AS job_period_year
FROM
  client_client c
RIGHT JOIN job_job j ON c.id = j.client_id
GROUP BY
  c.id,
  c.name,
  job_period_month,
  job_period_year
ORDER BY
  c.name ASC,
  job_period_year DESC,
  job_period_month ASC;
