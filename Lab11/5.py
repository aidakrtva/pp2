#Implement procedure to deleting data from tables by username or phone


"""
CREATE OR REPLACE PROCEDURE delet(
    deleted VARCHAR(255)
)

LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM contacts WHERE deleted = phone OR deleted = first_name;
END;
$$;

"""