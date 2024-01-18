
Pones todas tus funciones aquí, las importas a tu jupyter notebook y las llamas desde ahí.


def replace_str_values(df, column_name, original_value, new_value):
    #Best practice is to add a comment inside the function to explain what it does, so anyone knows what to expect. And it is always best to use clear names of variables, instead of x,y 
    '''
    This function updates a value contained inside a column of a daframe:
    Input:
        df: name of the dataframe
        column_name: name of a column that includes the value to be changed
        original_value: value to be changed
        new_value: value that will replace the original value
    Output:
        The same dataframe's column with the new values replacing the original values
    '''    
    return df[column_name].str.replace(original_value, new_value)


## SECOND FUNCTION

def rename_col(df, column_name, new_column_name):
    '''
    This function renames a column from a dataframe
    Input:
        df: name of the dataframe
        column_name: name of the column that will be renamed
        new_column_name: the new name of the columns
    Output:
        A dataframe with the renamed column
    
    '''
    return df.rename(columns = {column_name:new_column_name}, inplace = True) 