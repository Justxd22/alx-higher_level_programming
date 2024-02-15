-- states
SELECT i.id, i.name, s.name FROM cities i, states s WHERE i.state_id = s.id GROUP BY i.id ASC;