CREATE POLICY admin_no_create_cita_deudor ON Citas
FOR INSERT
TO administrativo
24
WITH CHECK (
patient_id NOT IN (
SELECT patient_id FROM Facturacion
WHERE financial_status = 'DEUDOR'
)
);
