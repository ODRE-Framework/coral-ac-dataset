CREATE POLICY guardian_read_minor ON Historial_Clinico
FOR SELECT
TO familiar
40
USING (
patient_id IN (
SELECT id FROM Pacientes
WHERE guardian_id = current_user_id()
AND age < 18
)
);
