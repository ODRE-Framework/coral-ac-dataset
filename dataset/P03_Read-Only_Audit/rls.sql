CREATE POLICY auditor_read_only_historial ON Historial_Clinico
FOR SELECT
TO auditor
USING (true);
CREATE POLICY auditor_read_only_facturacion ON Facturacion
FOR SELECT
TO auditor
USING (true);
CREATE POLICY auditor_no_write ON Historial_Clinico
FOR UPDATE, DELETE, INSERT
TO auditor
USING (false);
CREATE POLICY auditor_no_write_fact ON Facturacion
FOR UPDATE, DELETE, INSERT
TO auditor
USING (false);
