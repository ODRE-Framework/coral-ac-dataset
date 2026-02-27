CREATE POLICY medico_prescribe_meds ON Medicacion
FOR INSERT, UPDATE
TO medico
WITH CHECK (true); -- Assigned patient restriction applies in P05
