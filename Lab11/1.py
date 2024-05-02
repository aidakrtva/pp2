#Function that returns all records based on a pattern 
#(example of pattern: part of name, surname, phone number)

#i created a table6 then created function
"""
CREATE OR REPLACE FUNCTION search_phonebook(pattern VARCHAR) #ну просто создала
RETURNS TABLE (first_name VARCHAR, phone VARCHAR) #показывает что будет return
AS $$  #just to get started 
#variable_conflict use_column  -- !!   #this is also nesseccery to work with code

BEGIN
    RETURN QUERY  #return запрос
    SELECT first_name, phone  #selecting name or phone 
    FROM contacts #working with our table 
    WHERE first_name ILIKE   '%' || pattern || '%'     OR phone ILIKE     '%' || pattern || '%'; #checks with pattern 
END;
$$ LANGUAGE plpgsql;  #the language that we are using

"""
#to use this function i need to write  "select * from (name of function) (pattern)"






