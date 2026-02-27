CREATE POLICY jefe_read_department_patients ON Historial_Clinico
FOR SELECT
TO jefe_departamento
USING (
	patient_id IN (
		SELECT id FROM Pacientes
		WHERE department_id = current_user_department()
	)
);
