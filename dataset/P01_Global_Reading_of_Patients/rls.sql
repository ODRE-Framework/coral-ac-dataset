CREATE POLICY medico_read_all_patients ON Pacientes
FOR SELECT
TO medico
USING (true);
