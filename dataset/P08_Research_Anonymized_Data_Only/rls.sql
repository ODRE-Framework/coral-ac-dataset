CREATE POLICY investigador_anonymized_only ON Historial_Clinico
FOR SELECT
TO investigador
USING (is_anonymized = true);
