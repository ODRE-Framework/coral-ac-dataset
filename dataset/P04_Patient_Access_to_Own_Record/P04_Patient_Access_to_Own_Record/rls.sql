CREATE POLICY paciente_own_records ON Historial_Clinico
FOR SELECT
TO paciente
USING (patient_id = current_user_id());
