CREATE POLICY enfermero_shift_access ON Medicacion
FOR SELECT, UPDATE
TO enfermero
USING (
CURRENT_TIME >= (
SELECT shift_start FROM Empleados
WHERE id = current_user_id()
)
AND
CURRENT_TIME <= (
SELECT shift_end FROM Empleados
WHERE id = current_user_id()
)
);
