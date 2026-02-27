CREATE POLICY external_consult_access ON Historial_Clinico
FOR SELECT
TO medico_externo
USING (
id IN (
SELECT patient_id FROM Derivaciones
WHERE target_doctor_id = current_user_id()
AND expiry_date > NOW()
)
);
