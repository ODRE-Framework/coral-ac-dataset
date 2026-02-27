CREATE POLICY admin_no_create_cita_deudor ON Citas
FOR INSERT
TO administrativo
WITH CHECK (
	patient_id NOT IN (
		SELECT patient_id FROM Facturacion
		WHERE financial_status = 'DEUDOR'
	)
);
