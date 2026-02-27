CREATE POLICY urgencias_emergency_access ON Historial_Clinico
FOR SELECT
TO medico_urgencias
USING (
	patient_id IN (
		SELECT id FROM Pacientes
		WHERE status IN ('CRITICO', 'EMERGENCIA')
	)
);
