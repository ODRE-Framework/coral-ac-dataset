CREATE POLICY pharma_dispense ON Medicacion
FOR SELECT, UPDATE
TO farmaceutico
USING (status = 'PENDIENTE')
WITH CHECK (status = 'DISPENSADO');
