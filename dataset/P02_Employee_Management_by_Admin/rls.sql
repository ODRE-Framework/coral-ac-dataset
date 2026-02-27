CREATE POLICY admin_full_access_empleados ON Empleados
FOR ALL
TO admin
USING (true)
WITH CHECK (true);
