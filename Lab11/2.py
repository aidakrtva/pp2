#Create procedure to insert new 
#user by name and phone, update phone if user already exists

#i created propertie line this:

"""
CREATE OR REPLACE PROCEDURE iouu(
    user_name VARCHAR(255),
    user_phone VARCHAR(11)
)
LANGUAGE plpgsql
AS $$



BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE first_name = user_name) THEN
        UPDATE PhoneBook
        SET phone = user_phone
        WHERE first_name = user_name;
    ELSE
        INSERT INTO contacts (first_name,second_name, phone)
        VALUES ( user_name, second_name, user_phone);
    END IF;
END;
$$;

"""

#to call this:

"""
call iouu('name','second name','phone')

then i need to select all from my table 

"""