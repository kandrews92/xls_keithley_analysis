def get_FilePaths(directory, extension=['']):
    """
    /*-----------------------------------------------------*/
    description:
        This function will generate the file names in a directory 
        tree by walking the tree either top-down or bottom-up. For each 
        directory in the tree rooted at directory top (including top itself), 
        it yields a 3-tuple (dirpath, dirnames, filenames).
    /*-----------------------------------------------------*/
    args: 
        directory: current path that is to be searched
        extension(s): specific file extension to be found.
                    defaults to empty, which will give all files
                    found in tree
    returns:
        file_paths: list of strings with each absolute path
    /*----------------------------------------------------*/
    """
    import os 
    file_paths = [] # init of list of strings to be returned

    # walk the tree
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath 
            filepath = os.path.join(root, filename)
            # check the filepath's extension, if wanted then add to list
            # if arg:extension is blank, then all files found in tree
            # will be added
            for ext in extension:
                if filepath.lower().endswith(ext) and 'analyzed' not in filepath:
                    file_paths.append(filepath) # add it to the list.
    return file_paths # self-explanatory

def get_DataFrames(xls_file):
    """
    /*-----------------------------------------------------*/
    description:
    	This function takes an instance of a pandas excel 
    	file (ex: xls = pd.ExcelFile(filename) ) and returns
    	two data frames from it. 
    	This function is specific to the settings for the 
    	keithley s4200 writing structure. 
    	The xls file has, by default, three sheets.
    	1. Data (contains all the measurement data)
    	2. Calc (blank and is skipped by default)
    	3. Settings (contains the measurement settings)
    /*-----------------------------------------------------*/
    args: 
        xls_file: an instance of pd.ExcelFile(filename)
    returns:
        data frames for each individual shet
    /*----------------------------------------------------*/
    """
    df0 = xls_file.parse(xls_file.sheet_names[0])
    df2 = xls_file.parse(xls_file.sheet_names[2])
    return df0, df2

def get_TestName(settings_dataframe):
    """
    /*-----------------------------------------------------*/
    description:
        The function gets the headers from the xls settings
        and returns the measurement type from the settings
        file.
    /*-----------------------------------------------------*/
    args: 
        settings_dataframe: data frame containing the 
        measurement settings from xls file.
    returns:
        a string containing the measurement type. The 
        options are:
            -'vgs-id#1@1'
            -'vds-id#1@1'
            -'res2t#1@1'
    /*----------------------------------------------------*/
    """
    return list(settings_dataframe)[1]

def get_LastExecuted(df):
    """
    /*-----------------------------------------------------*/
    description:
        Get the timestamp of the measurement from the 
        settings xls sheet / dataframe. 
        Because of the setup of the xls sheet named:
        'settings' this function searches the first column
        of the sheet (e.g. list(df)[0] ) and finds the 
        index of the phrase 'Last Executed' and uses that 
        index to return the measurement type string.
    /*-----------------------------------------------------*/
    args: 
        df: dataframe to be searched
    returns:
        a string containing the measurement type. The 
        options are:
            -'vgs-id#1@1'
            -'vds-id#1@1'
            -'res2t#1@1'
    /*----------------------------------------------------*/
    """
    headers = list(df) # len = 4
    # ['Test Name', 'Measurement Type', 'Unnamed: 2', 'Unnamed: 3']
    # loop over the data frame's first column
    for i in range(len(df[headers[0]])):
        if df[headers[0]][i] == 'Last Executed': # search for time
            last_exec_idx = i # store index 
    return df[headers[1]][last_exec_idx]

def get_OnlyFname(fobj):
    """
    /*----------------------------------------------------*/
    description:
        returns the file name only, without absolute path
    /*----------------------------------------------------*/
    args:
        fobj: a file name with absolute path included

    returns:
        string with file name 
    /*----------------------------------------------------*/     
    """
    left_index = fobj.rfind("\\") # find the split for the last dir in path
    right_index = fobj.rfind(".") # find the split for file ext
    return fobj[left_index+1:right_index]

def get_SubDir(fobj, delimiter="\\"):
    """
    /*----------------------------------------------------*/
    description:
        returns the subdir of fobj with absolute path of 
        type string
    /*----------------------------------------------------*/
    args:
        fobj: a file name with absolute path included
        delimiter: character to break at. default value 
        is '\' (\\ = \ in python)

    returns:
        string with file name and file extension stripped 
        but last slash still remains
    /*----------------------------------------------------*/     
    """
    index = fobj.rfind(delimiter)
    return fobj[:index+1]

def DisplayFiles(file_list, currpath, log):
    """
    /*-----------------------------------------------------*/
    description:
        This function will prints the files found using the 
        function get_filepaths in ordered method
    /*-----------------------------------------------------*/
    args: 
        file_list: a list of strings containing absolute
                    paths.
        mypath: the current top path that the script is run 
                from
    returns:
        None
    /*----------------------------------------------------*/
    """
    # count the number of files found in tree
    log.write("\n###--->\tFound %d files in %s\n" %(len(file_list), currpath))
    # loop and print the files found in sucessive order
    # and account for python's zero-indexing when outputting
    # the list. 
    for i in range(len(file_list)):
        log.write("\n###--->\t[%d] %s\n\n" %((i+1), file_list[i]))
    log.write("\n")

def CreateNewXLS(df, new_fame):
    """
    /*-----------------------------------------------------*/
    description:

    /*-----------------------------------------------------*/
    args: 

    returns:
        
    /*----------------------------------------------------*/
    """
    import pandas as pd 
    writer = pd.ExcelWriter(new_fame) # open new xls to write df
    df.to_excel(writer, index=False) # write w/o indicies
    writer.save() # save file under new name

def PutAllPngToPdf(directory, extension=['.png']):
    """
    /*-----------------------------------------------------*/
    description:

    /*-----------------------------------------------------*/
    args: 

    returns:
        
    /*----
    """
    from fpdf import FPDF
    import os 
    file_paths = [] # init of list of strings to be returned

    # walk the tree
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath 
            filepath = os.path.join(root, filename)
            # check the filepath's extension, if wanted then add to list
            # if arg:extension is blank, then all files found in tree
            # will be added
            for ext in extension:
                if filepath.lower().endswith(ext):
                    file_paths.append(filepath) # add it to the list.
    pdf = FPDF()
    for image in file_paths:
        pdf.add_page()
        pdf.image(image)
    pdf.output("yourfile.pdf", 'F')

def WriteDataFrameToQDA(df):
    from qdafile import QDAfile
    QDAfile(
        df,
        #headers=list(df)
        ).write('test.qda')