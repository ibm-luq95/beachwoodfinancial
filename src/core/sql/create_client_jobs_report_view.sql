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
  EXTRACT(MONTH FROM j.created_at) AS job_month,
  EXTRACT(YEAR FROM j.created_at) AS job_year
FROM
  client_client c
LEFT JOIN job_job j ON c.id = j.client_id
RIGHT JOIN (
  SELECT
    EXTRACT(MONTH FROM created_at) AS month,
    EXTRACT(YEAR FROM created_at) AS year
  FROM
    job_job
  GROUP BY
    EXTRACT(MONTH FROM created_at),
    EXTRACT(YEAR FROM created_at)
) AS months ON EXTRACT(MONTH FROM j.created_at) = months.month
  AND EXTRACT(YEAR FROM j.created_at) = months.year
GROUP BY
  c.id,
  c.name,
  job_month,
  job_year
ORDER BY
  job_year DESC,
  job_month DESC;