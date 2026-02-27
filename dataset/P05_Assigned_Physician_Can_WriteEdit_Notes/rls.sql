CREATE POLICY medico_write_own_assigned ON Historial_Clinico
FOR UPDATE
TO medico
USING (assigned_doctor_id = current_user_id())
WITH CHECK (assigned_doctor_id = current_user_id());
CREATE POLICY medico_insert_own_assigned ON Historial_Clinico
FOR INSERT
TO medico
WITH CHECK (assigned_doctor_id = current_user_id());
