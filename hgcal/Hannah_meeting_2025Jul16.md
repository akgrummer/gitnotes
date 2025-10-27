        """
major types (could add tilemodule - add to maj types and make a table)
jjj
TEXT is the type in the cell
NOT NULL must be populated
unique must be
        CREATE TABLE IF NOT EXISTS Maj_Types (
        LD_Modules TEXT,
        HD_Modules TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS LD_Modules (
        barcode TEXT NOT NULL UNIQUE PRIMARY KEY,
        loc_at_fermi TEXT NOT NULL,
        qc_passed BOOLEAN,
        grade TEXT,
        alt_loc TEXT NOT NULL,
        alt_adc_tests TEXT NOT NULL,
        alt_pedestal_meas TEXT NOT NULL,
        alt_yaml_file TEXT,
        fermi_adc_tests TEXT,

not yet capable of holding more than one:
        fermi_yaml_file TEXT,
        fermi_pedestal_meas TEXT);
        """,
        """
        CREATE TABLE IF NOT EXISTS HD_Modules (
        barcode TEXT NOT NULL UNIQUE PRIMARY KEY,
        loc_at_fermi TEXT NOT NULL,
        qc_passed BOOLEAN,
        grade TEXT,
        alt_loc TEXT NOT NULL,
        alt_adc_tests TEXT NOT NULL,
        alt_pedestal_meas TEXT NOT NULL,
        alt_yaml_file TEXT NOT NULL,
        fermi_adc_tests TEXT,
        fermi_yaml_file TEXT,
        fermi_pedestal_meas TEXT);
        """


addPlain part is the
unpacking barcode files
updating dictionary wiht more entries

flexible code
learning about exceptinos and testing

sql call cant call by number first.
put in string "
