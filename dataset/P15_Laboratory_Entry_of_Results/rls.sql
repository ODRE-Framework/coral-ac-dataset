CREATE POLICY lab_insert_results ON Resultados_Pruebas
FOR INSERT
TO tecnico_lab
WITH CHECK (true);
-- Policy to allow reading only their own inserted
-- results or open orders can be added separately
